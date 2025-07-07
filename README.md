# Django REST API Template

A Cookiecutter template for creating Django REST API projects with modern best practices.

## Features

- Django REST Framework
- JWT Authentication with SimpleJWT
- Custom User Model with OTP functionality
- API Documentation with drf-spectacular (Swagger/ReDoc)
- CORS support
- Modern Python dependency management with uv
- Well-structured app organization

## Usage

1. Install cookiecutter:
```bash
pip install cookiecutter
```

2. Generate a new project:
```bash
cookiecutter https://github.com/Dawood-Siddique/starter-kit-dj
```

3. Follow the prompts to customize your project

4. Navigate to your new project and start developing!

## What you'll be prompted for

- **project_name**: The human-readable name of your project
- **project_slug**: The technical name (used for directories and package names)
- **author_name**: Your name
- **author_email**: Your email address
- **description**: A brief description of your project

## Template Structure

The generated project includes:

- **apps/**: Organized Django apps
- **core/**: Django project settings and configuration
- **Custom User Model**: Email-based authentication with OTP support
- **API Views**: Ready-to-use authentication endpoints
- **Tests**: Basic test structure
- **Modern tooling**: uv for dependency management

## Getting Started with Generated Project

After generating your project:

1. Install dependencies: `uv sync`
2. Run migrations: `uv run python manage.py migrate`
3. Create superuser: `uv run python manage.py createsuperuser`
4. Start server: `uv run python manage.py runserver`
5. Visit API docs: http://localhost:8000/api/docs/

## License

This template is open source and available under the MIT License.
