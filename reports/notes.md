Shape of raw data:
- 10000 rows 
- 55 features/columns

Columns:
    ['emp_title', 
    'emp_length', 
    'state', 
    'homeownership', 
    'annual_income',
    'verified_income', 
    'debt_to_income', 
    'annual_income_joint',
    'verification_income_joint', 
    'debt_to_income_joint', 
    'delinq_2y',
    'months_since_last_delinq', 
    'earliest_credit_line',
    'inquiries_last_12m', 
    'total_credit_lines', 
    'open_credit_lines',
    'total_credit_limit', 
    'total_credit_utilized',
    'num_collections_last_12m', 
    'num_historical_failed_to_pay',
    'months_since_90d_late', 
    'current_accounts_delinq',
    'total_collection_amount_ever', 
    'current_installment_accounts',
    'accounts_opened_24m', 
    'months_since_last_credit_inquiry',
    'num_satisfactory_accounts', 
    'num_accounts_120d_past_due',
    'num_accounts_30d_past_due', 
    'num_active_debit_accounts',
    'total_debit_limit', 
    'num_total_cc_accounts', 
    'num_open_cc_accounts',
    'num_cc_carrying_balance', 
    'num_mort_accounts',
    'account_never_delinq_percent', 
    'tax_liens', 
    'public_record_bankrupt',
    'loan_purpose', 
    'application_type', 
    'loan_amount', 
    'term',
    'interest_rate', 
    'installment', 
    'grade', 
    'sub_grade', 
    'issue_month',
    'loan_status', 
    'initial_listing_status', 
    'disbursement_method',
    'balance', 
    'paid_total', 
    'paid_principal', 
    'paid_interest',
    'paid_late_fees']

Removing columns which are not important for the projects and can lead to data leakage
Columns to be dropped: ['loan_status', 'balance', 'paid_total', 'paid_principal', 'paid_interest', 'paid_late_fees']

High missingness in particularly these columns
annual_income_joint                 85.05
verification_income_joint           85.45
debt_to_income_joint                85.05
They are all related to join applications. We will drop join applications and all the columns associated with them

Missing values in months_since_last_delinq and months_since_90d_late
impute them with max + 1, 0 can be misinterpretted by the model. 

Missing values in emp_length, debt_to_income --> impute them with median

Missing values in 
