import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :

    df = pd.read_csv('diabetes_data.csv')
    df.rename(columns = {'Age' : '연령'}, inplace = True)
    df.rename(columns = {'Sex' : '성별'}, inplace = True)
    df.rename(columns = {'HighChol' : '고 콜레스테롤'}, inplace = True)
    df.rename(columns = {'BMI' : '체질량 지수'}, inplace = True)
    df.rename(columns = {'Smoker' : '흡연 여부'}, inplace = True)
    df.rename(columns = {'HeartDiseaseorAttack' : '심장병 여부'}, inplace = True)
    df.rename(columns = {'PhysActivity' : '신체활동 여부'}, inplace = True)
    df.rename(columns = {'Fruits' : '과일 섭취'}, inplace = True)
    df.rename(columns = {'Veggies' : '채소 섭취'}, inplace = True)
    df.rename(columns = {'HvyAlcoholConsump' : '음주 섭취'}, inplace = True)
    df.rename(columns = {'GenHlth' : '평소 건강상태'}, inplace = True)
    df.rename(columns = {'MentHlth' : '정신 건강척도'}, inplace = True)
    df.rename(columns = {'HighBP' : '뇌졸중'}, inplace = True)
    df.rename(columns = {'Diabetes' : '당뇨병'}, inplace = True)

    
    
    st.subheader('데이터 프레임 확인')
    st.dataframe(df.head(3))
    
    st.subheader('기본 통계 데이터')
    
    st.dataframe(df.describe())

    # 컬럼을 선택할 수 있게 한다. 하나의 컬럼을 선택하면, 
    # 해당컬럼의 최댓값 최솟값 데이터를 화면에 보여준다.
    st.subheader('최대 / 최소 데이터 확인하기')
    
    column_list = df.columns[4: ]

    selected_column = st.selectbox('컬럼을 선택하세요' , column_list)
    
    df_min =df.loc[df[selected_column] ==df[selected_column].min(), ]
    df_max =df.loc[df[selected_column] ==df[selected_column].max(), ]
    
    st.text('최대값')
    st.dataframe(df_max)
    st.text('최소값')
    st.dataframe(df_min)

    # 선택한 컬럼에 대한 히스토그램
    st.subheader('컬럼 별 히스토그램')
    
    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요', column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 10, 30, value=10,step=1)
    
    fig1 = plt.figure()
    plt.hist(data=df , x= histogram_column , bins= my_bins ,rwidth=0.8)
    plt.title
    st.pyplot(fig1)



    st.subheader('상관 관계 분석')

    selected_list = st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', column_list)

    df.corr()
    df_corr = df[selected_list].corr()
    
    fig2 = plt.figure()
    sb.heatmap(data= df_corr,annot=True, fmt='.2f', cmap='coolwarm', vmin= -1, vmax= 1, linewidths=0.5)
    st.pyplot(fig2)