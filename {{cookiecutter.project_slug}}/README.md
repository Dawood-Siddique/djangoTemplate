# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Features

- Django REST Framework
- JWT Authentication
- Custom User Model with OTP functionality
- API Documentation with Swagger
- CORS support
- Modern Python dependency management with uv

## Installation

1. Install dependencies:
```bash
uv sync
```

2. Run migrations:
```bash
uv run python manage.py migrate
```

3. Create a superuser:
```bash
uv run python manage.py createsuperuser
```

4. Start the development server:
```bash
uv run python manage.py runserver
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc: http://localhost:8000/api/redoc/

## Author

{{cookiecutter.author_name}} ({{cookiecutter.author_email}})
