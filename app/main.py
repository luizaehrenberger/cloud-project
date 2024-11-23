from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import get_db, init_db, User, is_valid_token
from security import hash_senha, verify_senha, criar_jwt_token
from schemas import UserRegister, UserLogin
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import requests

app = FastAPI()
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # Token expira em 1 hora
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
IBGE_API_URL = "https://servicodados.ibge.gov.br/api/v3/noticias"


@app.on_event("startup")
def startup_event():
    init_db()


# Rota raiz para exibir uma mensagem simples
@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Autenticação"}


# Endpoint para registrar um usuário
@app.post("/registrar")
def registrar_usuario(user: UserRegister, db: Session = Depends(get_db)):
    # Hash da senha antes de salvar
    hashed_password = hash_senha(user.senha)

    # Simulação de salvar o usuário no banco de dados
    user_db = User(email=user.email, nome=user.nome, senha=hashed_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    exp_datetime = datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    # Criar o token JWT
    token = criar_jwt_token(exp_datetime, user.email, db, JWT_ALGORITHM)

    return {"jwt": token}


# Endpoint para login
@app.post("/login")
def login_usuario(user: UserLogin, db: Session = Depends(get_db)):
    # Simulação de busca no banco de dados para obter o hashed_password
    user_db = db.query(User).filter(User.email == user.email).first()
    if not user_db or not verify_senha(user.senha, user_db.senha):
        raise HTTPException(status_code=401, detail="Credenciais incorretas")

    # Gerar o token JWT
    exp_datetime = datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    token = criar_jwt_token(exp_datetime, user.email, db, JWT_ALGORITHM)

    return {"jwt": token}


# Endpoint para consultar dados da API do IBGE
@app.get("/consulta")
def consulta(
    tipo: str = Query(None, description="Tipo de conteúdo: noticia ou release"),
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Consulta a API do IBGE para buscar notícias ou releases. Autenticação necessária.
    """
    # Validação do token JWT
    if not is_valid_token(token, db):
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    # Consulta a API externa
    try:
        response = requests.get(IBGE_API_URL)
        response.raise_for_status()  # Levanta exceção se a requisição falhar
        dados = response.json()

        # Filtragem dos dados com base no tipo
        if tipo == "noticia":
            filtrado = [item for item in dados if item.get("tipo") == "noticia"]
        elif tipo == "release":
            filtrado = [item for item in dados if item.get("tipo") == "release"]
        elif tipo is None:
            filtrado = dados
        else:
            raise HTTPException(status_code=400, detail="Tipo inválido. Use 'noticia' ou 'release'.")

        return {"tipo": tipo or "todos", "resultados": filtrado}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar a API externa: {e}")



