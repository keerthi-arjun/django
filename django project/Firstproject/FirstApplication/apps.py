from django.apps import AppConfig


class FirstApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FirstApplication'

    def ready(self):
        
        from FirstApplication.models import Name, ID, Contact, Address
