import streamlit as st
from utils.notion_client import retrieve_database_all, query_notion

st.title("📋 スコア閲覧")

if not st.session_state.get("logged_in"):
    st.warning("ログインしてください。")
    st.stop()

scores_db = st.secrets["notion"].get("scores_db_id", None)
if not scores_db:
    st.info("スコアDBが未設定です。secrets.toml に scores_db_id を追加してください。")
    st.stop()

results = retrieve_database_all(scores_db)
if not results:
    st.info("スコアがまだ登録されていません。")
else:
    for p in results:
        props = p.get("properties", {})
        date_prop = props.get("ラウンド日", {}).get("date", {})
        date = date_prop.get("start", "不明")
        score_text = "".join([rt.get("text", {}).get("content", "") for rt in props.get("スコアJSON", {}).get("rich_text", [])])
        st.write(f"- {date}: {score_text}")
