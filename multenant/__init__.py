from django.conf import settings
from django.db import connections

from .utils import get_tenant_databases

routers = settings.DATABASE_ROUTERS
tenant_settings = settings.TENANT_SETTINGS
tenant_apps = settings.TENANT_APPS

apps_prefix = settings.TENANT_SETTINGS['apps_folder']
redis = settings.TENANT_SETTINGS['redis']

settings.DATABASES = get_tenant_databases()
connections.databases = get_tenant_databases()
