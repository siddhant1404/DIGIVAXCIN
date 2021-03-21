global flagsympt
global flagvacc

def app(): 
    import streamlit as st
    import pandas as pd
    import view
    import vaccine
    import numpy as np
    import hashlib

    #Reading database
    df = pd.read_excel('patient.xlsx')
    st.title("COVID-19 Quarantine Diary")
    
    
    #Streamlit text placeholders
    placeholder_name = st.empty()
    placeholder_pass = st.empty()
    placeholder_button = st.empty()
    name = placeholder_name.text_input('Enter your name: ')
    passw = placeholder_pass.text_input("Enter password: " , type = "password")
    result = hashlib.sha256(passw.encode())

    index_pass = list(np.where(df['name'] == name)[0])
    
    
    flagsympt = 0
    flagvacc = 0
    if name == '' or passw == '':
        st.error("Enter Valid Name/Password")
    #if name not in dataset
    if name != '' and passw != '':
        if len(index_pass) == 0:                
                x = True
                st.error("Account not found")
                view.new_app(name, result.hexdigest())
            
    #if name found but password not found
    if name in df['name'].tolist() and passw != '':
        if result.hexdigest() not in df.loc[index_pass]['password'].tolist():
            st.error("Account not found")
            view.new_app(name, result.hexdigest())
    
    
    #if name and password match

    if name in df['name'].tolist():
        index_p = list(np.where(df['password'] == result.hexdigest())[0])
        if len(index_p) != 0:
                
            placeholder_button.button = st.empty()
            comm_ind = 0
            for i in index_pass:
                if i in index_p:
                    comm_ind = i
            st.success("Logged in")
            if st.sidebar.checkbox("Symptom Tracker"):
                flagsympt = 1
            if st.sidebar.checkbox("Vaccine Tracker"):
                flagvacc = 1
                
                
            if flagsympt == 1:
                view.view_app(name, df.iloc[comm_ind]['password'], comm_ind)
            if flagvacc == 1:
                vaccine.view_app(name, df.iloc[comm_ind]['password'], comm_ind)
app()