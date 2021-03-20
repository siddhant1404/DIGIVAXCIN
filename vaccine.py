#Vaccine App
def view_app(name, age, comm_ind):
    import streamlit as st
    from PIL import Image
    vac_img = st.file_uploader("Please upload a screenshot of your vaccine certificate")
    if vac_img is not None:
        image = Image.open(vac_img)
        st.image(image, caption='Your Certificate')
    