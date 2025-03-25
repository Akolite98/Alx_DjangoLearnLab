# Deployment Guide

## Requirements
- Python 3.9
- PostgreSQL
- Heroku CLI

## Steps
1. Set environment variables
2. Run `heroku create`
3. Push code: `git push heroku main`
4. Run migrations: `heroku run python manage.py migrate`
5. Collect static files: `heroku run python manage.py collectstatic`

## Environment Variables
- SECRET_KEY
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST