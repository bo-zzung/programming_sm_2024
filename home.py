import streamlit as st
st.write('# Hi ! Welcome to My App!')

# 버튼
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# select box
option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '말','토끼','코끼리'))

st.write(f'내가 좋아하는 동물은 {option} 입니다.')

# text-area
txt = st.text_area('자신을 소개해보세요', '''

    ''')
st.write('입력한 내용은: ', txt)


st.write(f"You wrote {len(txt)} characters.")

age = st.slider('나이를 선택하세요', 0, 130, 25)
st.write("저의 나이는", age, '입니다.')

