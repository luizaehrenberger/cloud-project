from sqlalchemy import Column, Integer, String, DateTime, inspect, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime, timedelta
from sqlalchemy.sql import text

DATABASE_URL= "postgresql://projeto_user:projeto_password@db:5432/projeto"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

class Security(Base):
    __tablename__ = "security"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    secret = Column(String, unique=True)
    algorithm = Column(String)
    exp_datetime = Column(DateTime)

def init_db():
    """
    Initializes the database:
    - Creates tables if they do not exist.
    - Ensures the schema is updated if the table already exists.
    """
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    # Create missing tables
    for table in Base.metadata.sorted_tables:
        if table.name not in existing_tables:
            print(f"Creating table: {table.name}")
            table.create(bind=engine)
        else:
            print(f"Table already exists: {table.name}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def is_valid_token(token: str, db: SessionLocal) -> bool:
#     query = """
#     SELECT * FROM security
#     WHERE secret = :secret AND
#           exp_datetime > NOW()
#     """
#     db_token = db.execute(query, {"secret": token}).fetchone()
#     return bool(db_token)


# from sqlalchemy.sql import text

def is_valid_token(token: str, db: SessionLocal) -> bool:
    query = text("""
        SELECT * FROM security
        WHERE secret = :secret AND
              exp_datetime > NOW()
    """)
    try:
        db_token = db.execute(query, {"secret": token}).fetchone()
        return bool(db_token)
    except Exception as e:
        print(f"Erro na validação do token: {e}")
        return False
