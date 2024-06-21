from rest_framework import viewsets
from app.models import User
from app.serializer import User_Serializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

    @method_decorator(cache_page(60*1))        ## Caching page for faster response, 60*1=60 seconds = 60 sec caching.
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
