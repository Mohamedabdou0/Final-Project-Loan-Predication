# Importing libraries
import streamlit as st
import pandas as pd
import pickle as pickle




# reading data
df = pd.read_csv('D:\AI\Data science\8-Final Project\Final Project\Sources\Loan_data_train.csv')

# titles
st.markdown(" <center>  <h1> Prediction Page </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
st.markdown(" <center>  <h2> Enter Your Data </h2> </font> </center> </h2> ",
            unsafe_allow_html=True)

# storing data to use in selectboxes & radio choices
genders = tuple(df.Gender.unique())
Gender = st.radio('Select Type ', genders, horizontal= True)

Marrieds = tuple(df.Married.unique())
Married = st.radio('Select Marital Status', Marrieds, horizontal= True)

dependents = tuple(df.Dependents.unique())
st.write("Number of family members")
Dependents = st.selectbox('Select Dependents', dependents)


educations = tuple(df.Education.unique())
Education = st.radio('Select Education', educations, horizontal= True)

self_employed_ = tuple(df.Self_Employed.unique())
st.write("Applicant employment status  (yes for self-employed, no for employed/others)")
Self_Employed = st.selectbox('Select Applicant employment status', self_employed_)

ApplicantIncome = st.number_input("Applicant's monthly salary/income")
st.write(ApplicantIncome)

CoapplicantIncome = st.number_input("Additional applicant's monthly salary/income")
st.write(CoapplicantIncome)


LoanAmount = st.number_input("Loan Amount")
st.write(LoanAmount)

loan_amount_term = tuple(df.Loan_Amount_Term.unique())
Loan_Amount_Term = st.selectbox('Select The loans repayment period (in days)', loan_amount_term)



credit_history = tuple(df.Credit_History.unique())
st.write("Records of previous credit history  (0: bad credit history, 1: good credit history)")
credit_history = st.radio('Select credit history ', credit_history, horizontal= True)

property_area = tuple(df.Property_Area.unique())
st.write("The location of property  (Rural/Semiurban/Urban)")
Property_Area = st.selectbox('Select Property Area ', property_area)

# create dataframe for entries

pred_sample = {'gender': Gender,
               'married': Married, 
               'dependents': Dependents, 
               'education': Education, 
               'self_employed': Self_Employed,
                'applicantincome': ApplicantIncome, 
                'coapplicantincome': CoapplicantIncome, 
                'loanamount': LoanAmount, 
                'loan_amount_term': Loan_Amount_Term,
                'credit_history': credit_history
               ,'property_area':Property_Area
                } 
pred_sample_df = pd.DataFrame(pred_sample, index= [0])

# providing cat_cols & num_cols to be able to use transformer
cat_cols = ['gender', 'married', 'dependents', 'education', 'self_employed', 'property_area', 'loan_amount_term']
num_cols = ['applicantincome', 'coapplicantincome', 'loanamount']

# # loading transformer & model
# t = pickle.load(open('transf.pkl', 'rb'))
# m = pickle.load(open('RF.pkl', 'rb'))

# # # show the prediction when pressing the button
# if st.button('Predict'):
    # res_smpl = t.transform(pred_sample_df[cat_cols+num_cols])
    # prediction = m.predict(res_smpl)[0]
    # pred_shape = str(f'{prediction:,.0f}')
    # st.metric("loan_status", str(pred_shape)) 



