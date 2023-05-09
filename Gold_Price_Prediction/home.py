import streamlit as st
import numpy as np
import pickle 
import sklearn 
# import the gold price prediction model
R_model=pickle.load(open('R_model.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

#title 
st.title('Gold Price Predictor')

# getting the input year from the user
year = st.number_input("Enter the Year")

# gettin the input month from the use
month=st.number_input('Enter the Month')

if st.button('Predict Price'):
    query=np.array([year,month],int)
    query=query.reshape(1,-1)

    st.title("The predicted price is :$"+str(int(R_model.predict(query)[0])))
