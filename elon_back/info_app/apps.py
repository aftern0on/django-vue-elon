from django.apps import AppConfig


class InfoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info_app'

    def ready(self):
        import info_app.signals
