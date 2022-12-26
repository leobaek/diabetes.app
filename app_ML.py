import streamlit as st
import numpy as np
import joblib


def run_ml_app() : 
    st.subheader('당뇨병 발병 예측')
    # 성별은 여자이고, 나이는 50이며, 연봉은 4만달러, 카드빛 5만달러, 자산은 20만달러 이 사람은 얼마짜리 차를 구매할까?
    
    # 성별, 나이, 연봉, 카드빛, 자산을 유저한테 모두 입력받아서
    # 자동차 구매 금액 예측하세요.

    gender = st.radio('성별 선택' ,['여자', '남자'])
    if gender == '여자' :
        gender = 0
    else :
        gender = 1

    age = st.number_input('연령 입력' , 18,100)

    HighChol = st.number_input('고 콜레스테롤 입력', 10000,1000000)

    BMI = st.number_input('체질량 지수 입력', 0 ,1000000)    

    Smoker = st.number_input('흡연 여부 입력' , 20000,10000000)

    HeartDiseaseorAttack = st.number_input('심장병 여부 입력' , 20000,10000000)

    PhysActivity = st.number_input('신체활동 여부 입력' , 20000,10000000)

    Fruits = st.number_input('과일 섭취 여부 입력' , 20000,10000000)

    Veggies = st.number_input('채소 섭취 여부 입력' , 20000,10000000)

    HvyAlcoholConsump= st.number_input('음주 여부 입력' , 20000,10000000) 

    GenHlth = st.number_input('평소 건강상태 입력' , 20000,10000000)

    MentHlth = st.number_input('정신 건강 척도 입력' , 20000,10000000)

    HighBP = st.number_input('뇌졸중 여부 입력' , 20000,10000000)




    new_data = np.array([gender,age,HighChol,BMI,Smoker,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,GenHlth,MentHlth,HighBP])
    
    new_data=new_data.reshape(1,13)

    classifier = joblib.load('classifier.pkl')    
    
    y_pred = classifier.predict(new_data)

    y_pred = round(y_pred[0],1)