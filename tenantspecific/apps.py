from django.apps import AppConfig


class TenantspecificConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenantspecific'
