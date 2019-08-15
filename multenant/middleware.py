import threading

from django.shortcuts import redirect

from multenant.models import Tenant
from multenant.utils import get_tenant_name_from_request

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_name = get_tenant_name_from_request(request)

        if tenant_name != 'default':
            tenant = Tenant.objects.filter(subdomain=tenant_name).first()
            setattr(THREAD_LOCAL, "DB", tenant.subdomain)

        response = self.get_response(request)
        return response


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)


class DisallowTenantUserCrossSwitch:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and not request.user.is_superuser:
            current_tenant = get_tenant_name_from_request(request)

            if request.user.tenant.subdomain == current_tenant:
                return response
            else:
                protocol = 'https' if request.is_secure() else 'http'
                return redirect(f"{protocol}://{request.user.tenant.subdomain}.{request.META['HTTP_HOST']}/")

        return response


