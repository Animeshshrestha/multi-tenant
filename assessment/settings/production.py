import environ

from .base import *

env = environ.Env()
env.read_env(env.str("BASE_DIR", ".envs/.production/.django.env"))

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "tenant_schemas.postgresql_backend",
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASS"),
        "NAME": env("DATABASE_NAME"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}
