from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import viewsets

from .serializers import PostSerializer, UserSerializer
from .mixin import SubscribeMixin
from ..models import Post

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        return redirect(request.META['HTTP_REFERER'])


class UserViewSet(SubscribeMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
