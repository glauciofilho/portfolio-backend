# 🎯 Portfolio Backend API

**Creation Date:** April 2026

Django backend server to manage data for a personal portfolio website. The API provides endpoints to manage projects, contact messages, and Google Analytics tracking data.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Architecture](#project-architecture)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Environment Variables](#environment-variables)
- [Getting Started](#getting-started)
- [Directory Structure](#directory-structure)
- [Django Applications](#django-applications)
- [API Endpoints](#api-endpoints)
- [Docker](#docker)
- [Database](#database)
- [Security](#security)
- [Middleware](#middleware)
- [Contributing](#contributing)
- [License](#license)

---

## 👀 Overview

This project is a REST API backend built with Django that powers a personal portfolio website. The application manages three main functionalities:

1. **Projects Management** - Create, read, update, and delete portfolio projects
2. **Contact System** - Receive and store contact messages from visitors
3. **Analytics** - Google Analytics integration for traffic data collection

The server is configured for production hosting with PostgreSQL as the database and is containerized using Docker to facilitate deployment.

---

## 🛠️ Technologies Used

### Backend
- **Python 3.13** - Programming language
- **Django 6.0+** - Web framework
- **Django REST Framework** - For building REST APIs
- **PostgreSQL** - Relational database
- **Gunicorn** - WSGI server for production

### Tools and Dependencies
- **python-dotenv** - Environment variables management
- **django-cors-headers** - CORS (Cross-Origin Resource Sharing) support
- **whitenoise** - Serving static files in production
- **psycopg2** - PostgreSQL adapter for Python
- **Google Analytics API** - Google Analytics integration

### DevOps
- **Docker** - Application containerization
- **Docker Compose** - Container orchestration (optional)
- **Alpine Linux** - Lightweight base image for Docker

---

## 🏗️ Project Architecture

```
portifolio-backend/
├── backend/                    # Main Django configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main routing
│   ├── wsgi.py                # WSGI interface for production
│   └── asgi.py                # ASGI interface for production
├── projects/                  # App for managing projects
│   ├── admin.py              # Django admin
│   ├── models.py             # Data models
│   ├── views.py              # Views/Controllers
│   ├── urls.py               # App-specific routing
│   ├── utils.py              # Utility functions
│   ├── migrations/           # Migration history
│   └── tests.py              # Unit tests
├── analytics/                 # Google Analytics integration app
│   ├── models.py             # Data models (currently empty)
│   ├── views.py              # Views/Controllers
│   ├── urls.py               # App-specific routing
│   ├── services/             # Business logic
│   │   ├── ga_service.py    # Main GA service
│   │   └── ga_queries.py    # Pre-configured queries
│   ├── migrations/           # Migration history
│   └── tests.py              # Unit tests
├── contact/                   # Contact messages management app
│   ├── models.py             # Data models
│   ├── views.py              # Views/Controllers
│   ├── urls.py               # App-specific routing
│   ├── admin.py              # Django admin
│   ├── migrations/           # Migration history
│   └── tests.py              # Unit tests
├── manage.py                  # Django CLI utility
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── entrypoint.sh             # Container startup script
└── README.md                 # This file
```

---

## 📋 Prerequisites

### Local Environment
- **Python 3.13** or higher
- **pip** (Python package manager)
- **PostgreSQL 12** or higher
- **Git** (version control)

### Using Docker
- **Docker 20.0** or higher
- **Docker Compose 1.29** or higher (optional)

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/glauciofilho/portfolio-backend.git
cd portifolio-backend
```

### 2. Set Up Environment Variables

Create a `.env` file at the project root:

```bash
cp .env.example .env  # If example file exists
# or manually create a .env file
```

### 3. Install Dependencies (Local Environment)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Run Migrations (Local Environment)

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional - Local Environment)

```bash
python manage.py createsuperuser
```

---

## 🔐 Environment Variables

Configure the following variables in your `.env` file:

```env
# Django Settings
SECRET_KEY=your_very_long_and_secret_key
DEBUG=False
ALLOWED_HOSTS=api.glauciofilho.com.br,glauciofilho.com.br

# PostgreSQL Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=portfolio_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432

# Database (Docker - if used)
POSTGRES_DB=portfolio_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_HOST=db

# Superuser (Django)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=super_secure_password

# Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID=your_property_id
GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/service-account-key.json

# CORS and Trusted Hosts
CORS_ALLOWED_ORIGINS=https://glauciofilho.com.br,https://api.glauciofilho.com.br
CSRF_TRUSTED_ORIGINS=https://glauciofilho.com.br,https://api.glauciofilho.com.br
```

### Variable Descriptions

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for security | `your-very-secret-key-here` |
| `DEBUG` | Django debug mode | `False` (always False in production) |
| `DB_NAME` | PostgreSQL database name | `portfolio_db` |
| `DB_USER` | PostgreSQL user | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | `secure_password` |
| `DB_HOST` | Database host | `localhost` or `db` (Docker) |
| `DB_PORT` | PostgreSQL port | `5432` |
| `GOOGLE_ANALYTICS_PROPERTY_ID` | Google Analytics property ID | `G-XXXXXXXXXX` |

---

## 🏁 Getting Started

### Local Environment

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run development server
python manage.py runserver

# Server will be available at: http://localhost:8000
```

### Docker

```bash
# Build Docker image
docker build -t portfolio-backend:latest .

# Run container
docker run -p 8888:8888 \
  -e SECRET_KEY="your_secret_key" \
  -e DB_HOST="your_db_host" \
  -e DB_NAME="portfolio_db" \
  -e DB_USER="postgres" \
  -e DB_PASSWORD="password" \
  portfolio-backend:latest

# Server will be available at: http://localhost:8888
```

### Docker Compose (Recommended)

```bash
# Create docker-compose.yml file at project root
docker-compose up --build

# Server will be at: http://localhost:8888
# PostgreSQL will be at: localhost:5432
```

---

## 📁 Directory Structure

### `backend/` Directory
Contains main Django configuration:
- **settings.py** - Database, installed apps, middleware, and security settings
- **urls.py** - Main application routing
- **wsgi.py** - WSGI interface for production with Gunicorn
- **asgi.py** - Alternative ASGI interface for production

### `projects/` Directory
Manages portfolio projects:
- **models.py** - Defines Project, Stack, StackProject, File models
- **views.py** - REST APIs for projects
- **urls.py** - Endpoints: `/api/projects/`, `/api/stacks/`
- **utils.py** - Helper functions
- **admin.py** - Admin interface

### `analytics/` Directory
Google Analytics integration:
- **services/** - Business logic
  - **ga_service.py** - Main GA integration service
  - **ga_queries.py** - Pre-configured queries
- **views.py** - Analytics endpoints
- **urls.py** - Routes: `/analytics/data/`, `/analytics/reports/`

### `contact/` Directory
Contact message management:
- **models.py** - ContactMessage model
- **views.py** - APIs for creating messages
- **urls.py** - Endpoints: `/contact/messages/`
- **admin.py** - Admin interface

---

## 🔌 Django Applications

### 1. Projects App

#### Models

**Project**
```python
- name_pt: CharField (Portuguese name)
- name_en: CharField (English name)
- summary_pt: TextField (Portuguese summary)
- summary_en: TextField (English summary)
- image_url: URLField (Image URL)
- created_at: DateTimeField (Creation date)
```

**Stack**
```python
- name: CharField (Stack/technology name)
- badge_url: URLField (Badge URL)
```

**StackProject**
```python
- project: ForeignKey(Project)
- stack: ForeignKey(Stack)
- unique_together: (project, stack)
```

**File**
```python
- project: ForeignKey(Project)
- ... (additional fields)
```

### 2. Contact App

#### Models

**ContactMessage**
```python
- name: CharField (Sender name)
- email: EmailField (Sender email)
- message: TextField (Message body)
- created_at: DateTimeField (Creation date/time)
- ip_address: GenericIPAddressField (Sender IP)
- user_agent: TextField (Browser user agent)
```

### 3. Analytics App

#### Services

**GA Service** - Google Analytics Integration
- Service account authentication
- Event and report queries
- Traffic metric calculations

**GA Queries** - Pre-configured Queries
- Daily reports
- Monthly reports
- Engagement metrics

---

## 🔌 API Endpoints

### Projects

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/projects/` | List all projects |
| GET | `/api/projects/{id}/` | Get project details |
| POST | `/api/projects/` | Create new project |
| PUT | `/api/projects/{id}/` | Update project |
| DELETE | `/api/projects/{id}/` | Delete project |

### Stacks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stacks/` | List all stacks |
| POST | `/api/stacks/` | Create new stack |

### Contact

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contact/messages/` | List contact messages |
| POST | `/contact/messages/` | Create new message |

### Analytics

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/analytics/data/` | Get GA data |
| GET | `/analytics/reports/` | Get GA reports |

### Administration

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/` | Django admin interface |

---

## 🐳 Docker

### Dockerfile Configuration

The project is configured with Docker using Alpine Linux for a lightweight image:

```dockerfile
FROM python:3.13-alpine

# Install dependencies for PostgreSQL and compilation
RUN apk add --no-cache gcc musl-dev postgresql-dev postgresql-client ...

# Copy dependencies and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code and execute entrypoint
COPY . .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8888"]
```

### Entrypoint Script (entrypoint.sh)

The startup script:
1. Waits for PostgreSQL availability
2. Runs automatic migrations
3. Creates superuser if it doesn't exist
4. Starts the Gunicorn server

### Build and Run

```bash
# Build
docker build -t portfolio-backend:latest .

# Run with environment variables
docker run -p 8888:8888 -e SECRET_KEY=xyz ... portfolio-backend:latest

# Logs
docker logs -f <container_id>

# Stop container
docker stop <container_id>
```

---

## 🗄️ Database

### PostgreSQL

The project uses PostgreSQL as the primary database.

#### Configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
```

#### Migrations

```bash
# Create migration after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

#### Backup

```bash
# Database backup
pg_dump portfolio_db > backup.sql

# Restore backup
psql portfolio_db < backup.sql
```

---

## 🔒 Security

### Security Configuration

1. **ALLOWED_HOSTS** - Only trusted domains
   ```python
   ALLOWED_HOSTS = ['api.glauciofilho.com.br', 'glauciofilho.com.br', ...]
   ```

2. **CORS** - Cross-origin resource control
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://glauciofilho.com.br",
       "https://api.glauciofilho.com.br",
   ]
   ```

3. **CSRF** - CSRF protection
   ```python
   CSRF_TRUSTED_ORIGINS = [
       "https://glauciofilho.com.br",
       "https://api.glauciofilho.com.br",
   ]
   ```

4. **DEBUG** - Must be `False` in production
   ```python
   DEBUG = "False"  # Never True in production
   ```

5. **SECRET_KEY** - Secure and unique key
   - Generate with: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
   - Never commit to repository

6. **HTTPS** - Always use in production
   ```python
   SECURE_SSL_REDIRECT = True
   SECURE_HSTS_SECONDS = 31536000
   SECURE_HSTS_INCLUDE_SUBDOMAINS = True
   SECURE_HSTS_PRELOAD = True
   ```

---

## 🔧 Middleware

The application uses the following middleware:

1. **SecurityMiddleware** - Adds HTTP security headers
2. **WhiteNoiseMiddleware** - Serves static files in production
3. **SessionMiddleware** - Session management
4. **CorsMiddleware** - CORS handling
5. **CommonMiddleware** - Common Django functionality
6. **CsrfViewMiddleware** - CSRF protection
7. **AuthenticationMiddleware** - User authentication
8. **MessageMiddleware** - Message framework
9. **XFrameOptionsMiddleware** - Clickjacking protection

---

## 💻 Local Development

### Running Tests

```bash
# All tests
python manage.py test

# Tests for specific app
python manage.py test projects
python manage.py test contact
python manage.py test analytics

# With code coverage (if coverage installed)
coverage run --source='.' manage.py test
coverage report
coverage html  # Generates HTML report
```

### Django Shell

```bash
# Access Django shell
python manage.py shell

# Usage examples
>>> from projects.models import Project
>>> Project.objects.all()
>>> project = Project.objects.create(name_pt="My Project", ...)
```

### Create Admin User

```bash
python manage.py createsuperuser

# Access at: http://localhost:8000/admin
```

---

## 🔍 Debugging

### Enable Debug Mode (Development Only)

```env
DEBUG=True
```

### Logs

Check `debug.log` file or configure in settings.py:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

---

## 📦 Requirements

```
Django>=6.0
gunicorn
psycopg2-binary
django-cors-headers
whitenoise
python-dotenv
```

---

## 🤝 Contributing

### How to Contribute

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python
- Add tests for new features
- Document functions and classes
- Use semantic commits

---

## 📝 Changelog

### Version 1.0.0 - April 2026

**Project Initialization**
- ✅ Initial Django setup
- ✅ PostgreSQL database configuration
- ✅ Projects App with portfolio management
- ✅ Contact App for messages
- ✅ Analytics App with Google Analytics integration
- ✅ Application dockerization
- ✅ CORS and security configuration
- ✅ Automatic migrations entrypoint

---

## 🆘 Troubleshooting

### Error: `psycopg2 not found`

```bash
pip install psycopg2-binary
```

### Error: `Database connection refused`

Check:
1. PostgreSQL is running
2. Environment variables (DB_HOST, DB_PORT) are correct
3. Database credentials (DB_USER, DB_PASSWORD)

### Error: `SECRET_KEY not set`

Set in `.env`:
```env
SECRET_KEY=your_very_long_and_secret_key
```

### Migration failing

```bash
# Database reset (WARNING - deletes data!)
python manage.py migrate analytics zero
python manage.py migrate contact zero
python manage.py migrate projects zero

# Reapply
python manage.py migrate
```

---

## 📚 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Google Analytics API](https://developers.google.com/analytics/devguides/reporting/data/v1)

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 👨‍💻 Author

**Glaucio Filho**  
Website: [glauciofilho.com.br](https://glauciofilho.com.br)  
Email: contato@glauciofilho.com.br

---

## 📞 Support

For questions or issues:
1. Open an [Issue](https://github.com/glauciofilho/portfolio-backend/issues)
2. Check the Troubleshooting section above
3. See the [Django Documentation](https://docs.djangoproject.com/)

---

**Last Updated:** April 2026  
**Version:** 1.0.0
**Status:** ✅ In Production
