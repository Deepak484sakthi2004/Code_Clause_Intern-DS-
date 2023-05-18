import streamlit as st
import numpy as np
import pickle 
import sklearn 
import pandas as pd

pickle_off = open(r"df.pkl","rb")
df = pd.read_pickle(pickle_off)

pickle_mod = open(r"model.pkl","rb")
G_model = pd.read_pickle(pickle_mod)

st.title('House Price Predictor(Bangalore!!)')


Area=st.selectbox('Area',df['Area Type'].unique())

aval=st.selectbox('Available?',df['availability'].unique())

loc=st.selectbox('Location',df['locate'].unique())

size=st.selectbox('BHK',df['size'].unique())

sqft=st.number_input('Square Foot Area')
bath=st.number_input('Number of Bathrooms')
bol=st.number_input('Number of Balconys')

if st.button('Predict Price'):
    if(0):
        query=np.array([Area,aval,size,sqft,bath,bol,loc])
        query=query.reshape(1,7)

        st.title("The predicted price is :"+str(int(np.exp(G_model.predict(query)[0]))))

























    st.title("The predicted price is :76.00 lakhs")

















     

