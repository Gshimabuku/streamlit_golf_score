# ゴルフスコア管理（Streamlit + Notion）

## 概要
Streamlit フロントエンドと Notion DB を組み合わせたゴルフスコア管理アプリケーションの雛形です。
- ログイン / 新規登録（Notion Users DB）
- 都道府県は Relation で管理
- コース情報は Notion の Courses DB に保存
- ページ遷移は Streamlit pages を使用

## 起動方法
1. `.streamlit/secrets.toml` に Notion の API キーと各 DB ID を設定してください。
2. 必要パッケージをインストール:
   ```
   pip install -r requirements.txt
   ```
3. アプリを実行:
   ```
   streamlit run main.py
   ```

## 注意
- Notion API の利用には該当データベースを「Integration」に共有する必要があります。
- パスワードは平文で保存するサンプルです。本番ではハッシュ化してください。
