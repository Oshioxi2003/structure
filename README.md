# EDU Project - Full Stack Django + Next.js

Educational platform built with Django REST Framework and Next.js 14.

## 🚀 Quick Start

### Backend (Django)
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

- **backend/** - Django REST API
- **frontend/** - Next.js 14 App
- **BACKEND_GUIDE.md** - Detailed backend documentation

## 📚 Documentation

See [BACKEND_GUIDE.md](./BACKEND_GUIDE.md) for detailed backend setup and API documentation.

## 🛠️ Tech Stack

### Backend
- Django 4.2+
- Django REST Framework
- PostgreSQL / SQLite
- Docker

### Frontend
- Next.js 14
- React 18
- SCSS
- Docker

## 🐳 Docker

```bash
# Backend
cd backend
docker-compose up

# Frontend
cd frontend
docker-compose up
```

## 📝 License

MIT
