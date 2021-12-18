from main_app.models import SubscriberList, SubscriptionList


def get_subscribers(user):
    """
    Возвращает подписчиков пользователя user
    """
    subscriber_list = get_subscriber_list(user)
    return subscriber_list.subscribers.all()


def get_subscriptions(user):
    """
    Возвращает подписки пользователя user
    """
    subscription_list = get_subscription_list(user)
    return subscription_list.subscriptions.all()


def get_subscriber_list(user):
    """
    Возвращает список подписчиков (объект) пользователя user
    """
    subscriber_list, created = SubscriberList.objects.get_or_create(user=user)
    return subscriber_list


def get_subscription_list(user):
    """
    Возвращает список подписок (объект) пользователя user
    """
    subscription_list, created = SubscriptionList.objects.get_or_create(user=user)
    return subscription_list


def subscribe(from_user, to_user):
    """
    Подписывает пользователя from_user на пользователя to_user
    """
    subscription_list = get_subscription_list(from_user)
    subscription_list.subscriptions.add(to_user)

    subscriber_list = get_subscriber_list(to_user)
    subscriber_list.subscribers.add(from_user)


def unsubscribe(from_user, to_user):
    """
    Отписывает пользователя from_user от пользователя to_user
    """
    subscription_list = get_subscription_list(from_user)
    subscription_list.subscriptions.remove(to_user)

    subscriber_list = get_subscriber_list(to_user)
    subscriber_list.subscribers.remove(from_user)


def is_subscription(from_user, to_user):
    """
    Проверяет подписан ли пользователь from_user на пользователя to_user
    """
    subscription_list = get_subscription_list(from_user)
    return to_user in subscription_list.subscriptions.all()
