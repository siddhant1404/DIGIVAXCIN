def new_app(name, age):
    import streamlit as st
    import math
    import pandas as pd
    import numpy as np
    df = pd.read_excel('patient.xlsx')    

    df2 = pd.DataFrame([[df.shape[0] + 1, name, age]], columns=['ID', 'name', 'age'])
    df = df.append(df2)
    if st.button("Register New User"):
        df.to_excel('patient.xlsx', index=False)
        view_app(name, age, df.shape[0]-1)
    


def view_app(name, age, comm_ind):
    import streamlit as st
    import pandas as pd
    import numpy as np
    from geopy.geocoders import Nominatim
    placeholder_map = st.empty()
    placeholder_df = st.empty()
    
    st.sidebar.write("Your name: ", name)
    st.sidebar.write("Your age: ", age)
    df = pd.read_excel('patient.xlsx')
    
    st.header("Select today's symptoms and click submit: ")
    index = list(np.where(df['name'] == name)[0])
    placeholder_df.write(df.iloc[comm_ind])
    days = ["Select a day","Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
    "Day 13", "Day 14"]
    option = st.sidebar.selectbox('Which day of your quarantine do you want to access',
                        days)
    for j in days:
        if option == j:
            symp_list = []
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                fever = st.checkbox("Fever")
                fatigue = st.checkbox("Fatigue")
                dry_cough = st.checkbox("Dry Cough")
                loss_app = st.checkbox("Loss of appetite")
                body_ache = st.checkbox("Body aches")
            with col2:
                short_breath = st.checkbox("Shortness of Breath")
                nasal_cong = st.checkbox("Nasal Congestion")
                sore_throat = st.checkbox("Sore throat")
                headache = st.checkbox("Headache")
                chills = st.checkbox("Chills")
            with col3:
                loss_smell = st.checkbox("Loss of Smell")
                loss_taste = st.checkbox("Loss of taste")
                nausea = st.checkbox("Nausea")
                diarrhoea = st.checkbox("Diarrhoea")
            st.empty()

            if fever == True:
                symp_list.append("Fever")
            if fatigue == True:
                symp_list.append("Fatigue")
            if dry_cough == True:
                symp_list.append("Dry Cough")
            if loss_app == True:
                symp_list.append("Loss of appetite")
            if body_ache == True:
                symp_list.append("Body aches")
            if short_breath == True:
                symp_list.append("Shortness of Breath")
            if nasal_cong == True:
                symp_list.append("Nasal Congestion")
            if sore_throat == True:
                symp_list.append("Sore throat")
            if headache == True:
                symp_list.append("Headache")
            if chills == True:
                symp_list.append("Chills")
            if loss_smell == True:
                symp_list.append("Loss of Smell")
            if loss_taste == True:
                symp_list.append("Loss of taste")
            if nausea == True:
                symp_list.append("Nausea")
            if diarrhoea == True:
                symp_list.append("Diarrhoea")
            df.at[index, option] =  str(symp_list)
            
            if st.button("Submit"):
                df.to_excel('patient.xlsx', index=False)