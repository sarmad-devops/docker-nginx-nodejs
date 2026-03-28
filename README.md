# 🐳 Docker + Nginx + Flask — DevOps Project

A production-ready containerized Flask application served through Nginx reverse proxy using Docker Compose.

---

## 🏗️ Architecture
```
User Request
     │
     ▼
┌─────────┐
│  Nginx  │  ← Reverse Proxy (Port 8080)
└────┬────┘
     │
     ▼
┌─────────┐
│  Flask  │  ← Python App (Port 5000)
│ Gunicorn│  ← Production WSGI Server
└─────────┘
```

---

## ✅ Features

- Multi-stage Docker build — smaller image size
- Nginx reverse proxy — production standard
- Gunicorn WSGI server — not a dev server
- Health check endpoint — container monitoring ready
- Environment variables — configurable per environment
- Custom Docker network — service isolation

---

## 📁 Project Structure
```
docker-nginx-nodejs/
├── app/
│   ├── app.py            # Flask application
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Multi-stage build
├── nginx/
│   └── nginx.conf        # Reverse proxy config
├── docker-compose.yml    # Multi-container orchestration
└── README.md
```

---

## 🚀 Run Locally

**Clone the repo:**
```bash
git clone https://github.com/sarmad-devops/docker-nginx-nodejs.git
cd docker-nginx-nodejs
```

**Start the app:**
```bash
docker-compose up --build
```

**Access endpoints:**
```
http://localhost:8080        → Welcome message
http://localhost:8080/health → Health status
http://localhost:8080/info   → App info
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check status |
| `/info` | GET | App version and environment info |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python Flask | Web application |
| Gunicorn | Production WSGI server |
| Nginx | Reverse proxy |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |