import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time


def bmi_range(bmi):
    if bmi >= 23:
        st.warning('당신은 과체중입니다!', icon="⚠️")
    elif bmi <= 18.5:
        st.warning('당신은 저체중입니다!', icon="⚠️")
    else:
        st.success('당신은 정상입니다!', icon="✅")



selected = st.sidebar.selectbox("목차",("BMI Caculator","Gap minder","국가별 통계"))


#bmi 

if selected == "BMI Caculator":


    st.title("체질량 지수 계산기")

    st.info("체질량 지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.")


    height = st.number_input(" 신장 (cm)",value = 160, step = 5)
    st.write("당신의 신장은  ", height, "cm" )

    weight = st.number_input(" 몸무게 (cm)",value = 50, step = 5)
    st.write(f"당신의 몸무게는  {weight} cm ")

    if st.button("계산", type="primary"):
        bmi = weight / ((height/100)**2)
        st.write(f"당신의 체질량 지수는 {bmi:.2f} 입니다")
        bmi_range(bmi)
        st.balloons()
        
            

        st.image('Rabbit.png', caption='Resnet50 Result')

if selected == "Gap minder":
    st.title("Gap minder")

    st.write("파일 불러오기")

    data = pd.read_csv('gapminder.csv')
    
    year = st.slider("Select Year",1952,2007,1952,step = 5)

    data = data[data['year']==year]
    st.write(data)


    colors = []
    
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('yellowgreen')
        elif x == 'Japan':
            colors.append('orange')
        else:
            colors.append('pink')
            
    data['colors'] = colors

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'], s =data['pop']*0.00002, color = data['colors'] )

    st.pyplot(fig)
    
   
    




if selected == "국가별 통계":
    st.title("국가별 통계")

