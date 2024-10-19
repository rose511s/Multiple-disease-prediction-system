import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#set page configurations
st.set_page_config(page_title="Health Guard", layout="wide")

#getting the working directory of the .py file
working_dir=os.path.dirname(os.path.abspath(__file__))

#loading of the saved models
diabetes_model=pickle.load(open('diabetes.pkl','rb'))
heart_model=pickle.load(open('heart.pkl','rb'))
parkinsons_model=pickle.load(open('parkinson.pkl','rb'))

#sidebar for navigation
with st.sidebar:
	selected=option_menu('Disease Prediction System',['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], menu_icon='hospital-fill', icons=['activity','heart','person'], default_index=0)

if selected=='Diabetes Prediction':
	st.title('Welcome to the Diabetes Prediction Model')
	col1,col2,col3=st.columns(3)
	
	glucose=col1.slider('Glucose Level', 0, 500, 120)
	bp=col1.slider('Blood Pressure Level',0,200,120)
	skthick=col3.slider('Skin Thickness Value', 0,100,20)
	insulin=col1.slider('Insulin Level', 0, 900,30)
	bmi=col2.slider('BMI Value', 0.0, 70.0,25.0)
	dpf=col3.slider('Diabetes Pedigree Function Value', 0.0,2.5,0.5)
	age=col1.slider('Age of the Person', 0,100,25)

	if st.button('Diabetes Test Result'):
		user_input=[glucose,bp,skthick,insulin,bmi,dpf,age]
		pred=diabetes_model.predict([user_input])[0]
		diab_diagnosis='The Person is Diabetic' if pred==1 else 'The Person is not Diabetic'
		st.success(diab_diagnosis)



if selected=='Heart Disease Prediction':
	st.title('Welcome to the Heart Disease Prediction Using ML')
	col1,col2,col3=st.columns(3)
	
	age=col1.slider('Age of the Person', 0,100, 36)
	gender=col2.radio('Gender of Person', ['Male','Female'])
	cp=col3.selectbox('Chest Pain Types',['Type1','Type2','Type3','Type4'])
	trestbps=col1.slider('Resting BloodPressure',0,200,128)
	chol=col2.slider('Serum Cholestrol in mg/dl', 50,564,258)
	fbs=col3.radio('Fasting Blood Sugar > 120', ['Yes','No'])
	restecg=col1.radio('Resting Electrocardiograph Results',['Normal','Abnormal'])
	mhra=col2.slider('Maximum Heart Rate Acheived',50,200,80)
	ang=col3.radio('Exercise Induced Angina', ['Yes','No'])
	oldpeak=col1.slider('ST depression induced by exercise',0.0,10.0,1.0)
	slope=col2.selectbox('Slope of the peak exercise ST segment', ['Upsloping','Flat','Downsloping'])
	cf=col3.slider('Major Vessels colored by flourosopy', 0,4,0)
	thal=col1.selectbox('Thalassemia',['Normal','Fixed Defect','Reversable'])
        

	#mapping for categorial data
	cp_mapping={'Type1':0,'Type2':1,'Type3':2,'Type4':3}
	slope_mapping={'Upsloping':0,'Flat':1,'Downsloping':2}	
	thal_mapping={'Normal':0,'Fixed Defect':1,'Reversable':2}

	if st.button('Heart Disease Test Result'):
		user_input=[age,1 if gender=='Male' else 0,cp_mapping[cp],trestbps,chol,1 if fbs=='Yes' else 0,1 if restecg=='Normal' else  0,mhra,1 if ang=='Yes' else 0,oldpeak,slope_mapping[slope],cf,thal_mapping[thal]]
		pred=heart_model.predict([user_input])[0]
		heart_diagnosis='The Person is Heart Patient' if pred==1 else 'The Person is not Heart Patient'
		st.success(heart_diagnosis)




if selected=='Parkinsons Prediction':
	
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5) 
    with col1:
        fo = st.text_input('MDVP',help="Fo(Hz)")
        
    with col2:
        fhi = st.text_input('MDVP',help="Fhi(Hz)")
        
    with col3:
        flo = st.text_input('MDVP',help="Flo(Hz)")
        
    with col4:
        Jitter_percent = st.text_input('MDVP',help="Jitter(%)")
        
    with col5:
        Jitter_Abs = st.text_input('MDVP',help="Jitter(Abs)'")
        
    with col1:
        RAP = st.text_input('MDVP',help="RAP")
        
    with col2:
        PPQ = st.text_input('MDVP',help="PPQ")

    with col3:
        DDP = st.text_input('Jitter',help="DDP")
        
    with col4:
        Shimmer = st.text_input('MDVP',help="Shimmer")
        
    with col5:
        Shimmer_dB = st.text_input('MDVP',help="Shimmer(dB)")
        
    with col1:
        APQ3 = st.text_input('Shimmer',help="APQ3")
        
    with col2:
        APQ5 = st.text_input('Shimmer',help="APQ5")

    with col3:
        APQ = st.text_input('MDVP',help="APQ")
        
    with col4:
        DDA = st.text_input('Shimmer',help="DDA")

    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinsons Test Result"):
        if(fo != "" and fhi != "" and flo != "" and Jitter_percent != "" and Jitter_Abs != "" and RAP != "" and PPQ!="" and DDP != "" and Shimmer != ""
            and Shimmer_dB != "" and APQ3 != "" and APQ5 != "" and APQ != "" and DDA != "" and NHR != "" and HNR != "" and RPDE != ""
            and DFA != "" and spread1 != "" and spread2 != "" and D2 != "" and PPE != ""):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,
                                                            Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
                
            if (parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        else:
            st.error("Please enter valid diagnostic details")

    
	



	