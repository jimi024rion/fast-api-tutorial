from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user_name: str = "user"
password: str = "password"
host: str = "localhost"
port: int = 5432
db_name: str = "database"
# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = f"postgresql://{user_name}:{password}@{host}:{port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
