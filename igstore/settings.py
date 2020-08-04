import os
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'gco!g9rbt*9kom_5#1*8zr3con=qf!4z+%u25i!5504(b$1vhr'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Системные и установленные:
    'grappelli',
    'treewidget',
    'django_summernote',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    # Приложения:
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'home.apps.HomeConfig',
    'instagram.apps.InstagramConfig',
    'reviews.apps.ReviewAppConfig',
    'orders.apps.OrdersConfig',
    'emails.apps.EmailsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'igstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'igstore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
# ID сессии корзины:
CART_SESSION_ID = 'cart'
# Настройки языковой зоны:
LANGUAGE_CODE = 'ru-RU'

# Настройки временной зоны:
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_FORMAT = 'd E Y'

# Настройки директорий для статикфайлов:
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static", "static_dev"),)
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_prod")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "neformatinc@gmail.com"
EMAIL_HOST_PASSWORD = "rarara111"
EMAIL_USE_TLS = True

FROM_EMAIL = "neformatinc@gmail.com"
EMAIL_ADMIN = "neformatinc@gmail.com"
