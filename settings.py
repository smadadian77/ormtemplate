# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sajjad_test',
        'USER': 'postgres',
        'PASSWORD': 'Ms121633',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'mytestapp',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
