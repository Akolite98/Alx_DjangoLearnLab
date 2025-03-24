# Social Media API

## Setup

1. Create virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install requirements: `pip install django djangorestframework`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`

## API Endpoints

- POST `/api/auth/register/` - User registration
- POST `/api/auth/login/` - User login