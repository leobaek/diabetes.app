import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app_home import run_home_app
from app_eda import run_eda_app
from app_ML import run_ml_app
def main() :
    
    st.title('당뇨병 발병 예측 앱')

    menu = ['Home', 'EDA', 'ML']

    choice = st.sidebar.selectbox('메뉴' , menu)

    if choice == 'Home' :
        run_home_app()
    
    elif choice == 'EDA' :
        run_eda_app()

    elif choice == 'ML' :
        run_ml_app()


    








if __name__ =='__main__' :
    main()
