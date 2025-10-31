        import streamlit as st
        from utils.notion_client import retrieve_database_all, create_notion_page, query_notion

        st.title("📝 スコア登録")

        if not st.session_state.get("logged_in"):
            st.warning("ログインしてください。")
            st.stop()

        # Placeholder implementation: a minimal score page that stores scores to a 'scores' Notion DB if configured.
        scores_db = st.secrets["notion"].get("scores_db_id", None)
        if not scores_db:
            st.info("スコア保存用のNotion DB ID (scores_db_id) が .streamlit/secrets.toml に設定されていません。
ローカルで動かす場合は secrets.toml を更新してください。")
            st.stop()

        course_db = st.secrets["notion"]["course_db_id"]
        courses = retrieve_database_all(course_db)
        course_map = {}
        for c in courses:
            props = c.get("properties", {})
            title = props.get("コース名", {}).get("title", [])
            name = title[0].get("text", {}).get("content", "") if title else ""
            course_map[name] = c["id"]

        selected_course = st.selectbox("コースを選択", list(course_map.keys()))
        date = st.date_input("ラウンド日")
        holes = st.number_input("ホール数", min_value=9, max_value=18, value=18, step=9)

        scores = []
        for i in range(1, holes+1):
            val = st.number_input(f"Hole {i} スコア", min_value=1, max_value=20, key=f"score_{i}")
            scores.append(val)

        if st.button("スコアを保存"):
            # create a simple page in scores DB with JSON of scores
            data = {
                "ユーザー": {"relation": [{"id": st.session_state.get('user_email')}]},
                "コース": {"relation": [{"id": course_map[selected_course]}]},
                "ラウンド日": {"date": {"start": date.isoformat()}},
                "スコアJSON": {"rich_text": [{"text": {"content": str(scores)}}]}
            }
            create_notion_page(scores_db, data)
            st.success("スコアを保存しました。")
