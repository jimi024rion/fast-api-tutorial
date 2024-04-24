# fastapiとsqlalchemyとpydanticとpostgres

[fastapiのチュートリアル](https://fastapi.tiangolo.com/ja/tutorial/sql-databases/)に沿って試してみたときの

## ローカルサーバを起動したいとき

```bash
uvicorn sql_app.main:app --reload
```

## postgresのDBに接続したいとき

```bash
psql -h localhost -p 5432 -U user -d database
```

## テーブルを作成/削除したいとき (alembic)

1. `sql_app/models.py`にモデルを定義/変更
2. マイグレーション情報を生成
    ```bash
    alembic revision --autogenerate -m "コメント"
    ```
    `migration/versions/`直下にスクリプトが生成される。
3. テーブル作成
    ```bash
    alembic upgrade head  # 最新のリビジョンで作成
    ```
4. テーブル削除
    ```bash
    alembic downgrade base
    ```
## (おまけ)API確認をしたいとき
一番楽なのは
1.  http://127.0.0.1:8000/docs をブラウザで開く
2.  Swagger UIが開く
3.  確認をしたいエンドポイントの`Try it out`からテスト実行する
