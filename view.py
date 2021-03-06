def new_app(name, res):
    import streamlit as st
    import math
    import pandas as pd
    import numpy as np
    df = pd.read_excel('patient.xlsx')    

    df2 = pd.DataFrame([[df.shape[0] + 1, name, res]], columns=['ID', 'name', 'password'])
    df = df.append(df2)
    if st.button("Register New User"):
        df.to_excel('patient.xlsx', index=False)
        view_app(name, res, df.shape[0]-1)
    


def view_app(name, res, comm_ind):
    import streamlit as st
    import pandas as pd
    import numpy as np
    from geopy.geocoders import Nominatim
    placeholder_map = st.empty()
    placeholder_df = st.empty()
    
    
    
    st.sidebar.write("Your name: ", name)
    
    df = pd.read_excel('patient.xlsx')
    df_score = pd.read_excel("score.xlsx")
    
    
    index = list(np.where(df['name'] == name)[0])
    age_pre = df.loc[index, 'age']
    age_pre = age_pre.tolist()
    age = int(round(st.number_input('Enter your age: ', age_pre[0])))
    st.sidebar.write("Your age: ", age)
    gender = df_score.loc[index, 'Gender']
    gender = gender.tolist()
    if gender[0] == "M":
        placeholder_gender = st.sidebar.write("Gender: Male")
    elif gender[0] == "F":
        placeholder_gender = st.sidebar.write("Gender: Female")
        
    if age_pre[0] < 20:
        st.sidebar.write("Age Group: <20")
    if age_pre[0] >= 20 and age_pre[0] < 40:
        st.sidebar.write("Age Group: 20 to 40")
    if age_pre[0] >= 40 and age_pre[0] < 60:
        st.sidebar.write("Age Group: 40 to 60")
    if age_pre[0] >= 60:
        st.sidebar.write("Age Group: >60")
    df.at[index, 'age'] = age
    df2 = df.iloc[comm_ind, 4:]
    #st.write(df2)
    #placeholder_df.dataframe(df2)
    
    st.header("Select today's symptoms and click submit: ")
    days = ["Select a day","Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10", "Day 11", "Day 12", 
    "Day 13", "Day 14"]
    option = st.sidebar.selectbox('Which day of your quarantine do you want to access',
                        days)
    df = df.fillna("NA")
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

            if st.button("Calculate Day-Wise Scores"):
                WEIGHTS=[]
                for x in range(4,18):
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
                for x in range(4, 18):
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
                for x in range(14):
                    score=0
                    for y in user[x]:
                        for key,value in WEIGHTS[x].items():
                            if (y==key):
                                score=score+value
                    SCORE.append(score)
                    
                    
                    
                    
                df_score = pd.read_excel("score.xlsx")
                
                    
                
                age=list(df_score["age"])[1:]
                pre=list(df_score["Precondition"])[1:]
                gender=list(df_score["Gender"])[1:]
                df_score["sum"]=df_score.loc[:,["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7","Day 8","Day 9","Day 10","Day 11","Day 12","Day 13","Day 14"]].sum(axis=1)
                sum=list(df_score["sum"])[1:]
                dict_age={}
                for x in age:
                    if(x>20 and x<40):
                        dict_age["20-40"]=dict_age.get("20-40",0)+1
                    elif(x>=60 ):
                        dict_age[">60"] = dict_age.get(">60", 0) + 1
                    elif(x<60 and x>=40):
                        dict_age["40-60"] = dict_age.get("40-60", 0) + 1
                        dict_age["<20"] = dict_age.get("<20", 0) + 1
                dict_pre={}
                for x in pre:
                    if(x=="A"):
                        dict_pre[x]=dict_pre.get(x,0)+1
                    elif(x=="B"):
                        dict_pre[x]=dict_pre.get(x,0)+1
                    elif(x=="C"):
                        dict_pre[x]=dict_pre.get(x,0)+1
                dict_gender={}
                for x in gender:
                    if(x=="M"):
                        dict_gender[x]=dict_gender.get(x,0)+1
                    if(x=="F"):
                        dict_gender[x]=dict_gender.get(x,0)+1
                dict_age_s={}
                y=0
                scores=[]
                dict_gender[gender[1]]
                y=""
                for x in range(len(sum)):
                    if(age[x]>20 and age[x]<40):
                        y="20-40"
                    elif(age[x]>=60 ):
                        y=">60"
                    elif(age[x]<60 and age[x]>=40):
                        y="40-60"
                    else:
                        y="<20"
                    sum[x]=sum[x]+(dict_gender[gender[x]]/10) + (dict_age[y]/10) + (dict_pre[pre[x]]/10)
                    #sum[x] -= sum[x]*(x/14)
                maximum=max(sum)
                minimum=min(sum)
                add=[]
                for x in range(len(sum)):
                    add.append(((sum[x]-minimum)/(maximum-minimum)))
                
                for x in range(1,len(sum)+1):
                    df_score.loc[x,["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7","Day 8","Day 9","Day 10","Day 11","Day 12","Day 13","Day 14"]]=df_score.loc[x,["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7","Day 8","Day 9","Day 10","Day 11","Day 12","Day 13","Day 14"]]+add[x-1]
                                
                                
                                
                #for i in range(3,17):
                    #df_score.at[index, df_score.columns[i]] = SCORE[i-3]
                    
                    
                    
                    
                #df_score.to_excel("score.xlsx", index=False)
            
                #df_score = pd.read_excel("score.xlsx")
                ave = df_score.mean(axis = 0)[1:14]
                deviation = df_score.std(axis = 0)[1:14]

                high = ave + deviation
                days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
                    "13"]
                scores = df_score.iloc[index[0], 5:18]
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
    
    placeholder_df.write(df.iloc[comm_ind, 4:])

    st.sidebar.subheader("Location and Tracing")
    location = st.sidebar.text_area("Enter your location")
    if st.sidebar.button("Check on map"):
        '''geolocator = Nominatim(user_agent="my-app")
        location = geolocator.geocode(location)
        print(location.address)
        print((location.latitude, location.longitude))'''
        df_map = pd.read_excel("location.xlsx")
        loc_list = []
        for i in range(2):
            for j in range(1, len(df_map)):
                loc_list.append(df_map.iloc[j, i])
        loc_list.append(location)
        geolocator = Nominatim(user_agent='tracker')
        df_latlong = pd.DataFrame(columns=['lat', 'lon'])
        for location in loc_list:
            geo_loc = geolocator.geocode(location)
            if geo_loc is not None:
                df2 = pd.DataFrame([[geo_loc.latitude, geo_loc.longitude]], columns=['lat', 'lon'])
                df_latlong = df_latlong.append(df2)

        placeholder_map.map(df_latlong)
        import numpy as np
        import pandas as pd
        from sklearn.cluster import KMeans
        from sklearn.cluster import DBSCAN
        from sklearn.decomposition import PCA
        from sklearn.metrics import silhouette_score
        import seaborn as sns
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        from sklearn.cluster import DBSCAN 
        from sklearn.preprocessing import StandardScaler 
        from sklearn.preprocessing import normalize
        from sklearn.cluster import KMeans
        from sklearn.cluster import DBSCAN
        import matplotlib.pyplot as plt 

        df_latlong.rename(columns={'lat':'P1','lon':'P2'},inplace=True)
        db_default = DBSCAN(eps = 0.05, min_samples = 3).fit(df_latlong) 
        labels = db_default.labels_ 
        labels
        colours1 = {} 
        colours1[0] = 'r'
        colours1[1] = 'g'
        colours1[2] = 'b'
        colours1[3] = 'c'
        colours1[4] = 'y'
        colours1[5] = 'm'
        colours1[-1] = 'k'
        
        cvec = [colours1[label] for label in labels] 
        colors = ['r', 'g', 'b', 'c', 'y', 'm', 'k' ] 
        
        r = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[0]) 
        g = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[1]) 
        b = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[2]) 
        c = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[3]) 
        y = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[4]) 
        m = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[5]) 
        k = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[6]) 
        
        plt.figure(figsize =(9, 9)) 
        plt.scatter(df_latlong['P1'], df_latlong['P2'], c = cvec) 
        plt.legend((r, g, b, c, y, m, k), 
                ('Group 0', 'Group 1', 'Group 2', 'Group 3' ,'Group 4', 
                    'Group 5', 'Group 6'), 
                scatterpoints = 1, 
                loc ='upper left', 
                ncol = 3, 
                fontsize = 8) 
        st.pyplot(plt)


    if st.sidebar.button("Current hotspots"):
        df_map = pd.read_excel("location.xlsx")
        print(df_map)
        loc_list = []
        for i in range(2):
            for j in range(1, len(df_map)):
                loc_list.append(df_map.iloc[j, i])
        print(loc_list)
        geolocator = Nominatim(user_agent='patient')
        df_latlong = pd.DataFrame(columns=['lat', 'lon'])
        for location in loc_list:
            geo_loc = geolocator.geocode(location)
            if geo_loc is not None:
                df2 = pd.DataFrame([[geo_loc.latitude, geo_loc.longitude]], columns=['lat', 'lon'])
                df_latlong = df_latlong.append(df2)
            
        print(df_latlong)
        placeholder_map.map(df_latlong)
        import numpy as np
        import pandas as pd
        from sklearn.cluster import KMeans
        from sklearn.cluster import DBSCAN
        from sklearn.decomposition import PCA
        from sklearn.metrics import silhouette_score
        import seaborn as sns
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        from sklearn.cluster import DBSCAN 
        from sklearn.preprocessing import StandardScaler 
        from sklearn.preprocessing import normalize
        from sklearn.cluster import KMeans
        from sklearn.cluster import DBSCAN
        import matplotlib.pyplot as plt 

        df_latlong.rename(columns={'lat':'P1','lon':'P2'},inplace=True)
        db_default = DBSCAN(eps = 0.05, min_samples = 3).fit(df_latlong) 
        labels = db_default.labels_ 
        labels
        colours1 = {} 
        colours1[0] = 'r'
        colours1[1] = 'g'
        colours1[2] = 'b'
        colours1[3] = 'c'
        colours1[4] = 'y'
        colours1[5] = 'm'
        colours1[-1] = 'k'
        
        cvec = [colours1[label] for label in labels] 
        colors = ['r', 'g', 'b', 'c', 'y', 'm', 'k' ] 
        
        r = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[0]) 
        g = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[1]) 
        b = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[2]) 
        c = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[3]) 
        y = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[4]) 
        m = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[5]) 
        k = plt.scatter( 
                df_latlong['P1'], df_latlong['P2'], marker ='o', color = colors[6]) 
        
        plt.figure(figsize =(9, 9)) 
        plt.scatter(df_latlong['P1'], df_latlong['P2'], c = cvec) 
        plt.legend((r, g, b, c, y, m, k), 
                ('Group 0', 'Group 1', 'Group 2', 'Group 3' ,'Group 4', 
                    'Group 5', 'Group 6'), 
                scatterpoints = 1, 
                loc ='upper left', 
                ncol = 3, 
                fontsize = 8) 
        st.pyplot(plt)
    if st.sidebar.button("Reset Map"):
        placeholder_map = st.empty()