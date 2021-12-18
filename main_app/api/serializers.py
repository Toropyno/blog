from django.contrib.auth import get_user_model
from rest_framework import serializers

from main_app.models import Post
from main_app.services import is_subscription


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'content',
        ]


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'url',
        ]
