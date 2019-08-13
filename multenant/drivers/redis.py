import json

import redis
from django.conf import settings

rds = redis.Redis(
    host=settings.TENANT_SETTINGS['redis']['host'],
    port=settings.TENANT_SETTINGS['redis']['port'],
    password=settings.TENANT_SETTINGS['redis']['password']
)


def rget(key, default=False):
    data = rds.get(f"multitenant:{key}")
    return json.loads(data) if data else default


def rset(key, value):
    return rds.set(f"multitenant:{key}", json.dumps(value))


def rdelete(key):
    return rds.delete(f"multitenant:{key}")


def rget_all_keys():
    keys = []
    for key in rds.scan_iter("multitenant:*"):
        keys.append(key.decode('utf-8').split(':')[1])
    return keys
