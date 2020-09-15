from django.apps import AppConfig


class ApplicationuserConfig(AppConfig):
    name = 'applicationUser'

    def ready(self):
        import applicationUser.signals
