from django.conf import settings
from django.core.management import call_command
from django.db import models, connections
from django.db.models.signals import post_save

from multenant.drivers.redis import rset
from multenant.drivers.utils import create_database
from multenant.utils import uuid_random_string, get_tenant_databases


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255, unique=True)
    unique_key = models.CharField(max_length=255, blank=True, editable=False)

    def __str__(self):
        return self.name

    @property
    def database(self):
        return f"multenant_{self.unique_key}"

    def save(self, *args, **kwargs):
        self.unique_key = uuid_random_string()
        super().save(*args, **kwargs)


def create_tenant_database(sender, instance, created, **kwargs):
    # create database for correspondingly to database engine
    create_database(settings.DATABASES['default'], instance.database)

    # gather all tenant database names in a List
    database_settings = get_tenant_databases()
    database_settings[instance.subdomain] = settings.DATABASES['default']
    database_settings[instance.subdomain]["NAME"] = instance.database

    settings.DATABASES = database_settings
    connections.databases = database_settings

    call_command('migrate', database=instance.subdomain)
    rset(instance.subdomain, settings.DATABASES[instance.subdomain])


post_save.connect(create_tenant_database, sender=Tenant)
