# Usar a imagem base do Python 3.9 (ou versão desejada)
FROM python:3.13-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo o código da aplicação para o contêiner
COPY . .

# Expor a porta onde o app rodará
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
