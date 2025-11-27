import pandas as pd
import numpy as np

   
#drop leakage columns
def drop_leakage_columns(df):
    leakage_columns = ['loan_status', 'balance', 'paid_total', 'paid_principal', 'paid_interest', 'paid_late_fees', 'annual_income_joint', 'emp_title', 'verification_income_joint', 'debt_to_income_joint']

    df.drop(columns=[c for c in leakage_columns if c in df.columns], inplace = True)
    return df

def fill_with_max(df, col):
    df[col] = df[col].fillna(np.max(df[col]) + 1)
    return df
    
def fill_with_median(df, col):
    df[col] = df[col].fillna(np.median(df[col]))
    return df