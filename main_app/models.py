from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Запись')
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Контент', max_length=3000)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.author.get_full_name()}: {self.title}'


class SubscriberList(models.Model):
    """
    Список подписчиков пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='subscribers')
    subscribers = models.ManyToManyField(User, verbose_name='Читатели')

    class Meta:
        verbose_name = 'Список читателей'
        verbose_name_plural = 'Списки читателей'

    def __str__(self):
        return f'Читатели пользователя: {self.user.username}'


class SubscriptionList(models.Model):
    """
    Список подписок пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                                related_name='subscriptions')
    subscriptions = models.ManyToManyField(User, verbose_name='Читатели', blank=True)

    class Meta:
        verbose_name = 'Список подписок'
        verbose_name_plural = 'Списки подписок'

    def __str__(self):
        return f'Подписки пользователя: {self.user.username}'
