import requests
import streamlit as st

NOTION_API_KEY = st.secrets["notion"]["api_key"]
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def query_notion(db_id, filter=None, page_size=100):
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    payload = {}
    if filter:
        payload["filter"] = filter
    if page_size:
        payload["page_size"] = page_size
    res = requests.post(url, headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json().get("results", [])

def create_notion_page(db_id, properties):
    url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": db_id}, "properties": properties}
    res = requests.post(url, headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json()

def retrieve_database_all(db_id):
    # simple wrapper to get first page; for large DBs you'd need to handle pagination
    return query_notion(db_id)
