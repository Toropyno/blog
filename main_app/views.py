from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, View, DetailView

from main_app.models import Post
from . import services

User = get_user_model()


class IndexView(TemplateView):
    """
    Ваш блог

    Страница управления вашим блогом (записи, подписки, подписчики)
    """
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['posts'] = user.post_set.all()
        context['subscribers'] = services.get_subscribers(user)
        context['subscriptions'] = services.get_subscriptions(user)
        context['title'] = 'Ваш блог'
        return context


class AuthorPageView(View):
    """
    Блог другого автора
    """
    model = User
    template_name = 'main_app/author_page.html'

    def get(self, request, pk):
        if pk == self.request.user.pk:
            return redirect(reverse('index'))
        context = self.get_context_data(request, pk)
        return render(request, self.template_name, context)

    def get_context_data(self, request, pk):
        context = {}
        author = User.objects.get(pk=pk)
        context['author'] = author
        context['posts'] = author.post_set.all()
        context['subscribers'] = services.get_subscribers(author)
        context['subscriptions'] = services.get_subscriptions(author)
        context['is_subscription'] = services.is_subscription(self.request.user, author)
        context['title'] = f'Блог {author.get_full_name()}'
        return context


class PostListView(TemplateView):
    """
    Записи других авторов

    Лента состоящая из последних записей случайных пользователей
    """
    template_name = 'main_app/post_list_other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_post_list(self.request.user)
        context['title'] = 'Другие авторы'
        return context

    @staticmethod
    def get_post_list(user):
        """
        Получает список записей всех пользователей кроме: user и его подписок
        """
        subscriptions = services.get_subscriptions(user)
        users = User.objects.exclude(Q(pk=user.pk) | Q(post__isnull=True) | Q(pk__in=subscriptions))
        posts = [u.post_set.last() for u in users]
        return posts


class SubscriptionPage(TemplateView):
    """
    Записи по подпискам пользователя

    Лента записей от авторов, на которых подписан пользователь
    """
    template_name = 'main_app/post_list_sub.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_post_list(self.request.user)
        context['title'] = 'Подписки'
        context['subscriptions'] = services.get_subscriptions(self.request.user)
        return context

    @staticmethod
    def get_post_list(user):
        """
        Возвращает записи авторов, на которых подписан пользователь user
        """
        subscriptions = services.get_subscriptions(user)
        return Post.objects.filter(author__in=subscriptions).order_by('-pub_date')
