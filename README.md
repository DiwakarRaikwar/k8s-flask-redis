\# 🚀 Flask + Redis App on Kubernetes (Minikube)



A two-tier web application deployed on Kubernetes using Minikube.

Built with Flask (frontend) and Redis (backend) to demonstrate

container orchestration skills.



\## 🏗️ Architecture



Browser → Flask Service (NodePort) → Flask Pod → Redis Service → Redis Pod



\## 🛠️ Tech Stack



\- \*\*Flask\*\* - Python web framework

\- \*\*Redis\*\* - In-memory database (visit counter)

\- \*\*Docker\*\* - Containerization

\- \*\*Kubernetes\*\* - Container orchestration

\- \*\*Minikube\*\* - Local Kubernetes cluster



\## 📁 Project Structure



k8s-flask-redis/

├── app.py                  # Flask application

├── requirements.txt        # Python dependencies

├── Dockerfile              # Docker image definition

└── k8s/

├── flask-deployment.yaml

├── flask-service.yaml

├── redis-deployment.yaml

└── redis-service.yaml



\## 🚀 How to Run



\### Prerequisites

\- Docker Desktop

\- Minikube

\- kubectl



\### Steps



1\. Start Minikube

```bash

minikube start --driver=docker --memory=1800 --cpus=2

```



2\. Build Docker image

```bash

docker build -t flask-redis-app:latest .

```



3\. Load image into Minikube

```bash

docker save flask-redis-app:latest -o flask-redis-app.tar

minikube image load flask-redis-app.tar

```



4\. Deploy to Kubernetes

```bash

kubectl apply -f k8s/redis-deployment.yaml

kubectl apply -f k8s/redis-service.yaml

kubectl apply -f k8s/flask-deployment.yaml

kubectl apply -f k8s/flask-service.yaml

```



5\. Access the app

```bash

minikube service flask-service --url

```



\## 📸 Screenshots



\### App Running in Browser

!\[App Screenshot](app-screenshot.png)



\### Kubernetes Pods Running

!\[Pods Screenshot](pods-screenshot.png)



\## 👨‍💻 Author

\*\*Diwakar Raikwar\*\*

\- GitHub: \[@DiwakarRaikwar](https://github.com/DiwakarRaikwar)

