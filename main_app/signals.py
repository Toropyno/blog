from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models import signals

from main_app.models import SubscriberList, SubscriptionList

User = get_user_model()


@receiver(signal=signals.post_save, sender=User)
def new_user(**kwargs):
    user = kwargs.get('instance')
    SubscriberList.objects.get_or_create(user=user)
    SubscriptionList.objects.get_or_create(user=user)


# @receiver(signal=signals.m2m_changed, sender=SubscriberList.subscribers.through)
# def new_sub(**kwargs):
#     print(kwargs)
