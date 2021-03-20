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