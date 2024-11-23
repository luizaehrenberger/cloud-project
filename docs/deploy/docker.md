# DOCKER 

## Docker
O projeto usa o Docker para rodara aplicação em container e tem uma imagem disponível em `https://hub.docker.com/repository/docker/luizaehrenberger/cloud-project/general`.

### **Detalhes**
1. Arquivo `Dockerfile` para configurar o ambiente, definir a imagem e instalar as bibliotecas necessárias especificadas no `requirements.txt`.
Para mais detalhes sobre o arquivo, nele todos oos comandos estão comentados.

2. Arquivo `compose.yaml` usado para orquestrar múltiplos serviços em contêineres, como a aplicação e o banco de dados, facilitando a configuração e execução de ambientes complexos. 

3. Rodando o Ambiente com  `docker compose up -d` o Docker Compose constrói a immagem da aplicação app usando o Dockerfile, inicia os containers e os conecta.

### **Imagem no Docker Hub**
A imagem da aplicação foi publicada no Docker Hub para facilitar o uso.

### **Passo a para criar uma imagem**
1. Login no Docker Hub: `docker login`.
2. Docker build: `docker build -t`
3. Criar a imagem: `docker tag cloud-project-app luizaehrenberger/cloud-project-app`
4. Publicar a imagem: `docker push luizaehrenberger/cloud-project-app`S