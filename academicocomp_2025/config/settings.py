import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta do Django (alterar para algo mais seguro em produção)
SECRET_KEY = 'django-insecure-8l8o(-2su$6t%k424293i#x672q0$*^itfyi9r32$8j-igo7zf'

# Ativar ou desativar o modo de depuração
DEBUG = True

# Hosts permitidos (adicionar domínios e IPs em produção)
ALLOWED_HOSTS = []

# Aplicações instaladas no Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', 
     'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap4"]
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Middleware que processa as requisições
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Corrigido: 'SssionMiddleware' estava errado
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivo de URLs principal do projeto
ROOT_URLCONF = 'config.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app/templates'),  # Diretório onde os templates são armazenados
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicação WSGI para o projeto
WSGI_APPLICATION = 'config.wsgi.application'

# Configuração do banco de dados (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'academicocomp',  # Nome do banco de dados
        'USER': 'postgres',      # Nome de usuário do banco de dados
        'PASSWORD': '123456',    # Senha do banco de dados
        'HOST': 'localhost',     # Servidor do banco de dados
        'PORT': '5432',          # Porta padrão do PostgreSQL
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Definindo idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Configurações de internacionalização
USE_I18N = True
USE_TZ = True

# Configuração para arquivos estáticos
STATIC_URL = 'static/'

# Caminho absoluto para os arquivos estáticos coletados
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Corrigido o caminho de STATIC_ROOT

# Diretórios adicionais para procurar arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app/static/"),  # Pasta estática dentro do diretório da aplicação
]

# Definindo o tipo padrão de auto campo para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
