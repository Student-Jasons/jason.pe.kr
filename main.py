import streamlit as st
from PIL import Image # 위에서 선언 후 사용해야한다.

option = st.sidebar.selectbox(
    '페이지 선택',
     ('매인 홈페이지', '황준섭의 업적(?)', '기능 추가중'))
if option == "매인 홈페이지":
    st.title("WELCOME 황준섭's site!")
    img = Image.open('image/face.png')
    empty1, image, empty2 = st.columns(3)
    empty1, texts, empty2 = st.columns(3)
    image.write(img)
    texts.write("""
    * 황준섭
    * 2011년 8월 26일생
    * 정평중학교 11132학번
    * 코딩 좋아하고 똘기가 있는(?) 학생
    """)


if option == "황준섭의 업적(?)":
    st.title("아저씨 여기 막 들어오시면 안되요~")
if option == "기능 추가중":
    st.title("아저씨 여기 막 들어오시면 안되요~")
