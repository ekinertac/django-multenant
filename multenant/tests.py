from django.test import TestCase

from multenant.models import Tenant


class TestTenantCase(TestCase):
    def test_tenant_creation(self):
        tenant = Tenant.objects.create(
            name='thor',
            subdomain='thor'
        )

        self.assertEqual('thor', tenant.name)
        self.assertEqual('thor', tenant.subdomain)

