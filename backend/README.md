# Backend - Django Project

## 📋 Cấu trúc dự án

```
backend/
├─ manage.py
├─ pyproject.toml
├─ README.md
├─ .env
├─ Dockerfile
├─ docker-compose.yml
├─ Makefile
│
├─ config/              # Django project config
│  ├─ settings/
│  │  ├─ base.py       # Settings chung
│  │  ├─ dev.py        # Development
│  │  └─ prod.py       # Production
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
│
├─ apps/                # Django apps
│  ├─ common/          # Utilities chung
│  │  ├─ exceptions.py
│  │  ├─ pagination.py
│  │  ├─ permissions.py
│  │  └─ utils/
│  │
│  └─ users/           # User management
│     ├─ models.py
│     ├─ serializers.py
│     ├─ views.py
│     ├─ urls.py
│     ├─ selectors.py  # Read queries
│     ├─ services.py   # Business logic
│     └─ signals.py
│
├─ requirements/
│  ├─ base.txt
│  ├─ dev.txt
│  └─ prod.txt
│
├─ scripts/
├─ templates/
├─ static/
└─ media/
```

## 🚀 Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd backend
```

### 2. Tạo virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements/dev.txt
```

### 4. Cấu hình môi trường

Sao chép file `.env` và điền thông tin:

```bash
cp .env.example .env
```

### 5. Chạy migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Tạo superuser

```bash
python manage.py createsuperuser
```

### 7. Chạy development server

```bash
python manage.py runserver
```

## 🔧 Makefile Commands

```bash
make run          # Chạy development server
make migrate      # Chạy migrations
make migrations   # Tạo migrations
make test         # Chạy tests
make shell        # Mở Django shell
make superuser    # Tạo superuser
```

## 📝 API Endpoints

### Users
- `GET /api/users/` - List users
- `POST /api/users/` - Create user
- `GET /api/users/{id}/` - Get user detail
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user
- `GET /api/users/me/` - Get current user
- `PUT /api/users/update_profile/` - Update profile
- `POST /api/users/change_password/` - Change password
- `GET /api/users/search/?q=query` - Search users

## 🐳 Docker

### Development

```bash
docker-compose up
```

### Production

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📚 Kiến trúc

### Selectors vs Services

- **Selectors**: Chỉ đọc dữ liệu từ database (read-only queries)
- **Services**: Xử lý business logic và ghi dữ liệu (write operations)

### Custom User Model

User model kế thừa từ `AbstractUser` với các field bổ sung:
- email (unique)
- phone
- avatar
- bio
- date_of_birth
- is_verified

## 🧪 Testing

```bash
# Chạy tất cả tests
pytest

# Chạy với coverage
pytest --cov

# Chạy specific test
pytest apps/users/tests/
```

## 📦 Dependencies

Xem file `requirements/base.txt` để biết danh sách đầy đủ.

## 🔐 Security

- SECRET_KEY phải được đổi trong production
- DEBUG=False trong production
- Sử dụng HTTPS trong production
- Cấu hình CORS đúng cách

## 📄 License

MIT License
