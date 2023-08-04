from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    Configuration class for the 'polls' app.

    Attributes:
        default_auto_field (str): Auto-generated primary key field.
        name (str): The name of the app ('polls' in this case).
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
