import random
import string
import uuid

from django.conf import settings

from multitenant.drivers.redis import rget, rset, rget_all_keys


def uuid_random_string(length=16):
    random_string_ = uuid.uuid4().hex
    random_string_ = random_string_.lower()[0:length]
    return random_string_


def get_tenant_name_from_request(request):
    hostname = request.get_host().split(':')[0].lower()
    hostname_parts = hostname.split('.')

    if len(hostname_parts) > 2:
        return f"{hostname_parts[0]}"
    else:
        return 'default'


def get_tenant_databases():
    if not rget('default'):
        rset('default', settings.DATABASES['default'])

    all_records = rget_all_keys()

    dbs = {}
    for record in all_records:
        dbs[record] = rget(record)

    return dbs
