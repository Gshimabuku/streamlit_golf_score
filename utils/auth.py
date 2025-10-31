import streamlit as st
from utils.notion_client import query_notion, create_notion_page

USER_DB_ID = st.secrets["notion"]["user_db_id"]

def login_user(email, password):
    # Query by rich_text equals for 'メールアドレス'
    results = query_notion(USER_DB_ID, filter={
        "property": "メールアドレス",
        "rich_text": {"equals": email}
    })
    if not results:
        return False

    # Extract stored password safely
    props = results[0].get("properties", {})
    pw_prop = props.get("パスワード", {})
    pw_texts = pw_prop.get("rich_text", [])
    if not pw_texts:
        return False
    stored_pw = pw_texts[0].get("text", {}).get("content", "")
    return stored_pw == password

def register_user(email, password):
    # Check existing
    results = query_notion(USER_DB_ID, filter={
        "property": "メールアドレス",
        "rich_text": {"equals": email}
    })
    if results:
        return False

    data = {
        "メールアドレス": {"title": [{"text": {"content": email}}]},
        "パスワード": {"rich_text": [{"text": {"content": password}}]}
    }
    create_notion_page(USER_DB_ID, data)
    return True
