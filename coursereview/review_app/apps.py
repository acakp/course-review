from django.apps import AppConfig


class ReviewAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "review_app"

    def ready(self):
        import review_app.signals
