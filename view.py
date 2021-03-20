#New User Registration function
def new_app(name, age):
    import streamlit as st
    import math
    import pandas as pd
    import numpy as np
    #Patient data read from local dataset
    df = pd.read_excel('patient.xlsx')

    df2 = pd.DataFrame([[df.shape[0] + 1, name, age]], columns=['ID', 'name', 'age'])
    df = df.append(df2)
    #new user registration
    if st.button("Register New User"):
        df.to_excel('patient.xlsx', index=False)
        view_app(name, age, df.shape[0]-1)

#Returning user landing page function
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
    
    #Symptom Tracking
    st.header("Select today's symptoms and click submit: ")
    index = list(np.where(df['name'] == name)[0])
    placeholder_df.write(df.iloc[comm_ind])
    days = ["Select a day","Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
    "Day 13", "Day 14"]
    option = st.sidebar.selectbox('Which day of your quarantine do you want to access',
                        days)