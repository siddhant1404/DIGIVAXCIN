#Vaccine App
def view_app(name, age, comm_ind):
    import cv2
    import pytesseract
    import re
    import streamlit as st
    import time
    from PIL import Image
    import pandas as pd
    import numpy as np
    placeholder_map = st.empty()
    placeholder_df = st.empty()
    
    st.sidebar.write("Your name: ", name)
    st.sidebar.write("Your age: ", age)
    df = pd.read_excel('vacsymp.xlsx')
    st.header("Select today's symptoms and click submit: ")
    index = list(np.where(df['name'] == name)[0])
    placeholder_df.dataframe(df.iloc[comm_ind])
    days = ["Select a day","Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
    
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
                df.to_excel('vacsymp.xlsx', index=False)

            if st.button("Calculate Day-Wise Scores"):
                WEIGHTS=[]
                for x in range(3,8):
                    for y in range(1, len(df)):
                        l=[]
                        n=0
                        count=1
                        weight={}
                        for z in range (len(df.iloc[y,x])):
                                if(df.iloc[y,x][z]=="'" and count%2!=0):
                                    count=count+1
                                    n=z
                                elif(df.iloc[y,x][z]=="'" and count%2==0):
                                    l.append(''.join(df.iloc[y,x][n:z]))
                                    count=count+1
                        
                        for z in l:
                            weight[z]=(weight.get(z,0)+1)/len(df)
                    WEIGHTS.append(weight)
                    
                user = []
                y = index[0]
                for x in range(3, 8):
                    l = []
                    n = 0
                    count = 1
                    for z in range(len(df.iloc[y, x])):
                        if(df.iloc[y,x][z]=="'" and count%2!=0):
                            count=count+1
                            n=z
                        elif(df.iloc[y,x][z]=="'" and count%2==0):
                            l.append(''.join(df.iloc[y,x][n:z]))
                            count=count+1
                    user.append(l)
                
                
                SCORE=[]
                for x in range(5):
                    score=0
                    for y in user[x]:
                        for key,value in WEIGHTS[x].items():
                            if (y==key):
                                score=score+value
                    SCORE.append(score)
                df_score = pd.read_excel("vacscore.xlsx")
                
                for i in range(3,8):
                    df_score.at[index, df_score.columns[i]] = SCORE[i-3]
                df_score.to_excel("vacscore.xlsx", index=False)
            
                df_score = pd.read_excel("vacscore.xlsx")
                ave = df_score.mean(axis = 0)[1:14]
                print(ave)
                deviation = df_score.std(axis = 0)[1:14]
                print(deviation)

                high = ave + deviation
                days = ["1", "2", "3", "4", "5"]
                scores = df_score.iloc[index[0], 3:8]
                for i in scores:
                    print(i)
                import matplotlib.pyplot as plt
                plt.bar(days, ave, color = ['green'])
                plt.bar(days, high, color = ['red'], alpha = 0.3)

                plt.xlabel("Days")
                plt.ylabel("Risk Factor")
                plt.plot(days, scores, color = 'red')
                plt.legend(['Patient Risk Factor','Medium risk factor', 'High risk factor'])
                st.table(df_score.iloc[index, :8])
                st.table(df_score.iloc[index, 8:])
                st.pyplot(plt)
                st.write("Medium risk factor: Average risk factor of all Patients")
                st.write("High risk factor: Average + Standard Deviation")
    
    placeholder_df.write(df.iloc[comm_ind])
    
    #Certificate Image Processing
    vac_img = st.file_uploader("Please upload a screenshot of your vaccine certificate")
    if vac_img is not None:
        image = Image.open(vac_img)
        st.image(image, caption='Your Certificate')
        img = np.array(image) 
        
        
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
        # cv2.imshow("Thresh1",thresh1)
        # cv2.waitKey(100000)
        custom_config = r'--oem 3 --psm 4'
        text=pytesseract.image_to_string(img, config=custom_config,lang='eng').split()
        info={}
        y=0
        for  x in range(len(text)):
            if(text[x]=="/" and text[x-2]=="Vaccine"):
                y=x+4
                info["Name"]=""
                while(text[y]!="COVISHIELD" and text[y]!="COVAXIN"):
        
                    info["Name"]=info["Name"]+" "+ text[y]
                    y = y + 1
                info["Name"]=info["Name"].strip()
            elif(text[x]=="(1st"):
                info["Dose"]="1st"
            elif(text[x]=="COVISHIELD" or text[x]=="COVAXIN"):
                info["Vaccine"]=text[x]
            elif(text[x]=="/" and text[x-1]=="Dose"):
                info["Age"]=text[x+4]
                info["Date"]=text[x+5]+ " " + text[x+6]+" "+ text[x+7]
            elif(text[x]=="/" and text[x-1]=="by"):
                info["by"]=text[x+7]+text[x+8]
                info["Gender"]=text[x+6]
            elif(text[x]=="/" and text[x-2]=="Vaccination" ):
                info["verification"]=" ".join(text[x+4:x+8])
            elif(text[x]=="ID"):
                info["BenificiaryID"]=text[x+1]
            elif(text[x]=="Residing"):
                info["City"]=text[x+4]
            
        
        
        st.write(text)
        st.write(info)
        
        
        
        
        
        
        
    #2nd Dose vaccination progress bar
    if(st.button("Progress Bar")):
        st.write("Hello")
        my_bar = st.progress(0)
        for percent_complete in range(1, 6):
            time.sleep(60)
            my_bar.progress(percent_complete * 20)
        st.success("Vaccine Dose 2 due")
        st.balloons()
        
        