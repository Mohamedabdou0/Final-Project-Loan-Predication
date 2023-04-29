# importing neede libraries
import streamlit as st
import pandas as pd

# Title
st.markdown(" <center>  <h1> Loan eligibility Dataset </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

# Link of Data
st.markdown('<a href="https://www.kaggle.com/datasets/ninzaami/loan-predication"> <center> Link to Dataset  </center> </a> ', unsafe_allow_html=True)

# Load data
df = pd.read_csv('D:\AI\Data science\8-Final Project\Final Project\Sources\Loan_data_train.csv')

# Show data
st.write('Data collected from Kaggle website . This data contains 614 rows contains information about customers')
st.write(df)
st.write(df.shape)