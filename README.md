# Lending Club Loan Analysis (Linear Regression)

## Project Overview
This project explores the **Lending Club loan dataset** using **Linear Regression** as the primary modeling technique.  
I completed this project immediately after learning Linear Regression, so I intentionally did **not use any other algorithms**.  
The goal was to practice:
- Building a reproducible machine learning pipeline
- Applying preprocessing (scaling, encoding, transformations)
- Running regression diagnostics (correlation, VIF, condition number)
- Interpreting coefficients for feature importance

This project serves as a **baseline exploration**. Future iterations may include more advanced algorithms (Ridge, Lasso, Random Forests, Gradient Boosting, XGBoost) once I study them in detail.

---

## About Dataset
- Source: [OpenIntro Lending Club Loans Dataset](https://www.openintro.org/data/index.php?data=loans_full_schema)  
- Raw shape: 10,000 rows × 55 columns  
- Description (from OpenIntro):  
  > This data set represents thousands of loans made through the Lending Club platform, which is a platform that allows individuals to lend to other individuals. Of course, not all loans are created equal. Someone who is essentially a sure bet to pay back a loan will have an easier time getting a loan with a low interest rate than someone who appears to be riskier. And for people who are very risky? They may not even get a loan offer, or they may not have accepted the loan offer due to a high interest rate. It is important to keep that last part in mind, since this data set only represents loans actually made, i.e. do not mistake this data for loan applications!

---

## Workflow Summary
### 1. Data Cleaning
- Dropped leakage columns (`loan_status`, `balance`, `paid_total`, etc.)
- Removed joint application features due to >85% missingness
- Imputed missing values (median for continuous, sentinel values for delinquency flags)
- Transformed `earliest_credit_line` into `years_since_first_credit`

### 2. Feature Engineering
- **Log transforms**: annual_income, debt_to_income, total_debit_limit, num_active_debit_accounts  
- **Squared transform**: months_since_last_delinq  
- **Binary flags**: is_renter, never_late_payment, has_bankruptcy  
- **Risk categories**: delinq_risk_category  
- **Collapsed categories**: state_grouped, loan_purpose_grouped  

### 3. Multicollinearity Checks
- Raw features: VIF between 1–3, condition number improved after scaling  
- Transformed features: VIF < 2, condition number ≈ 2.5 → stable  

### 4. Pipeline Construction
- Numeric features scaled with `StandardScaler`  
- Categorical features encoded with `OneHotEncoder`  
- Combined preprocessing + regression in a single `Pipeline`

### 5. Modeling
- **Linear Regression** baseline:
  - R² ≈ 0.21
  - MSE ≈ 19.97
- **Ridge & Lasso** regularization:
  - No significant improvement in scores
- Coefficient analysis highlighted key predictors:
  - Debt-to-income ratio  
  - Loan amount  
  - Verified income status  
  - Loan purpose (debt consolidation, other)  
  - Number of active debit accounts  

---

## Key Learnings
- Linear Regression provides interpretability but struggles with complex, nonlinear relationships in loan data.  
- Regularization (Ridge/Lasso) did not significantly improve performance, reinforcing the limits of linear models here.  
- Feature importance analysis highlighted meaningful drivers of interest rates, even with modest predictive power.  
- Advanced models will likely be needed to capture nonlinearities and interactions.

---

## Next Steps
- Revisit this project after learning advanced algorithms:
  - Ridge/Lasso with proper tuning
  - Tree-based models (Random Forest, Gradient Boosting, XGBoost)
  - Interaction terms and polynomial features
- Compare performance against the baseline Linear Regression to measure improvement.

---

## Repository Structure
- `notebooks/` → Jupyter notebooks for exploration and modeling  
- `src/` → Modular Python scripts for cleaning  
- `data/` → Raw and cleaned datasets, final coefficients dataset 
- `reports/` → Summary of findings, detailed workflow notes ((data cleaning, feature engineering, diagnostics, pipeline design, results)) in `notes.md`
- `README.md` → Project overview (this file)

---

## Acknowledgments
- Dataset provided by [OpenIntro](https://www.openintro.org/).  
- Project inspired by my learning journey in Linear Regression.
