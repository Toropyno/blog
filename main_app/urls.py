from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('post_list/', (login_required(views.PostListView.as_view())), name='post-list'),
    path('authors/<int:pk>/', login_required(views.AuthorPageView.as_view()), name='author'),
    path('subscriptions/', login_required(views.SubscriptionPage.as_view()), name='subscriptions')
]
