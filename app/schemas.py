from pydantic import BaseModel, Field

# Modelo Pydantic para registro de usuário
class UserRegister(BaseModel):
    email: str = Field(title="Email", description="Email do usuário", example="cloud@insper.edu.br")
    nome: str = Field(title="Nome", description="Nome do usuário", example="Cloud")
    senha: str = Field(title="Senha", description="Senha do usuário", example="**********")

# Modelo Pydantic para login de usuário
class UserLogin(BaseModel):
    email: str
    senha: str
