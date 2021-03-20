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
    #Reading database
    df = pd.read_excel('patient.xlsx')
    st.title("COVID-19 Quarantine Diary")
    #html_string= "<img src=\"https://ichef.bbci.co.uk/news/1024/cpsprodpb/EAD2/production/_114241106_vaccineillus976_rtrs.jpg\" alt=\"Girl in a jacket\" style=\"width:50%;height:50%;\">"
    #st.markdown(html_string, unsafe_allow_html=True)
    #Streamlit text placeholders
    placeholder_name = st.empty()
    placeholder_age = st.empty()
    name = placeholder_name.text_input('Enter your name: ')
    age = int(round(placeholder_age.number_input('Enter your age: ')))
    flagsympt = 0
    flagvacc = 0
    index = list(np.where(df['name'] == name)[0])
    
    #if name not in dataset (new name)
    if name != '':
        if len(index) == 0:
            view.new_app(name, age)
    #if name matches but age doesn't
    if name in df['name'].tolist():
        if age not in df.loc[index]['age'].tolist():
            view.new_app(name, age)
    
    #if name and age match

    if name in df['name'].tolist():
        index_age = list(np.where(df['age'] == age)[0])
        comm_ind = 0
        for i in index:
            if i in index_age:
                comm_ind = i
        
        if st.sidebar.checkbox("Symptom Tracker"):
            flagsympt = 1
        if st.sidebar.checkbox("Vaccine Tracker"):
            flagvacc = 1
            
            
        if flagsympt == 1:
            view.view_app(name, df.iloc[comm_ind]['age'], comm_ind)
        if flagvacc == 1:
            vaccine.view_app(name, df.iloc[comm_ind]['age'], comm_ind)
        
        
    
    if(st.button("Progress Bar")):
        st.write("Hello")
        my_bar = st.progress(0)
        for percent_complete in range(1, 6):
            time.sleep(60)
            my_bar.progress(percent_complete * 20)
        st.success("Vaccine Dose 2 due")
        st.balloons()
    
    
    
    
app()