# Projeto Computação em Nuvem - API RESTful 

Bem-vindo à documentação oficial, o projeto consiste na construção de uma API RESTful que deve ser dockerizada e implantada na AWS utilizando o Elastic Kubernetes Service (EKS).

# Construção da API
A API desenvolvida com fastapi permite o cadastro, login e consulta de notícias obtidas através de uma API do IBGE. A aplicação gerencia usuários em um banco de dados PostgreSQL usando Postman e pgAdmin em um container Docker.

## Para executar a aplicação:

1. Baixe o arquivo compose.yaml, dentro de cloud-project.
2. Execute o Docker.
   `docker compose up -d`
3. Acesse em `http://localhost:8080`.

## Endpoints Disponíveis
Para fazer as verificação é necessário acessar o Postman e seguir os passos:
- [Registro de Usuário](endpoints/registrar.md)
- [Login de Usuário](endpoints/login.md)
- [Consulta de Dados](endpoints/consultar.md)

## Deploy
- [Docker](deploy/docker.md)
- [AWS](deploy/aws.md)