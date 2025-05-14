import pandas as pd
from utils.constants import columns_to_aggregate,columns_to_resample,resample_frequency,agg_functions
from datetime import datetime, timedelta

def replace_outliers_with_median(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    median = data.median()
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data.apply(lambda x: x.where((x.between(lower_bound[x.name], upper_bound[x.name])) | x.isna(), median[x.name]))
    
    return data


def initial_data_preprocessing(treated_agg_data):
    min_timestamp = treated_agg_data['Timestamp_To'].min()
    print(min_timestamp)
    timestamp_1hr_before = min_timestamp - pd.Timedelta(hours=1)
    timestamp_2hr_before = min_timestamp - pd.Timedelta(hours=2)
    new_rows_dynamic = [
    {col: timestamp_1hr_before if col == 'Timestamp_To' else pd.NA for col in treated_agg_data.columns},
    {col: timestamp_2hr_before if col == 'Timestamp_To' else pd.NA for col in treated_agg_data.columns}]
    new_rows_df_dynamic = pd.DataFrame(new_rows_dynamic)
    data_extended_dynamic = pd.concat([new_rows_df_dynamic, treated_agg_data], ignore_index=True)
    data_extended_dynamic.sort_values(by='Timestamp_To', inplace=True)
    data_extended_dynamic.reset_index(drop=True, inplace=True)
    data_extended_dynamic['Timestamp_To'] = data_extended_dynamic['Timestamp_To'] + pd.Timedelta(hours=1)
    data_extended_dynamic.set_index('Timestamp_To', inplace=True)
    
    return data_extended_dynamic



def data_aggregation(df):
    resampled_df = pd.DataFrame()
    for feature in df.columns:
        if feature in columns_to_aggregate:
            for agg_name, agg_func in agg_functions.items():
                new_feature_name = f'{feature}_{agg_name}'
                resampled_df[new_feature_name] = df[feature].resample(resample_frequency).apply(agg_func)
        elif feature in columns_to_resample:
            resampled_df[feature] = df[feature].resample(resample_frequency).mean()
            
    resampled_df.reset_index(inplace=True)
    resampled_df['Timestamp_To'] = resampled_df['Timestamp_To'] + pd.Timedelta(hours=6)
    return resampled_df

def data_filter(resampled_df):
    resampled_df_sorted = resampled_df.sort_values(by='Timestamp_To', ascending=False)
    for index, row in resampled_df_sorted.head(5).iterrows():
        if pd.isna(row['Feed_Hydrate_D50']):
            resampled_df_sorted = resampled_df_sorted.drop(index)
    resampled_df = resampled_df_sorted.sort_values(by='Timestamp_To')
    return resampled_df

def calculate_lag_dates(target_date_str, min_shifts, max_shifts, shifts_per_day):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M")
    min_lag_days = min_shifts // shifts_per_day
    max_lag_days = max_shifts // shifts_per_day
    max_lag_extra_shifts = max_shifts % shifts_per_day
    start_date_min_lag = target_date - timedelta(days=min_lag_days)
    start_date_max_lag = target_date - timedelta(days=max_lag_days, hours=max_lag_extra_shifts * 8)
    return start_date_min_lag, start_date_max_lag

def preparing_lag_data(df):
    for column in df.columns:
        for i in range(39,84):
            nth_last_value = df[column].iloc[-(i - 38)]
            new_column_name = f'{column}_shift_{i}'
            df[new_column_name] = pd.NA
            df.at[df.index[-1],new_column_name] = nth_last_value
    df_lag_cleaned = df.dropna()
    return df_lag_cleaned

def get_predict_shift(df):
    hour_now=df['Timestamp_To'].dt.hour[0]
    if hour_now < 14:  # Before 2 PM
        if hour_now < 6:  # Before 6 AM
            shift = "C"  # Previous day's night shift
        else:
            shift = "A"  # Morning shift
    elif hour_now < 22:  # Between 2 PM and 10 PM
        shift = "B"  # Afternoon shift
    else:
        shift = "C"  # Night shift
    predicted_hour=df['Timestamp_To'][0]
    return shift,predicted_hour

    