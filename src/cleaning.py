import pandas as pd
import numpy as np

def clean_loan_data(df):
    
    #drop leakage columns
    def drop_leakage_columns(df):
        leakage_columns = ['loan_status', 'balance', 'paid_total', 'paid_principal', 'paid_interest', 'paid_late_fees']

        df.drop(columns=[c for c in leakage_columns if c in df.columns], inplace = True)
    
    drop_leakage_columns(df)
    return df