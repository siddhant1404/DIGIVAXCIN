def app():
    import streamlit as st
    import pandas as pd
    import view
    import numpy as np
    # Reading database
    df = pd.read_excel('patient.xlsx')
    st.title("COVID-19 Quarantine Diary")

    # Streamlit text placeholders
    placeholder_name = st.empty()
    placeholder_age = st.empty()
    name = placeholder_name.text_input('Enter your name: ')
    age = int(round(placeholder_age.number_input('Enter your age: ')))

    index = list(np.where(df['name'] == name)[0])

    # if name not in dataset (new name)
    if name != '':
        if len(index) == 0:
            view.new_app(name, age)
    # if name matches but age doesn't
    if name in df['name'].tolist():
        if age not in df.loc[index]['age'].tolist():
            view.new_app(name, age)

    # if name and age match

    if name in df['name'].tolist():
        index_age = list(np.where(df['age'] == age)[0])
        comm_ind = 0
        for i in index:
            if i in index_age:
                comm_ind = i
        view.view_app(name, df.iloc[comm_ind]['age'], comm_ind)


app()