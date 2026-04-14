# 🎯 Portfolio Backend API

**Data de Criação:** Abril/2026

Servidor backend desenvolvido em Django para gerenciar dados de um website portfólio pessoal. A API fornece endpoints para gerenciar projetos, mensagens de contato e dados analytícos do Google Analytics.

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Inicialização](#inicialização)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Aplicações Django](#aplicações-django)
- [Endpoints da API](#endpoints-da-api)
- [Docker](#docker)
- [Banco de Dados](#banco-de-dados)
- [Segurança](#segurança)
- [Middleware](#middleware)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 👀 Visão Geral

Este projeto é um backend REST API desenvolvido com Django que alimenta um website portfólio pessoal. A aplicação gerencia três principais funcionalidades:

1. **Gerenciamento de Projetos** - Criação, leitura, atualização e exclusão de projetos portfólio
2. **Sistema de Contato** - Recebimento e armazenamento de mensagens de contato dos visitantes
3. **Analytics** - Integração com Google Analytics para coleta de dados de tráfego

O servidor está configurado para ser hospedado em produção com PostgreSQL como banco de dados e é containerizado usando Docker para facilitar o deployment.

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.13** - Linguagem de programação
- **Django 6.0+** - Web framework
- **Django REST Framework** - Para construção de APIs REST
- **PostgreSQL** - Banco de dados relacional
- **Gunicorn** - Servidor WSGI para produção

### Ferramentas e Dependências
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **django-cors-headers** - Suporte a CORS (Cross-Origin Resource Sharing)
- **whitenoise** - Servindo arquivos estáticos em produção
- **psycopg2** - Adaptador PostgreSQL para Python
- **Google Analytics API** - Integração com Analytics do Google

### DevOps
- **Docker** - Containerização da aplicação
- **Docker Compose** - Orquestração de containers (opcional)
- **Alpine Linux** - Imagem base leve para Docker

---

## 🏗️ Arquitetura do Projeto

```
portifolio-backend/
├── backend/                    # Configurações principais do Django
│   ├── settings.py            # Configurações do projeto
│   ├── urls.py                # Roteamento principal
│   ├── wsgi.py                # Interface WSGI para produção
│   └── asgi.py                # Interface ASGI para produção
├── projects/                  # App para gerenciar projetos
│   ├── admin.py              # Admin do Django
│   ├── models.py             # Modelos de dados
│   ├── views.py              # Visões/Controllers
│   ├── urls.py               # Roteamento específico
│   ├── utils.py              # Funções utilitárias
│   ├── migrations/           # Histórico de migrations
│   └── tests.py              # Testes unitários
├── analytics/                 # App de integração com Google Analytics
│   ├── models.py             # Modelos (atualmente vazio)
│   ├── views.py              # Visões/Controllers
│   ├── urls.py               # Roteamento específico
│   ├── services/             # Serviços de negócio
│   │   ├── ga_service.py    # Serviço principal do GA
│   │   └── ga_queries.py    # Queries pré-configuradas
│   ├── migrations/           # Histórico de migrations
│   └── tests.py              # Testes unitários
├── contact/                   # App para gerenciar mensagens de contato
│   ├── models.py             # Modelos de dados
│   ├── views.py              # Visões/Controllers
│   ├── urls.py               # Roteamento específico
│   ├── admin.py              # Admin do Django
│   ├── migrations/           # Histórico de migrations
│   └── tests.py              # Testes unitários
├── manage.py                  # Utilidade Django CLI
├── requirements.txt           # Dependências Python
├── Dockerfile                 # Configuração para Docker
├── entrypoint.sh             # Script de inicialização do container
└── README.md                 # Este arquivo
```

---

## 📋 Pré-requisitos

### Ambiente Local
- **Python 3.13** ou superior
- **pip** (gerenciador de pacotes Python)
- **PostgreSQL 12** ou superior
- **Git** (para controle de versão)

### Usando Docker
- **Docker 20.0** ou superior
- **Docker Compose 1.29** ou superior (opcional)

---

## 🚀 Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/glauciofilho/portfolio-backend.git
cd portifolio-backend
```

### 2. Criar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env  # Se existir um arquivo de exemplo
# ou crie manualmente um arquivo .env
```

### 3. Instalar Dependências (Ambiente Local)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 4. Executar Migrações (Ambiente Local)

```bash
python manage.py migrate
```

### 5. Criar Superusuário (Opcional - Ambiente Local)

```bash
python manage.py createsuperuser
```

---

## 🔐 Variáveis de Ambiente

Configure as seguintes variáveis no arquivo `.env`:

```env
# Django Settings
SECRET_KEY=sua_chave_secreta_muito_longa_e_segura
DEBUG=False
ALLOWED_HOSTS=api.glauciofilho.com.br,glauciofilho.com.br

# Database PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=portfolio_db
DB_USER=postgres
DB_PASSWORD=sua_senha_segura
DB_HOST=localhost
DB_PORT=5432

# Database (Docker - se usar)
POSTGRES_DB=portfolio_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_segura
POSTGRES_HOST=db

# Superuser (Django)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=senha_super_segura

# Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID=seu_property_id
GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/service-account-key.json

# CORS e Hosts Confiáveis
CORS_ALLOWED_ORIGINS=https://glauciofilho.com.br,https://api.glauciofilho.com.br
CSRF_TRUSTED_ORIGINS=https://glauciofilho.com.br,https://api.glauciofilho.com.br
```

### Descrição das Variáveis

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SECRET_KEY` | Chave secreta do Django para segurança | `your-very-secret-key-here` |
| `DEBUG` | Modo debug do Django | `False` (sempre False em produção) |
| `DB_NAME` | Nome do banco de dados PostgreSQL | `portfolio_db` |
| `DB_USER` | Usuário do PostgreSQL | `postgres` |
| `DB_PASSWORD` | Senha do PostgreSQL | `secure_password` |
| `DB_HOST` | Host do banco de dados | `localhost` ou `db` (Docker) |
| `DB_PORT` | Porta do PostgreSQL | `5432` |
| `GOOGLE_ANALYTICS_PROPERTY_ID` | ID da propriedade do Google Analytics | `G-XXXXXXXXXX` |

---

## 🏁 Inicialização

### Ambiente Local

```bash
# Ativar ambiente virtual (se não estiver ativo)
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows

# Executar servidor de desenvolvimento
python manage.py runserver

# O servidor estará disponível em: http://localhost:8000
```

### Docker

```bash
# Build da imagem Docker
docker build -t portfolio-backend:latest .

# Executar container
docker run -p 8888:8888 \
  -e SECRET_KEY="sua_chave_secreta" \
  -e DB_HOST="seu_host_db" \
  -e DB_NAME="portfolio_db" \
  -e DB_USER="postgres" \
  -e DB_PASSWORD="senha" \
  portfolio-backend:latest

# O servidor estará disponível em: http://localhost:8888
```

### Docker Compose (Recomendado)

```bash
# Criar arquivo docker-compose.yml na raiz do projeto
docker-compose up --build

# O servidor estará em: http://localhost:8888
# PostgreSQL estará em: localhost:5432
```

---

## 📁 Estrutura de Diretórios

### Diretório `backend/`
Contém as configurações centrais do Django:
- **settings.py** - Configurações de banco de dados, apps instalados, middleware, segurança
- **urls.py** - Roteamento principal da aplicação
- **wsgi.py** - Interface WSGI para produção com Gunicorn
- **asgi.py** - Interface ASGI para produção alternativa

### Diretório `projects/`
Gerencia os projetos do portfólio:
- **models.py** - Define Project, Stack, StackProject, File
- **views.py** - APIs REST para projetos
- **urls.py** - Endpoints: `/api/projects/`, `/api/stacks/`
- **utils.py** - Funções auxiliares
- **admin.py** - Interface administrativa

### Diretório `analytics/`
Integração com Google Analytics:
- **services/** - Lógica de negócio
  - **ga_service.py** - Serviço principal de integração
  - **ga_queries.py** - Queries pré-configuradas
- **views.py** - Endpoints de analytics
- **urls.py** - Rotas: `/analytics/data/`, `/analytics/reports/`

### Diretório `contact/`
Gerenciamento de mensagens de contato:
- **models.py** - Modelo ContactMessage
- **views.py** - APIs para criar mensagens
- **urls.py** - Endpoints: `/contact/messages/`
- **admin.py** - Interface administrativa

---

## 🔌 Aplicações Django

### 1. Projects App

#### Modelos

**Project**
```python
- name_pt: CharField (nome em português)
- name_en: CharField (nome em inglês)
- summary_pt: TextField (resumo em português)
- summary_en: TextField (resumo em inglês)
- image_url: URLField (URL da imagem)
- created_at: DateTimeField (data de criação)
```

**Stack**
```python
- name: CharField (nome da stack/tecnologia)
- badge_url: URLField (URL da badge)
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
- ... (mais campos não mostrados)
```

### 2. Contact App

#### Modelos

**ContactMessage**
```python
- name: CharField (nome do remetente)
- email: EmailField (email do remetente)
- message: TextField (corpo da mensagem)
- created_at: DateTimeField (data/hora de criação)
- ip_address: GenericIPAddressField (IP do remetente)
- user_agent: TextField (User Agent do navegador)
```

### 3. Analytics App

#### Serviços

**GA Service** - Integração com Google Analytics
- Autenticação com credenciais de serviço
- Consulta de eventos e relatórios
- Cálculo de métricas de tráfego

**GA Queries** - Queries pré-configuradas
- Relatórios diários
- Relatórios mensais
- Métricas de engajamento

---

## 🔌 Endpoints da API

### Projetos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/projects/` | Listar todos os projetos |
| GET | `/api/projects/{id}/` | Obter detalhes de um projeto |
| POST | `/api/projects/` | Criar novo projeto |
| PUT | `/api/projects/{id}/` | Atualizar projeto |
| DELETE | `/api/projects/{id}/` | Deletar projeto |

### Stacks

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/stacks/` | Listar todas as stacks |
| POST | `/api/stacks/` | Criar nova stack |

### Contato

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/contact/messages/` | Listar mensagens de contato |
| POST | `/contact/messages/` | Criar nova mensagem |

### Analytics

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/analytics/data/` | Obter dados do GA |
| GET | `/analytics/reports/` | Obter relatórios do GA |

### Administração

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/admin/` | Interface administrativa do Django |

---

## 🐳 Docker

### Arquivo Dockerfile

O projeto está configurado com Docker usando Alpine Linux para imagem leve:

```dockerfile
FROM python:3.13-alpine

# Instala dependências necessárias para PostgreSQL e compilação
RUN apk add --no-cache gcc musl-dev postgresql-dev postgresql-client ...

# Copia dependências e instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia código e executa entrypoint
COPY . .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8888"]
```

### Entrypoint Script (entrypoint.sh)

O script de inicialização:
1. Aguarda disponibilidade do PostgreSQL
2. Executa migrations automáticas
3. Cria superuser se não existir
4. Inicia o servidor Gunicorn

### Build e Run

```bash
# Build
docker build -t portfolio-backend:latest .

# Run com variáveis de ambiente
docker run -p 8888:8888 -e SECRET_KEY=xyz ... portfolio-backend:latest

# Logs
docker logs -f <container_id>

# Parar container
docker stop <container_id>
```

---

## 🗄️ Banco de Dados

### PostgreSQL

O projeto utiliza PostgreSQL como banco de dados principal.

#### Configuração

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
# Criar migration após alterar modelo
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Ver status das migrations
python manage.py showmigrations
```

#### Backup

```bash
# Backup do banco de dados
pg_dump portfolio_db > backup.sql

# Restaurar backup
psql portfolio_db < backup.sql
```

---

## 🔒 Segurança

### Configurações de Segurança

1. **ALLOWED_HOSTS** - Apenas domínios confiáveis
   ```python
   ALLOWED_HOSTS = ['api.glauciofilho.com.br', 'glauciofilho.com.br', ...]
   ```

2. **CORS** - Controle de origem cruzada
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://glauciofilho.com.br",
       "https://api.glauciofilho.com.br",
   ]
   ```

3. **CSRF** - Proteção contra CSRF
   ```python
   CSRF_TRUSTED_ORIGINS = [
       "https://glauciofilho.com.br",
       "https://api.glauciofilho.com.br",
   ]
   ```

4. **DEBUG** - Deve estar `False` em produção
   ```python
   DEBUG = "False"  # Nunca True em produção
   ```

5. **SECRET_KEY** - Chave segura e única
   - Gere com: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
   - Nunca commit no repositório

6. **HTTPS** - Sempre use em produção
   ```python
   SECURE_SSL_REDIRECT = True
   SECURE_HSTS_SECONDS = 31536000
   SECURE_HSTS_INCLUDE_SUBDOMAINS = True
   SECURE_HSTS_PRELOAD = True
   ```

---

## 🔧 Middleware

A aplicação utiliza os seguintes middleware:

1. **SecurityMiddleware** - Adiciona headers de segurança HTTP
2. **WhiteNoiseMiddleware** - Serve arquivos estáticos em produção
3. **SessionMiddleware** - Gerenciamento de sessões
4. **CorsMiddleware** - Manipulação de CORS
5. **CommonMiddleware** - Funcionalidades comuns do Django
6. **CsrfViewMiddleware** - Proteção contra CSRF
7. **AuthenticationMiddleware** - Autenticação de usuários
8. **MessageMiddleware** - Framework de mensagens
9. **XFrameOptionsMiddleware** - Proteção contra clickjacking

---

## 💻 Desenvolvimento Local

### Executar Testes

```bash
# Todos os testes
python manage.py test

# Testes de um app específico
python manage.py test projects
python manage.py test contact
python manage.py test analytics

# Com cobertura de código (se coverage instalado)
coverage run --source='.' manage.py test
coverage report
coverage html  # Gera relatório HTML
```

### Shell Django

```bash
# Acessar shell do Django
python manage.py shell

# Exemplo de uso
>>> from projects.models import Project
>>> Project.objects.all()
>>> project = Project.objects.create(name_pt="Meu Projeto", ...)
```

### Criar Admin

```bash
python manage.py createsuperuser

# Acessar em: http://localhost:8000/admin
```

---

## 🔍 Debugging

### Ativar Debug Mode (Apenas Desenvolvimento)

```env
DEBUG=True
```

### Logs

Verifique arquivo `debug.log` ou configure em settings.py:

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

## 🤝 Contribuição

### Como Contribuir

1. Fork do repositório
2. Criar branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abrir Pull Request

### Padrões de Código

- Seguir PEP 8 para Python
- Adicionar testes para novas funcionalidades
- Documentar funções e classes
- Fazer commits semânticos

---

## 📝 Changelog

### Versão 1.0.0 - Abril 2026

**Inicialização do Projeto**
- ✅ Setup inicial do Django
- ✅ Configuração de banco de dados PostgreSQL
- ✅ App Projects com gerencio de portfólio
- ✅ App Contact para mensagens
- ✅ App Analytics com integração do Google Analytics
- ✅ Dockerização da aplicação
- ✅ Configuração de CORS e segurança
- ✅ Entrypoint automático com migrations

---

## 🆘 Troubleshooting

### Erro: `psycopg2 not found`

```bash
pip install psycopg2-binary
```

### Erro: `Database connection refused`

Verifique:
1. PostgreSQL está rodando
2. Variáveis de ambiente (DB_HOST, DB_PORT) estão corretas
3. Credenciais do banco de dados (DB_USER, DB_PASSWORD)

### Erro: `SECRET_KEY not set`

Defina em `.env`:
```env
SECRET_KEY=sua_chave_muito_secreta_e_longa
```

### Migração falhando

```bash
# Reset do banco (CUIDADO - apaga dados!)
python manage.py migrate analytics zero
python manage.py migrate contact zero
python manage.py migrate projects zero

# Reaplique
python manage.py migrate
```

---

## 📚 Recursos Úteis

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Google Analytics API](https://developers.google.com/analytics/devguides/reporting/data/v1)

---

## 📄 Licença

Este projeto é licenciado sob a License MIT - ver arquivo `LICENSE` para detalhes.

---

## 👨‍💻 Autor

**Glaucio Filho**  
Website: [glauciofilho.com.br](https://glauciofilho.com.br)  
Email: contato@glauciofilho.com.br

---

## 📞 Suporte

Para questões ou problemas:
1. Abra uma [Issue](https://github.com/glauciofilho/portfolio-backend/issues)
2. Verifique a seção Troubleshooting acima
3. Consulte a [Documentação do Django](https://docs.djangoproject.com/)

---

**Última atualização:** Abril de 2026  
**Versão:** 1.0.0
**Status:** ✅ Em Produção
