import bcrypt
import jwt
from datetime import datetime, timedelta
import os
from sqlalchemy import text    
from sqlalchemy import DateTime
from sqlalchemy.orm import Session


# Definir chave secreta para JWT
JWT_SECRET = os.getenv("JWT_SECRET", "mysecretkey")
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # Token expira em 1 hora

# Função para criar hash da senha
def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Função para verificar a senha
def verify_senha(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Função para criar JWT token
def criar_jwt_token(exp_datetime: DateTime, email: str, db: Session, algorithm: str) -> str:
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    query = text(
            "INSERT INTO security (secret, algorithm, exp_datetime) VALUES (:secret, :algorithm, :exp_datetime)"
        )
    db.execute(query, {"secret": token, "algorithm": algorithm, "exp_datetime": exp_datetime})
    db.commit()

    return token

