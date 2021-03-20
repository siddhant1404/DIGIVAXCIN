# <p align="center"> DIGIVAXCIN </p>
<p align="center">
<img align="center" width="800" height="600" src="https://user-images.githubusercontent.com/80914496/111869175-0d8e3f00-89a4-11eb-9dd9-f07a7d66bf6b.JPG" style="width:50%;display: block; align: center; margin-left: auto;margin-right: auto;">
</p>
### <p align="center"> _Digivaxin:_ Digital Vaccination Foot Print & COVID Risk Analyser & Tracker </p>

<br/> **1)	PROBLEM STATEMENT:** 
- COVID-19 has been gripping the World since the end of 2019, resulting in the loss of many lives. Now, with the introduction of new vaccines, uncertainty has increased with respect to whether a person in our vicinity is vaccinated or not, whether they are infected, etc. Moreover, infected people lack a customized means to keep a track of their symptoms on a day to day basis, and information on whether their health is improving or not.
-	India is a data deficient country especially when it comes to publicly available data which further incapacitates us in deriving a statistical analysis
- The symptoms of the people affected by COVID-19 often create a state of panic due to their incompetence in keeping track of their symptoms.
- Customer apprehension with respect to health security is preventing them from accessing public services like restaurants, trains etc which is further hindering our economic growth alongside creating an overall sense of paranoia
- Contemporarily everything comes at the cost of one’s privacy. Several platforms divulge private information in open market, which raises genuine concerns from the consumer end regarding lack of privacy
- Non-vaccinated individuals lack concrete knowledge on the effectiveness of GOI initiated vaccine drive, furthermore rumoured news on vaccine symptomatology is creating a sense of apprehension amongst the individuals in getting vaccinated
- The overall efficiency in the Business workflow has severely debilitated owing to uncertainty amid the COVID-19 pandemic. One of the most prominent outcome being downsizing which has left many penniless
- In day to day life people themselves cannot identify a non-vaccinated individual on-the-go i.e lack of real time visibility of vaccinated individuals or lack thereof in the vicinity of an individual which creates a barrier in interaction
- Our country lacks total transparency when it comes to the after-effects of different vaccines i.e COVAXIN & COVISHIELD in the healthcare.


<br/> **2) OUR APPROACH:** 
To provide a platform for one’s COVID risk assessment by improving preliminary diagnostics, tracking the infected areas and the same time real time tracking of vaccinated individuals in one’s vicinity. We further hope to motivate the users to get vaccinated and alleviate their concerns through people sharing their experiences on our platform and thus removing concerns about vaccination in the public.

<br/> **3) FLOW OF SOLUTION:**
- With the help of our user-friendly web-app, Digivaxci, which aims at improving the preliminary diagnostics, one can keep a track of their COVID-19 symptomatology with ease and can check how well they are recovering as compared to average trends of recovery.
- Our app takes day-wise record of the patient’s symptoms and calculates risk factor which is then used to determine if the patient should consider going for a test. This would be judged based on the severity of the patient’s symptoms. It is further used to match with our database using a matching algorithm developed by us. The data collected by the new patient would also be added to our ML model for updation.
-	Customized scheduled reminder for second vaccine dose
- Non-vaccinated users can analyse COVID-19 vaccine response from our users which will motivate them for the same.
- Our cumulative data will act as a beneficiary for multiple businesses helping them in smooth transition towards a post-COVID phase. 
-	Authenticates the claims of vaccinated users using image processing on the Vaccine Certificates uploaded by them
-	It also conducts analysis on accumulated data to generate trends related to demographics, side-effects etc.
-	Can be used as a portable proof of vaccination
-	Creates a sense of security and assurance amongst users by giving them real-time data of the vaccinated individuals in their vicinity.
-	Using the data provided by the vaccinated individual we can create a comparative report of different vaccines (COVAXIN & COVISHIELD)
-	Adverse COVID-19 & Vaccine symptomalogy can be reported or such data can be compiled for healthcare.

<br/> **5) TECHNOLOGY STACK:**
-	Streamlit web app -front end
-	Machine learning using python, sklearn
- Deployment- heroku

<br/> **6) Analysis of differences between our solution and the currently available technology.**
- The two apps that we found closest to our proposed solution are Aarogya Setu and CoWin, both launched by the Indian government. The comparison of our solution with those apps has been shown in the following slide.
 
<br/> ![table](https://user-images.githubusercontent.com/81008815/111868787-f0f10780-89a1-11eb-8835-653597f4adfa.JPG)
