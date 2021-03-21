#Vaccine App
def view_app(name, res, comm_ind):
    import cv2
    import pytesseract
    import re
    import streamlit as st
    import time
    from PIL import Image
    import pandas as pd
    import numpy as np
    import datetime 
    placeholder_map = st.empty()
    placeholder_df = st.empty()
    
    st.sidebar.write("Your name: ", name)
    
    df = pd.read_excel('vacsymp.xlsx')
    index = list(np.where(df['name'] == name)[0])
    age_pre = df.loc[index, 'age']
    age_pre = age_pre.tolist()
    age = int(round(st.number_input('Enter your age: ', age_pre[0])))
    
    st.header("Select today's symptoms and click submit: ")
    df.at[index, 'age'] = age
    
    st.sidebar.write("Your age: ", age)
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
    
    placeholder_df.write(df.iloc[comm_ind, 3:])
        #Health condition listing for patients
    issues = st.subheader("Enter your health conditions: ")
    col11, col22 = st.beta_columns(2)
    with col11:
        issue1 = st.checkbox("Heart failure with hospital admission in past one year")
        issue2 = st.checkbox("Post Cardiac Transplant/Left Ventricular Assist Device (LVAD)")
        issue3 = st.checkbox("Significant left ventricular systolic dysfunction (LVEF<40%)")
        issue4 = st.checkbox("Moderate or severe valvular heart disease")
        issue5 = st.checkbox("Congenital heart disease with severe PAH or Idiopathic PAH")
    with col22:
        issue6 = st.checkbox("Coronary Artery Disease with past CABG/PTCA/MI AND Hypertension/Diabetes on treatment")
        issue7 = st.checkbox("Angina AND Hypertension/Diabetes on treatment")
        issue8 = st.checkbox("CT/MRI documented stroke AND Hypertension/Diabetes on treatment")
        issue9 = st.checkbox("Pulmonary artery hypertension AND Hypertension/Diabetes on treatment")
        issue10 = st.checkbox("Diabetes (>10 years OR with complications) AND Hypertension on treatment")
    
    iss_list = []
    df_issues = pd.read_excel("hissues.xlsx")
    if issue1 == True:
        iss_list.append("Heart failure with hospital admission in past one year")
    if issue2 == True:
        iss_list.append("Post Cardiac Transplant/Left Ventricular Assist Device (LVAD)")
    if issue3 == True:
        iss_list.append("Significant left ventricular systolic dysfunction (LVEF<40%)")
    if issue4 == True:
        iss_list.append("Moderate or severe valvular heart disease")
    if issue5 == True:
        iss_list.append("Congenital heart disease with severe PAH or Idiopathic PAH")
    if issue6 == True:
        iss_list.append("Coronary Artery Disease with past CABG/PTCA/MI AND Hypertension/Diabetes on treatment")
    if issue7 == True:
        iss_list.append("Angina AND Hypertension/Diabetes on treatment")
    if issue8 == True:
        iss_list.append("CT/MRI documented stroke AND Hypertension/Diabetes on treatment")
    if issue9 == True:
        iss_list.append("Pulmonary artery hypertension AND Hypertension/Diabetes on treatment")
    if issue10 == True:
        iss_list.append("Diabetes (>10 years OR with complications) AND Hypertension on treatment")
    st.subheader("Your selected health issues: ")
    for i in iss_list:
        st.write(i)
        
        
        
        
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
            elif(text[x]=='#'  ):
                info["verification"]=text[x-2] + " "+ text[x-1]+ " " + text[x+1]
            elif(text[x]=="Residing"):
                info["City"]=text[x+4]
        st.write(info)
        
        
        if info["Name"] == name:
            st.success("Name Verified")
            list_keys = info.keys()
            list_vals = info.values()
            
            df_cert = pd.DataFrame(columns = list_keys)
            
            df_cert = pd.read_excel("cert.xlsx")
            names = list(df_cert["Name"])
        
            index = list(np.where(df_cert['Name'] == info["Name"])[0])
                
            if info["Name"] not in names:
                df_cert.loc[len(df_cert)] = list_vals
                df_cert.to_excel("cert.xlsx", index=False)
            st.sidebar.write("Vaccine Name: ", info["Vaccine"])
            st.sidebar.write("Vaccination Name: ", info["Date"])
            vac_date = df_cert.loc[index]['Date'].tolist()[0]
            
            df_timer = pd.read_excel("Timer.xlsx")
            
        
            if info["Name"] not in list(df_timer["Name"]):
                df_timer.loc[len(df_cert)] = [name, vac_date]
                df_timer.to_excel("Timer.xlsx", index=False)
                
            date_list = vac_date.split(" ")
            datenum = date_list[0]
            year = date_list[2]
            if date_list[1]=="Jan":
                month = 1
            elif date_list[1]=="Feb":
                month = 2
            elif date_list[1]=="Mar":
                month = 3
            elif date_list[1]=="Apr":
                month = 4
            elif date_list[1]=="May":
                month = 5
            elif date_list[1]=="Jun":
                month = 6
            elif date_list[1]=="Jul":
                month = 7
            elif date_list[1]=="Aug":
                month = 8
            elif date_list[1]=="Sept":
                month = 9
            elif date_list[1]=="Oct":
                month = 10
            elif date_list[1]=="Nov":
                month = 11
            elif date_list[1]=="Dec":
                month = 12
            date_string = ''
            date_string += datenum
            date_string += "/"
            date_string += str(month)
            date_string += "/"
            date_string += year
            
            
            element = datetime.datetime.strptime(date_string,"%d/%m/%Y")
            tuple = element.timetuple() 
        
            timestamp_dose1 = time.mktime(tuple) 
            timestamp_current = time.time()
            
            
        else:
            st.error("Names do not match")
        
        
        
        
    pan_img = st.file_uploader("Please upload a screenshot of your PAN Card")
    if pan_img is not None:
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img_pan = Image.open(pan_img)
        st.image(img_pan, caption='Your PAN Card')
        np_imgpan = np.array(img_pan)
        np_imgpan = cv2.cvtColor(np_imgpan, cv2.COLOR_BGR2GRAY)
        ret,thresh1 = cv2.threshold(np_imgpan,120,255,cv2.THRESH_BINARY)
        # cv2.imshow("Thresh1",thresh1)
        # cv2.waitKey(100000)
        custom_config = r'--oem 3 --psm 4'
        text=pytesseract.image_to_string(np_imgpan, config=custom_config,lang='eng').split()
        def isValid(Z):
            Result=re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}")
            return Result.match(Z)
        cert_pan = info["verification"].split(" ")[-1]
        for x in text:
            if (isValid(x)) and x == cert_pan:
                st.success(("PAN Number Verified: ", cert_pan))
                
                

        
        
    
    option = "Issues"
    
    index = list(np.where(df['name'] == name)[0])
    df_issues.loc[index[0]-1, option] =  str(iss_list)
    df_issues.to_excel("hissue.xlsx", index=False)
            
    covaxin = ['']
    covishield = ['']
    #2nd Dose vaccination progress bar
    if(st.sidebar.button("Progress Bar")):
        st.write("Hello")
        my_bar = st.progress(0)
        for percent_complete in range(1, 6):
            time.sleep(1)
            my_bar.progress(percent_complete * 20)
        st.success("Vaccine Dose 2 due")
        st.balloons()
    if st.sidebar.button("Reset"):
        my_bar = st.progress(0)
    
        