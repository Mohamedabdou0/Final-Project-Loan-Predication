# Importing needed libraries
import streamlit as st

# Page content
st.title('About Loan eligibility Prediction Project')
st.write('This app can predict Used Loan eligibility throughout 12 features affect the Loan status with accuracy about 87.83%.')
st.write('In "Prediction" page you can enter data for the Loan you want to know its eligibility.')




st.markdown("""Description
 Loan_ID : 
Loan reference number  (unique ID)
LP001002; LP001003; ...

Gender : 
Applicant gender  (Male or Female)
Male; Female

Married : 
Applicant marital status  (Married or not married)
Married; Not Married	

Dependents : 
Number of family members
0; 1; 2; 3+

Education : 
Applicant education/qualification  (graduate or not graduate)
Graduate; Under Graduate


Self_Employed : 
Applicant employment status  (yes for self-employed, no for employed/others)
Yes; No

ApplicantIncome : 
Applicant's monthly salary/income
5849; 4583; ...

CoapplicantIncome : 
Additional applicant's monthly salary/income
1508; 2358; ...

LoanAmount : 
Loan amount
128; 66; ...

Loan_Amount_Term : 
The loan's repayment period (in days)
360; 120; ...

Credit_History : 
Records of previous credit history  (0: bad credit history, 1: good credit history)
0; 1

Property_Area : 
The location of property  (Rural/Semiurban/Urban)

Loan_Status : 
Status of loan  (Y: accepted, N: not accepted)

""")