# Blog API Project

A modern RESTful API built with Django REST Framework that powers a blog platform.


*by "Django for APIs" book*

## Overview

This project implements a full-featured blog API with user authentication, permissions, and API documentation. It allows users to create, read, update, and delete blog posts through a RESTful API interface.

## Features

- Full CRUD operations for blog posts
- User authentication using Token authentication
- Custom permissions (only authors can edit their posts)
- API documentation with Swagger UI
- User registration and authentication endpoints
- Browsable API interface

## Tech Stack

- Django 5.2
- Django REST Framework
- dj-rest-auth for authentication
- django-allauth for registration
- drf-yasg for Swagger documentation
- SQLite database
- CORS support

## API Endpoints

- `api/v1/posts/` - List and create posts
- `api/v1/posts/<id>/` - Retrieve, update, and delete posts
- `api/v1/users/` - List users
- `api/v1/auth/` - Authentication endpoints
- `api/v1/auth/registration/` - User registration
- `docs/` - Swagger UI documentation
- `schema/` - API schema

## Authentication

The API uses Token authentication. To make authenticated requests:

1. Register a new user at `/api/v1/auth/registration/`
2. Login at `/api/v1/auth/login/`
3. Use the received token in the Authorization header: `Token <your-token>`

## Local Development

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit the API documentation at `http://127.0.0.1:8000/docs/`

## Permissions

- Anonymous users can only read posts
- Authenticated users can create posts
- Post authors can update and delete their own posts
- Admin users have full access to all posts

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the terms of the BSD license.

## Acknowledgments

- Special thanks to the authors of "Django for APIs" book
- Django REST Framework team
- Django community
