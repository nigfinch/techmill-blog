from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "techmill_blog.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import techmill_blog.users.signals  # noqa F401
        except ImportError:
            pass
