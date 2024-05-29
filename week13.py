import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
import time


def bmi_range(bmi):
    if bmi >= 23:
        st.warning('당신은 과체중입니다!', icon="⚠️")
    elif bmi <= 18.5:
        st.warning('당신은 저체중입니다!', icon="⚠️")
    else:
        st.success('당신은 정상입니다!', icon="✅")

#bmi 

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

