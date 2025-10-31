import streamlit as st

st.title("👤 プロフィール")

if not st.session_state.get("logged_in"):
    st.warning("ログインしてください。")
    st.stop()

st.write(f"ログイン中: {st.session_state.get('user_email')}")
st.info("プロフィール編集やパスワード変更機能は今後実装できます。")
