# 🎓 EDU Project - Full Stack

## 📂 Cấu trúc dự án

```
edu/
├─ backend/                # Django REST API
│  ├─ manage.py
│  ├─ config/              # Django settings
│  │  ├─ settings/
│  │  │  ├─ base.py
│  │  │  ├─ dev.py
│  │  │  └─ prod.py
│  │  └─ urls.py
│  │
│  ├─ apps/                # Django apps
│  │  ├─ common/          # Common utilities
│  │  │  ├─ exceptions.py
│  │  │  ├─ pagination.py
│  │  │  ├─ permissions.py
│  │  │  └─ utils/
│  │  │
│  │  └─ users/           # User management
│  │     ├─ models.py
│  │     ├─ serializers.py
│  │     ├─ views.py
│  │     ├─ selectors.py
│  │     ├─ services.py
│  │     └─ signals.py
│  │
│  ├─ requirements/
│  ├─ scripts/
│  └─ Dockerfile
│
└─ frontend/              # Next.js 14+
   ├─ src/
   │  ├─ app/            # Next.js App Router
   │  ├─ components/     # Reusable components
   │  ├─ services/       # API calls
   │  ├─ hooks/          # Custom React hooks
   │  └─ utils/          # Utilities
   │
   └─ public/
      └─ assets/
```

## 🚀 Khởi động Backend (Django)

### 1. Cài đặt dependencies

```bash
cd backend
pip install -r requirements/dev.txt
```

### 2. Cấu hình môi trường

File `.env` đã được tạo sẵn với cấu hình mặc định:

```env
SECRET_KEY=your-secret-key-here
DJANGO_ENV=dev
DEBUG=True
DB_NAME=edu_db
DB_USER=postgres
DB_PASSWORD=postgres
```

### 3. Chạy migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Tạo superuser

```bash
python manage.py createsuperuser
```

### 5. Chạy development server

```bash
python manage.py runserver
# hoặc
make run
```

Server sẽ chạy tại: **http://127.0.0.1:8000/**

### 6. Truy cập Django Admin

**http://127.0.0.1:8000/admin/**

## 📡 API Endpoints

### Users API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | List all users |
| POST | `/api/users/` | Create new user |
| GET | `/api/users/{id}/` | Get user detail |
| PUT | `/api/users/{id}/` | Update user |
| DELETE | `/api/users/{id}/` | Delete user |
| GET | `/api/users/me/` | Get current user profile |
| PUT | `/api/users/update_profile/` | Update current user |
| POST | `/api/users/change_password/` | Change password |
| GET | `/api/users/search/?q=query` | Search users |

## 🎯 Kiến trúc Backend

### Settings Structure

- **base.py**: Cấu hình chung cho tất cả môi trường
- **dev.py**: Cấu hình development (SQLite, Debug mode)
- **prod.py**: Cấu hình production (PostgreSQL, Security)

### App Structure (Selectors + Services Pattern)

#### **Selectors** (selectors.py)
- Chỉ đọc dữ liệu (read-only)
- Queries đơn giản, phức tạp
- Không có side effects

```python
# Example
def get_user_by_id(user_id: int) -> Optional[User]:
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
```

#### **Services** (services.py)
- Business logic
- Write operations
- Side effects (email, cache, etc.)
- Transaction handling

```python
# Example
@transaction.atomic
def create_user(data: Dict[str, Any]) -> User:
    # Business logic here
    user = User(**data)
    user.set_password(password)
    user.save()
    return user
```

### Custom User Model

Model `User` kế thừa từ `AbstractUser` với các field:

- `email` (unique)
- `phone`
- `avatar` (ImageField)
- `bio`
- `date_of_birth`
- `is_verified`
- `created_at`
- `updated_at`

## 🐳 Docker

### Development

```bash
cd backend
docker-compose up
```

Services:
- **backend**: Django app (port 8000)
- **db**: PostgreSQL (port 5432)

## 🔧 Makefile Commands

```bash
make run          # Chạy development server
make migrate      # Run migrations
make migrations   # Create migrations
make test         # Run tests
make shell        # Django shell
make superuser    # Create superuser
make install      # Install dependencies
make clean        # Clean pyc files
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific app tests
pytest apps/users/tests/
```

## 📦 Main Dependencies

### Backend
- Django 4.2+
- Django REST Framework
- django-cors-headers
- python-dotenv
- Pillow (for images)
- psycopg2-binary (PostgreSQL)

### Development
- pytest
- pytest-django
- black (code formatter)
- flake8 (linter)

## 🔐 Security Notes

- ⚠️ Đổi `SECRET_KEY` trong production
- ⚠️ Set `DEBUG=False` trong production
- ⚠️ Cấu hình `ALLOWED_HOSTS` đúng
- ⚠️ File `.env` không được commit vào git
- ⚠️ Sử dụng HTTPS trong production

## 📝 Next Steps

1. ✅ Backend structure đã hoàn tất
2. ✅ User model và authentication đã setup
3. ✅ API endpoints đã sẵn sàng
4. 📋 TODO:
   - Thêm JWT authentication
   - Thêm API documentation (Swagger)
   - Setup CI/CD
   - Thêm các app khác (courses, lessons, etc.)

## 🆘 Troubleshooting

### Lỗi: "No module named 'psycopg2'"

Nếu dùng SQLite (dev), đã được config sẵn trong `dev.py`.
Nếu dùng PostgreSQL, cài:

```bash
pip install psycopg2-binary
```

### Lỗi: "CORS"

Đã cấu hình CORS trong `dev.py`:

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
```

## 📞 Support

Xem thêm:
- Django docs: https://docs.djangoproject.com/
- DRF docs: https://www.django-rest-framework.org/

---

**Happy Coding! 🚀**
