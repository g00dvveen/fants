from django.contrib import admin
from .models import TelegramUsers, Tasks


# Register your models here.
admin.site.register(TelegramUsers)
admin.site.register(Tasks)
