from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django.db.models import Q
from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.GET.get('search')
        lookup = Q(first_name=query) | Q(last_name=query)
        return get_user_model().objects.filter(lookup)
