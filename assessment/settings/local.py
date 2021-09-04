import environ

from .base import *

env = environ.Env()
env.read_env(env.str("BASE_DIR", ".envs/.local/.django.env"))

SECRET_KEY = env("SECRET_KEY")
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
