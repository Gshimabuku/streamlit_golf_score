import streamlit as st
from utils.auth import login_user, register_user
from utils.session import init_session

st.set_page_config(page_title="ゴルフスコア管理", layout="centered")

init_session()

st.title("⛳ ゴルフスコア管理システム")

menu = st.sidebar.selectbox("メニュー", ["ログイン", "新規登録"])

if menu == "ログイン":
    st.subheader("ログイン")
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        if login_user(email, password):
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
            st.success("ログイン成功！")
            st.rerun()
        else:
            st.error("メールアドレスまたはパスワードが違います。")

elif menu == "新規登録":
    st.subheader("新規登録")
    email = st.text_input("メールアドレス")
    password = st.text_input("パスワード", type="password")

    if st.button("登録"):
        result = register_user(email, password)
        if result:
            st.success("登録完了！ログインしてください。")
        else:
            st.error("すでに登録されています。")
