from django.db.models import Q
from django.contrib.auth.models import UserManager, User


class CustomUserManager(UserManager):
    def search(self, query):
        lookup = Q(User__first_name=query) | Q(User__last_name=query)
        return self.get_queryset().filter(lookup).distinct()


class UserModel(User):
    objects = CustomUserManager()
