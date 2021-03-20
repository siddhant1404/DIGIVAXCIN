global flagsympt
global flagvacc

def app(): 
    import streamlit as st
    import pandas as pd
    import view
    import vaccine
    import numpy as np
    import time
    import os
    import hashlib

    #Reading database
    df = pd.read_excel('patient.xlsx')
    st.title("COVID-19 Quarantine Diary")
    
    
    #Streamlit text placeholders
    placeholder_name = st.empty()
    placeholder_age = st.empty()
    placeholder_pass = st.empty()
    name = placeholder_name.text_input('Enter your name: ')
    #age = int(round(placeholder_age.number_input('Enter your age: ')))
    passw = placeholder_pass.text_input("Enter password: " , type = "password")
    result = hashlib.sha256(passw.encode())
    

    index_pass = list(np.where(df['name'] == name)[0])
    
    
    flagsympt = 0
    flagvacc = 0
    index = list(np.where(df['name'] == name)[0])
    
    #if name not in dataset
    if name != '':
        if len(index_pass) == 0:
            view.new_app(name, result.hexdigest())
            
    #if name found but password not found
    if name in df['name'].tolist():
        if result.hexdigest() not in df.loc[index_pass]['password'].tolist():
            view.new_app(name, result.hexdigest())
    
    
    #if name and password match

    if name in df['name'].tolist():
        index_p = list(np.where(df['password'] == result.hexdigest())[0])
        comm_ind = 0
        for i in index:
            if i in index_p:
                comm_ind = i
        
        if st.sidebar.checkbox("Symptom Tracker"):
            flagsympt = 1
        if st.sidebar.checkbox("Vaccine Tracker"):
            flagvacc = 1
            
            
        if flagsympt == 1:
            view.view_app(name, df.iloc[comm_ind]['password'], comm_ind)
        if flagvacc == 1:
            vaccine.view_app(name, df.iloc[comm_ind]['password'], comm_ind)
app()