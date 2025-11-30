# 1. Dataset Overview
Raw shape: 10,000 rows × 55 columns

Dropped leakage columns: ['loan_status', 'balance', 'paid_total', 'paid_principal', 'paid_interest', 'paid_late_fees']

Joint application columns: High missingness (>85%) → dropped all joint-related features (annual_income_joint, verification_income_joint, debt_to_income_joint)

# 2. Missing Value Handling
months_since_last_delinq, months_since_90d_late → imputed with max + 1 (to avoid misinterpreting 0 as valid)

emp_length, debt_to_income → imputed with median

months_since_last_credit_inquiry, num_accounts_120d_past_due → imputed with max + 1

earliest_credit_line → transformed into years_since_first_credit (current year – earliest credit year)

# 3. Feature Buckets
Organized into three main groups:

Borrower Profile: emp_length, state, homeownership, annual_income, verified_income, debt_to_income

Credit History: delinquency, credit activity, limit utilization, account composition, public records

Loan Details: loan_purpose, application_type, loan_amount, term, installment, grade, sub_grade, issue_month, initial_listing_status, disbursement_method, interest_rate

## 4. Borrower Profile Analysis
annual_income → heavily right-skewed → log transform (log_transformed_annual_income)

debt_to_income → heavily right-skewed → log transform (log_transformed_debit_to_income)

emp_length → uniform distribution → dropped

state → high cardinality → collapsed rare states into "other" (state_grouped)

homeownership → renters show slightly higher interest rates → created a binary flag is_renter

## 5. Credit History Analysis
Correlation Highlights
Strong/moderate correlation with interest_rate: months_since_last_delinq, inquiries_last_12m, total_credit_limit, months_since_90d_late, total_debit_limit, num_mort_accounts, account_never_delinq_percent, accounts_opened_24m, delinq_2y

Feature Reductions
Dropped due to redundancy:
num_satisfactory_accounts, current_accounts_delinq, total_credit_lines, num_total_cc_accounts, num_open_cc_accounts, num_cc_carrying_balance

Dropped due to overlap:
tax_liens (correlated with num_historical_failed_to_pay, which had stronger signal)

### Buckets
Delinquency Features: delinq_2y, months_since_last_delinq, num_historical_failed_to_pay, months_since_90d_late, num_accounts_120d_past_due, num_accounts_30d_past_due, account_never_delinq_percent

Credit Activity: years_since_first_credit, inquiries_last_12m, open_credit_lines, total_credit_utilized, months_since_last_credit_inquiry

Limit Utilization: total_debit_limit, total_credit_limit

Account Composition: current_installment_accounts, accounts_opened_24m, num_active_debit_accounts, num_mort_accounts

Public Records: num_collections_last_12m, total_collection_amount_ever, public_record_bankrupt

### 5.1 Detailed Bucket Analysis
### 5.1.1 Delinquency Features
Dropped features with correlation <0.1

months_since_last_delinq, left skewed→ squared transform (square_months_since_last_delinq)

months_since_90d_late → sentinel values (129) → created binary flag never_late_payment

account_never_delinq_percent → binned into risk categories (High Risk, Moderate Risk, Low Risk, Perfect) → new feature delinq_risk_category

### 5.1.2 Credit Activity
Only inquiries_last_12m retained (strongest correlation)

Dropped others due to redundancy

### 5.1.3 Limit Utilization
Both total_debit_limit and total_credit_limit correlated with interest rate

To avoid multicollinearity → kept only total_debit_limit (later log-transformed)

### 5.1.4 Account Composition
Dropped current_installment_accounts (weak correlation)

num_active_debit_accounts → strongest correlation, log-transformed (log_num_active_debit_accounts)

Kept accounts_opened_24m and num_mort_accounts

### 5.1.5 Public Records
Very weak correlation with interest rate

Still kept public_record_bankrupt (binary flag engineered as has_bankruptcy) for interpretability

## 6. Loan Details Analysis
loan_purpose → collapsed rare categories into "other_purpose"; boxplots confirmed signal

application_type → categorical, to be one-hot encoded

loan_amount → right-skewed → log transform (log_loan_amount)

installment → dropped (redundant)

term → categorical (36 vs 60 months)

grade / sub_grade → flagged as potential leakage with interest_rate

Other categorical features (issue_month, initial_listing_status, disbursement_method) → retained for encoding

# 8. Transformations & Engineering
Log transforms: annual_income, debt_to_income, total_debit_limit, num_active_debit_accounts

Squared transform: months_since_last_delinq

Binary flags: is_renter, never_late_payment, has_bankruptcy

Risk categories: delinq_risk_category

Collapsed categories: state_grouped, loan_purpose_grouped

# 9. Check Multicollimnearity
for raw_features 
- installment and loan amount heavily correlated with each other, dropped installments column
- vif ranges between 1 and 3 for all numerical columns. 
- condition number is too high because we have not scalled the data yet. 
- consition number after scalling --> 2.71

for transformed features
- corr() is less than 0.80 for all the pairs
- VIF is less than 2. Looks good
- high condition number without scalling 
- condition number after scalling 2.47, Looks good.

Conclusion: tranformed_features have smaller condition number and VIF after scalling as compared to raw_features

# 10. Create pipeline for one hot encoding and standard scalling
- Use transformed_data (which includes log and square transformed columns)

- When applied Linear Regression using the pipeline,
R2 score = 0.21
MSE = 19.97

- We will try regularisation to check if it improved the scores
Ridge -- not much difference in scores
Lasso -- not much difference

# 11. Conclusion
R2 score remains at 0.21 and MSE at 19.97 even after applying regularisation. 
Our project needs more advanced models to improve prediction scores. 








