# Deploy no AWS

A API Restful implementada na AWS pode ser acesssada em: `http://a82c0a93257ec433189a7611363e86be-977945615.us-east-1.elb.amazonaws.com:8080/docs`

### **Passo a passo para o deploy no AWS**
1. Instalar e configurtar o  AWS CLI seguindo: `https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html` e `https://docs.aws.amazon.com/pt_br/eks/latest/userguide/install-awscli.html` <br>
2. Criar chave de acesso AWS:
- Login no AWS Management Console.
- Criar um usuário.
- Em IAM selecione um usuario
- Criar uma chave de acesso usando CLI.
- Salve as informações da chave de acesso em um lugar seguro, onde não será compartilhada e exposta a outros.
3. Para configurar o AWS CLI, no terminal, `aws configure` e fornessa as informações da chave de acesso obtida com as suas configurações de região e output.

#### ** EKSCTL **
Utilizando o EKSCTL para a gestão de cluster EKS. <br>
4. Instalação e configuração EKS: `https://docs.aws.amazon.com/eks/latest/userguide/setting-up.html`
5. Criar o cluster:
```
 eksctl create cluster ´
>>     --name cluster-lu `
>>     --region us-east-1 `
>>     --nodegroup-name "ng-default" `
>>     --node-type "t3.medium" `
>>     --nodes 2 `
>>     --nodes-min 1 `
>>     --nodes-max 3 `
>>     --managed
>> 
```
`aws eks --region us-east-1 update-kubeconfig --name cluster-lu` <br>
5. Arquivo `app-config.yaml` para o deployment. <br>
6. Arquivo `db-config.yaml` para o deployment da base de dados.<br>
7. Aplicação dos arquivos `kubectl apply -f (app/db)-config.yaml -n cloud-project`<br>
8. Para obter o link: `kubectl get svc -n cloud-project`<br>
9. Resultado: `curl http://a82c0a93257ec433189a7611363e86be-977945615.us-east-1.elb.amazonaws.com:8080`<br>


Para fazer as verificação pode ser feita no Postman, substituindo `localhost`por `a82c0a93257ec433189a7611363e86be-977945615.us-east-1.elb.amazonaws.com` ou pelo terminal:
```
curl -X POST "http://a82c0a93257ec433189a7611363e86be-977945615.us-east-1.elb.amazonaws.com:8080/registrar" -H "Content-Type: application/json" -d '{
    "nome": "Computação em Nuvem Humberto",
    "email": "nuvem@insper.edu.br",
    "senha": "nuvem0"
}'
```
```
curl -X POST "http://a82c0a93257ec433189a7611363e86be-977945615.us-east-1.elb.amazonaws.com:8080/login" -H "Content-Type: application/json" -d '{
    "email": "nuvem@insper.edu.br",
    "senha": "nuvem0"
}'
```
```
Invoke-RestMethod -Uri 'http://a82c0a93257ec433189a7611363e86be-977945615.us-east-2.elb.amazonaws.com/consultar' -Method GET -Headers @{ "Content-Type" = "application/json"; "Authorization" = "Bearer (token)" } -Body '{"email": "teste1811@gmail.com", "senha": "cloudo"}'
```
### ** Outros comandos**
- `kubectl get pods`
- `kubectl get services -n`
- `kubectl logs (pod) -n cloud-project`
- `kubectl run debug-pod --rm -it --image=busybox -n cloud-project -- /bin/sh`
