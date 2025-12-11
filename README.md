# Sistemas Distribuídos - Q1, Q2 e Q3

- **Q1:** Multicast com Ordenação Total  
- **Q2:** Exclusão Mútua Distribuída (Token Ring)  
- **Q3:** Eleição de Líder (Algoritmo do Valentão) 

## 🚀 Instalação e Execução

### 1. Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

### 2. Clonar o repositório
```bash
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd 
```

### 3. Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
```

### 4. Iniciar Minikube
```bash
minikube start
```

### 5. Build da imagem dentro do Minikube
```bash
eval $(minikube docker-env)   # Linux/Mac
& minikube -p minikube docker-env --shell powershell | Invoke-Expression   # Windows PowerShell

docker build -t q1-total-order:latest .
```

### 6. Deploy no Kubernetes
```bash
kubectl apply -f k8s/namespace.yaml
kubectl -n q1 apply -f k8s/statefulset.yaml
```

### 7. Verificar pods
```bash
kubectl -n q1 get pods
```

## 🧪 Testes

### 🔹 Q1 – Multicast com Ordenação Total

1. Enviar mensagem multicast:
```bash
Invoke-WebRequest -Uri "http://localhost:8000/multicast" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"text":"Mensagem A"}'
```

2. Ver logs:
```bash
kubectl -n q1 logs -f q1-app-0
kubectl -n q1 logs -f q1-app-1
kubectl -n q1 logs -f q1-app-2
```
### 🔹 Q2 – Exclusão Mútua Distribuída (Token Ring)

1. P0 entra na seção crítica:
```bash
Invoke-WebRequest -Uri "http://localhost:8000/request_cs" -Method POST
```

2. P0 libera e passa token para P1:
```bash
Invoke-WebRequest -Uri "http://localhost:8000/release_cs" -Method POST
```

3. P1 entra e libera para P2:
```bash
Invoke-WebRequest -Uri "http://localhost:8001/request_cs" -Method POST
Invoke-WebRequest -Uri "http://localhost:8001/release_cs" -Method POST
```

4. P2 entra:
```bash
Invoke-WebRequest -Uri "http://localhost:8002/request_cs" -Method POST
```

### 🔹 Q3 – Eleição de Líder (Valentão)

1. Iniciar eleição em P0:
```bash
Invoke-WebRequest -Uri "http://localhost:8000/election" -Method POST
```

2. Logs esperados:
```bash
[ELECTION] P0 iniciou eleição
[ELECTION] P1 recebeu ELEIÇÃO de P0 e respondeu OK
[ELECTION] P2 não recebeu OK. Assume liderança.
[COORDINATOR] P2 anunciado como líder por P2
[COORDINATOR] P0 registrou líder = P2
[COORDINATOR] P1 registrou líder = P2
```

3. Consultar coordenador:
```bash
Invoke-WebRequest -Uri "http://localhost:8001/coordinator" -Method GET
```