from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscriberList)
class FollowerListAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscriptionList)
class FollowerListAdmin(admin.ModelAdmin):
    pass

