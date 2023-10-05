from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null':True, 'blank':True}

class User(AbstractUser):
   username = None
   email = models.EmailField(unique=True, verbose_name='Почта')

   chat_id = models.BigIntegerField(unique=True, **NULLABLE)
   first_name = models.CharField(max_length=150, verbose_name='Имя')
   last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
   surname = models.CharField(max_length=200, verbose_name='Отчествоо', **NULLABLE)

   
   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = [chat_id]
