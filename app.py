import streamlit as st
st.title("스트림잇 서비스를 통하여 배포")
# 버튼 클릭후에도 값을 유지
if "n1" not in st.session_state:
    st.session_state.n1 = 1
if "n2" not in st.session_state:
    st.session_state.n2 = 1
if "n3" not in st.session_state:
    st.session_state.n3 = 1

ln = st.link_button("깃허브", "https://github.com")
b1 = st.button("카운터 1부터 증가")
b2 = st.button("카운터 2부터 증가")
b3 = st.button("카운터 3부터 증가")
b999 = st.button("카운터 리셋")

if b1:
    st.session_state.n1 += 1
if b2:
    st.session_state.n2 += 1
if b3:
    st.session_state.n3 += 1

if b999:
    st.session_state.n1 = 1
    st.session_state.n2 = 2
    st.session_state.n3 = 3

st.write(f'카운터1={st.session_state.n1}')
st.write(f'카운터2={st.session_state.n2}')
st.write(f'카운터3={st.session_state.n3}')
