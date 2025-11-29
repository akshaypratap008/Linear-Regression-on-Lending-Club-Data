Shape of raw data:
- 10000 rows 
- 55 features/columns

Removing columns which are not important for the projects and can lead to data leakage
Columns to be dropped: ['loan_status', 'balance', 'paid_total', 'paid_principal', 'paid_interest', 'paid_late_fees']

High missingness in particularly these columns
annual_income_joint                 85.05
verification_income_joint           85.45
debt_to_income_joint                85.05
They are all related to join applications. We will drop joint applications and all the columns associated with them

Missing values in months_since_last_delinq and months_since_90d_late --> impute them with max + 1, 0 can be misinterpretted by the model. 

Missing values in emp_length, debt_to_income --> impute them with median

missing values in months_since_last_credit_inquiry and num_accounts_120d_past_due --> impute with max + 1

earliest_credit_line --> change from years to years_since_first_credit (current year - earlier_credit_line)

Divide data into 3 buckets (borrower_profile, credit_history, loan_details)

'emp_length' -- borrower_profile
'state' -- borrower_profile 
'homeownership' -- borrower_profile
'annual_income' -- borrower_profile
'verified_income' -- borrower_profile 
'debt_to_income' -- borrower_profile 

'delinq_2y' -- credit_history
'months_since_last_delinq' -- credit_history 
'years_since_first_credit' -- credit_history
'inquiries_last_12m' -- credit_history 
'total_credit_lines' -- credit_history 
'open_credit_lines' -- credit_history
'total_credit_limit' -- credit_history
'total_credit_utilized' -- credit_history
'num_collections_last_12m' -- credit_history
'num_historical_failed_to_pay' -- credit_history
'months_since_90d_late' -- credit_history 
'current_accounts_delinq' -- credit_history
'total_collection_amount_ever' -- credit_history 
'current_installment_accounts' -- credit_history
'accounts_opened_24m' -- credit_history
'months_since_last_credit_inquiry' -- credit_history
'num_satisfactory_accounts' -- credit_history 
'num_accounts_120d_past_due' -- credit_history
'num_accounts_30d_past_due' -- credit_history
'num_active_debit_accounts' -- credit_history
'total_debit_limit' -- credit_history
'num_total_cc_accounts' -- credit_history
'num_open_cc_accounts' -- credit_history
'num_cc_carrying_balance' -- credit_history 
'num_mort_accounts' -- credit_history
'account_never_delinq_percent' -- credit_history
'tax_liens' -- credit_history
'public_record_bankrupt' -- credit_history

'loan_purpose' -- loan_details 
'application_type' -- loan_details
'loan_amount' -- loan_details 
'term' -- loan_details
'interest_rate' -- loan_details 
'installment' -- loan_details 
'grade' -- loan_details 
'sub_grade' -- loan_details 
'issue_month' -- loan_details
'initial_listing_status' -- loan_details 
'disbursement_method' -- loan_details


### EDA- borrower's profile
annual_income -- heavily right skewed. Log transformation needed, created new col in temp data
debt_to_income -- heavily right skewed, log transformation needed, created new col in temp data

emp_length -- uniform throughout, drop the columns
states have high cardiniality -- colapse less popular states into others
renters have slightly high interest rates as compared to homeowners and morgage people, morgage and home owners have similar midean -- change them is_renter (0 or 1) - created a new col in temp_data

### EDA- credit history
As per heatmap - 
columns with strong/moderate correlation with interest rates - months_since_last_delinq, inquiries_last_12m, total_credit_limit, months_since_90d_late, month_since_last_credit_inquiry, total_debit_limit, num_mort_accounts, account_never_delinq_percent, months_since_90d_late, accounts_opened_24m, inquiries_last_12m, delinq_2y

remove num_satisfactory line --> heavily correlated to open_credit_lines
remove curr_accounts_delinq --> heavily correlated with num_accounts_30d_past_due
remove total_credit_lines --> heavily correlated with open_credit_lines
remove num_total_cc_accounts --> heavily correlated with open_credit_lines
remove num_open_cc_accounts --> correlated with open_credit_lines
remove num_cc_carrying_balance --> correlated with num_open_cc_accounts 

drop tax_liens as correlation with num_historical_failed_to_pay is high and num_historical_fail_to_pay has higher correlation with interest_rate than tax_liens
-----------------------------------------
create buckets like delinquency_fetaures, credit_activity, limit_utilisation, account_composition, public_records

delinq_features = ['delinq_2y', 'months_since_last_delinq', 'num_historical_failed_to_pay', 'months_since_90d_late', 'num_accounts_120d_past_due', 'num_accounts_30d_past_due', 'account_never_delinq_percent', ]

credit_activity = ['years_since_first_credit', 'inquiries_last_12m', 'open_credit_lines', 'total_credit_utilized', 'months_since_last_credit_inquiry', ]

limit_utilisation = ['total_debit_limit', 'total_credit_limit']

account_composition = ['current_installment_accounts', 'accounts_opened_24m', 'num_active_debit_accounts', 'num_mort_accounts', ]

public_records = ['num_collections_last_12m', 'total_collection_amount_ever', 'public_record_bankrupt']
-----------------------------------------
delinq features analysis
drop features in delinq_feature bucket which have less than 0.1 corr() with interest rate 

months_since_last_delinq --> need square transformation

most values in months_since_90d_due are 129 which is a sentinel values. Created a new column 'never_late_payment' with values 0 and 1. 1 for late payments in past 90days
- never_late_payment have slightly lesser interest rates as expected

column account_never_delinq_percent --> split them into bins [-1, 80, 95, 99, 100] and label ['High Risk', 'Moderate Risk', 'Low Risk', 'Perfect']
- interest rates goes down as risk decreases
-----------------------------------------
credit activity bucket analysis
inquiries_last_12m and months_since_last_credit_inquiry are the only two feature strongly correlated with interest rate(corr > 0.1). They are both heavily correlated. Droping all other features, except inquiries_last_12m
-----------------------------------------
limit Utilisation bucket analysis
Both columns highly correlated with interest rates. Both are heavily correlated with each other as well. To avoid multicollinearity, only keep total_debit_limit
------------------------------------------
Account composition analysis
All the features except current_install_ment_accounts have slightly higher corr with interest rates. num_active_debit_accounts have the highest corr. 
Drop current_installment_accounts
num_active_debit_accounts right skewed, highly correlated with interest rates. Log transformation column created. 
------------------------------------------
Public Recods analysis
very little correlation with interest rates





