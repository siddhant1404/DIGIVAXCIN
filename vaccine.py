#Vaccine App
def view_app(name, age, comm_ind):
    import streamlit as st
    import time
    from PIL import Image
    vac_img = st.file_uploader("Please upload a screenshot of your vaccine certificate")
    if vac_img is not None:
        image = Image.open(vac_img)
        st.image(image, caption='Your Certificate')
        
    #2nd Dose vaccination progress bar
    if(st.button("Progress Bar")):
        st.write("Hello")
        my_bar = st.progress(0)
        for percent_complete in range(1, 6):
            time.sleep(60)
            my_bar.progress(percent_complete * 20)
        st.success("Vaccine Dose 2 due")
        st.balloons()