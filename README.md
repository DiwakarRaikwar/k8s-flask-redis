# 🚀 Flask + Redis App on Kubernetes (Minikube)

A two-tier web application deployed on Kubernetes using Minikube. Built with Flask (frontend) and Redis (backend) to demonstrate container orchestration skills.

## 🏗️ Architecture

Browser → Flask Service (NodePort) → Flask Pod → Redis Service → Redis Pod

## 🛠️ Tech Stack

- **Flask** - Python web framework
- **Redis** - In-memory database (visit counter)
- **Docker** - Containerization
- **Kubernetes** - Container orchestration
- **Minikube** - Local Kubernetes cluster

## 📁 Project Structure

k8s-flask-redis/
├── app.py
├── requirements.txt
├── Dockerfile
└── k8s/
    ├── flask-deployment.yaml
    ├── flask-service.yaml
    ├── redis-deployment.yaml
    └── redis-service.yaml

## 🚀 How to Run

### Prerequisites
- Docker Desktop
- Minikube
- kubectl

### Steps

**1. Start Minikube**

minikube start --driver=docker --memory=1800 --cpus=2

**2. Build Docker image**

docker build -t flask-redis-app:latest .

**3. Load image into Minikube**

docker save flask-redis-app:latest -o flask-redis-app.tar
minikube image load flask-redis-app.tar

**4. Deploy to Kubernetes**

kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/redis-service.yaml
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml

**5. Access the app**

minikube service flask-service --url

## 📸 Screenshots

### App Running in Browser
![App Screenshot](https://raw.githubusercontent.com/DiwakarRaikwar/k8s-flask-redis/main/app-screenshot.png)

### Kubernetes Pods Running
![Pods Screenshot](https://raw.githubusercontent.com/DiwakarRaikwar/k8s-flask-redis/main/pods-screenshot.png)

## 👨‍💻 Author

**Diwakar Raikwar**
- GitHub: [@DiwakarRaikwar](https://github.com/DiwakarRaikwar)