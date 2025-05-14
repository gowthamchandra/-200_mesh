cols=['Timestamp_From','Timestamp_To','Special_Filling_temp','Special_Filling_Flow','First_Agglo_Tank_Temp_T42','Tank_47_Temp',
 'PPT-48_Temperature','Fine_Seed_Tonnage','Fine_Seed_Flow','Fine_Seed_Density','Fine_Seed_Charge','Fine_Seed_SSA','Fine_Seed_3_5u',
 'Fine_Seed_45u','Fine_Seed_D50','PHE_Inlet_Temp','PHE_Outlet_Temp','Regular_Filling_Flow','Tank__52_Temp','Tank__56_Temp',
 'Coarse_Seed_1_Tonnage','Coarse_Seed_2_Tonnage','Coarse_Seed_2_Flow','Coarse_Seed_1_Density','Coarse_Seed_2_Density',
 'HAT_3_5u','HAT_45u','HAT_D50','Filling_Concentration','Filling_Ratio','Batch_Circulation_Hrs','Feed_Hydrate_D50',
 'Feed_Hydrate_SSA','Date']

final_cols=['Timestamp_To','Special_Filling_Flow','Fine_Seed_Tonnage','Fine_Seed_Flow','Fine_Seed_Density',
                        'Fine_Seed_SSA','Fine_Seed_3_5u','Fine_Seed_45u','Fine_Seed_D50','PHE_Inlet_Temp','Regular_Filling_Flow',
                        'Coarse_Seed_1_Tonnage','Coarse_Seed_2_Flow','HAT_3_5u','HAT_45u','HAT_D50','Filling_Ratio','Feed_Hydrate_D50','Feed_Hydrate_200']

columns_to_aggregate = ['Special_Filling_temp','Special_Filling_Flow','First_Agglo_Tank_Temp_T42',
                        'Fine_Seed_Tonnage','Fine_Seed_Flow','Fine_Seed_Density',
                       'PHE_Inlet_Temp','PHE_Outlet_Temp','Regular_Filling_Flow','Tank__52_Temp','Tank__56_Temp',
                        'Coarse_Seed_1_Tonnage','Coarse_Seed_2_Tonnage','Coarse_Seed_2_Flow','Coarse_Seed_1_Density',
                        'Coarse_Seed_2_Density',]
columns_to_resample = ['Fine_Seed_SSA','Fine_Seed_3_5u','Fine_Seed_45u','Fine_Seed_D50','HAT_3_5u','HAT_45u','HAT_D50',
                       'Filling_Concentration','Filling_Ratio','Feed_Hydrate_D50','Feed_Hydrate_SSA','Feed_Hydrate_200']

resample_frequency = '24H'

agg_functions = {
    'min': 'min',
    'max': 'max',
    'median': 'median',
    'mean': 'mean',
    'std': 'std', 
    'var': 'var', 
    'var_coeff': lambda x: x.std() / x.mean() if x.mean() != 0 else 0 
}

min_days = 21
max_days = 34
shifts_per_day = 1

IST_TIMEZONE = 'Asia/Kolkata'

Next_Predictions = True

Next_Predictions = True

best_cols = '/Users/gowtham/Downloads/Final_200/model_pickles/precip_final_cols.pkl'

best_model = '/Users/gowtham/Downloads/Final_200/model_pickles/Light_gbm_model_22-01-2024.pkl'
