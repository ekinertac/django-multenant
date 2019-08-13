from django.apps import apps
from django.conf import settings

from multitenant.middleware import get_current_db_name


class TenantDatabaseRouter(object):

    def get_app_label_with_prefix(self, model):
        prefix = settings.TENANT_SETTINGS['apps_folder']
        app_name = f"{prefix}.{model._meta.app_label}"
        return app_name

    def db_for_read(self, model, **hints):
        app_name = self.get_app_label_with_prefix(model)
        if app_name in settings.TENANT_APPS:
            return get_current_db_name()

        return None

    def db_for_write(self, model, **hints):
        app_name = self.get_app_label_with_prefix(model)
        if app_name in settings.TENANT_APPS:
            return get_current_db_name()

        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
