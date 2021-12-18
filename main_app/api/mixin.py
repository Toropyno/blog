from django.shortcuts import redirect
from rest_framework.decorators import action

from main_app import services


class SubscribeMixin:

    @action(methods=['post'], detail=True)
    def subscribe(self, request, pk=None):
        """
        Подписаться на пользователя
        """
        services.subscribe(from_user=request.user, to_user=self.get_object())
        return redirect(request.META['HTTP_REFERER'])

    @action(methods=['post'], detail=True)
    def unsubscribe(self, request, pk=None):
        """
        Отписаться от пользователя
        """
        services.unsubscribe(from_user=request.user, to_user=self.get_object())
        return redirect(request.META['HTTP_REFERER'])
