import os
import pandas as pd
from decouple import config


DB_NAME = config('DB_NAME', 'hindalco_rdsdb')
DB_HOST = config('DB_HOST', 'dna-hindalco-rds-pg.cjyp7b59bidu.ap-south-1.rds.amazonaws.com')
DB_PORT = config('DB_PORT', 5432)
DB_USER = config('DB_USER','hinrdashok' )
DB_PASSWORD = config('DB_PASSWORD','Wdfg59TBczWQ9')

DB_SCHEMA = config('DB_SCHEMA', 'dna_belghavi')
DB_TABLE = '.'.join((DB_SCHEMA, config('DB_TABLE', 'Precipitation_Raw_Data_hourly')))
DB_PRED_TABLE = '.'.join((DB_SCHEMA, config('DB_TABLE', 'Precipitation_PSD_Preds')))

SENDER_ID = config('SENDER_ID', 'abg-group.dna@adityabirla.com')
SENDER_PASSWORD = config('SENDER_PASSWORD', 'vryfvgxrtlgrjdjq')

SMTP_SERVER = config('SMTP_SERVER', 'smtp.office365.com')
SMTP_PORT = config('SMTP_PORT', 587)

PRED_MAIL_RECIPIENTS = config('PRED_MAIL_RECIPIENTS', "pooja.kumarnaik@adityabirla.com,kaushalkishore.gupta@adityabirla.com,remzyalirasheedpk@adityabirla.com")

ERR_MAIL_RECIPIENTS = config('ERR_MAIL_RECIPIENTS', "ashok.gudipadu-v@adityabirla.com,deepu.nahak-v@adityabirla.com")

# PRED_MAIL_RECIPIENTS = config('PRED_MAIL_RECIPIENTS', "ashok.gudipadu-v@adityabirla.com,ashish.chopra@adityabirla.com,shreyak.tare@adityabirla.com,abhishek.r.singh@adityabirla.com")

PRED_CC_RECIPIENTS = config('PRED_CC_RECIPIENTS', "ashok.gudipadu-v@adityabirla.com")

#PRED_CC_RECIPIENTS = config('PRED_CC_RECIPIENTS', "abhishek.r.singh@adityabirla.com,shreyak.tare@adityabirla.com,ashish.chopra@adityabirla.com,sachin.gadkari@adityabirla.com")

PRED_MAIL_SUBJECT = config('PRED_MAIL_SUBJECT', "Alumina Plant Predictive Alert: PSD Forecast for 14-Day Outlook")

PRED_ERROR_SUBJECT = config('PRED_ERROR_SUBJECT', "Alumina Plant Predictive Alert: ERROR in Predictive Script")