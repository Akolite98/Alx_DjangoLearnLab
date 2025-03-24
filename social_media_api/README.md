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

## **Posts & Comments API Endpoints**  

### **Posts**  
- `GET /api/posts/` → List all posts (paginated)  
- `POST /api/posts/` → Create a post (auth required)  
- `GET /api/posts/{id}/` → Retrieve a post  
- `PUT /api/posts/{id}/` → Update a post (author only)  
- `DELETE /api/posts/{id}/` → Delete a post (author only)  

### **Comments**  
- `GET /api/comments/` → List all comments  
- `POST /api/comments/` → Create a comment (auth required)  
- `DELETE /api/comments/{id}/` → Delete a comment (author only)  

### **Filtering**  
- `GET /api/posts/?title=example` → Filter by title  
- `GET /api/posts/?author=username` → Filter by author  