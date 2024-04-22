# fastapiとsqlalchemyとpydanticとpostgres

ローカルサーバを起動したいとき
```bash
cd src
uvicorn main:app --reload
```

postgresのDBに接続したい
```bash
psql -h localhost -p 5432 -U user -d database
```