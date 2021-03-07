from django.db import models
import uuid


# Create your models here.
class TelegramUsers(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    SEX_TYPES = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )
    sex = models.CharField(max_length=16, choices=SEX_TYPES, null=True)
    partner_name = models.CharField(max_length=200, null=True)
    LEVELS = (
        ('green', 'Зеленый'),
        ('yellow', 'Желтый'),
        ('red', 'Красный'),
    )
    level = models.CharField(max_length=16, choices=LEVELS, null=True)
    current_task = models.IntegerField(null=True)


class Tasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    LEVELS = (
        ('green', 'Зеленый'),
        ('yellow', 'Желтый'),
        ('red', 'Красный'),
    )
    level = models.CharField(max_length=16, choices=LEVELS, null=True)
    image = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    SEX_TYPES = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )
    sex = models.CharField(max_length=16, choices=SEX_TYPES, null=True)
    SECTIONS = (
        ('oral', 'Оральный секс'),
        ('anal', 'Анальный секс'),
        ('classical', 'Классический секс'),
        ('bdsm', 'БДСМ'),
        ('finishing', 'Окончание'),
        ('toys', 'Секс игрушки'),
        ('domination', 'Доминирование'),
        ('fetish', 'Фетиш'),
    )
    section = models.CharField(max_length=32, choices=SECTIONS, null=True)
    deferred = models.BooleanField(default=False)
