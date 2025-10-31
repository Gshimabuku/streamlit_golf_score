import streamlit as st
from utils.notion_client import retrieve_database_all, create_notion_page, query_notion

st.title("🏌️ コース登録")

if not st.session_state.get("logged_in"):
    st.warning("ログインしてください。")
    st.stop()

prefecture_db = st.secrets["notion"]["prefecture_db_id"]
course_db = st.secrets["notion"]["course_db_id"]

prefs = retrieve_database_all(prefecture_db)
if not prefs:
    st.error("都道府県DBが空です。先にNotionで都道府県を登録してください。")
    st.stop()

# Map name -> id
pref_map = {}
for p in prefs:
    props = p.get("properties", {})
    title = props.get("都道府県名", {}).get("title", [])
    name = title[0].get("text", {}).get("content", "") if title else ""
    pref_map[name] = p["id"]

course_name = st.text_input("コース名")
pref_name = st.selectbox("都道府県", list(pref_map.keys()))
address = st.text_input("住所")
course_type = st.selectbox("コースタイプ", ["ロング", "ミドル", "ショート"])
total_par = st.number_input("パー数", min_value=9, max_value=72, step=1, value=72)

if st.button("登録"):
    if not course_name:
        st.error("コース名を入力してください。")
    else:
        data = {
            "コース名": {"title": [{"text": {"content": course_name}}]},
            "都道府県": {"relation": [{"id": pref_map[pref_name]}]},
            "住所": {"rich_text": [{"text": {"content": address}}]},
            "コースタイプ": {"select": {"name": course_type}},
            "パー数": {"number": total_par}
        }
        create_notion_page(course_db, data)
        st.success("コース登録完了！")
