import streamlit as st

def bmi_range(bmi):
    if bmi >= 23:
        st.warning('당신은 과체중입니다!', icon="⚠️")
    elif bmi <= 18.5:
        st.warning('당신은 저체중입니다!', icon="⚠️")
    else:
        st.success('당신은 정상입니다!', icon="✅")