# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank=pd.read_csv(path) 
#print(bank.head())
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks=bank.drop(['Loan_ID'],axis=1)
#print(banks.head())
print(banks.isnull().sum())
bank_mode=banks.mode()
print(bank_mode['Gender'][0])
banks['Gender'].fillna(bank_mode['Gender'][0],inplace=True)
banks['Married'].fillna(bank_mode['Married'][0],inplace=True)
banks['Dependents'].fillna(bank_mode['Dependents'][0],inplace=True)
banks['Education'].fillna(bank_mode['Education'][0],inplace=True)
banks['Self_Employed'].fillna(bank_mode['Self_Employed'][0],inplace=True)
banks['ApplicantIncome'].fillna(bank_mode['ApplicantIncome'][0],inplace=True)
banks['CoapplicantIncome'].fillna(bank_mode['CoapplicantIncome'][0],inplace=True)
banks['LoanAmount'].fillna(bank_mode['Loan_Amount_Term'][0],inplace=True)
banks['Loan_Amount_Term'].fillna(bank_mode['Loan_Amount_Term'][0],inplace=True)
banks['Credit_History'].fillna(bank_mode['Credit_History'][0],inplace=True)
banks['Property_Area'].fillna(bank_mode['Property_Area'][0],inplace=True)
banks['Loan_Status'].fillna(bank_mode['Loan_Status'][0],inplace=True)
#print(banks)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
import numpy as np
#print(banks.head())
#print(banks.head())

#print(type(banks))

avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc = np.mean)

#print(avg_loan_amount)
#,aggfunc=np.mean
# code ends here



# --------------
# code starts here
Loan_Status=614
loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
print(loan_approved_se)
loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
print(loan_approved_nse)
percentage_se=(loan_approved_se/Loan_Status)*100
print(percentage_se)
percentage_nse=(loan_approved_nse/Loan_Status)*100
print(percentage_nse)
# code ends here


# --------------
# code starts here
#print(banks.head())
#print(banks['Loan_Amount_Term'])

loan_term=banks['Loan_Amount_Term'].apply(lambda x : int(x)/12)
#print(loan_term.head())
#loan_term.columns
big_loan_term=len(loan_term[loan_term>=25])
#big_loan_term=len(loan_term[loan_term['Loan_Amount_Term']>=25])
print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
#print(loan_groupby.groups)
mean_values=loan_groupby.mean()
print(mean_values)

# code ends here


