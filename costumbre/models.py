from django.db import models
from users.models import User

NULLABLE = {'null':True, 'blank':True}

class Habits(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Habits')
   place = models.CharField(max_length=250, verbose_name='Место где нужно выполнять прывычку')
   datetime = models.TimeField(verbose_name='Время, когда необходимо выполнять привычку')
   action = models.CharField(max_length=250, verbose_name='Действие, которое представляет из себя привычка')
   sign_of_a_pleasant_habit = models.CharField(max_length=150, verbose_name='Приятная привычка')
   related_Habit = models.CharField(max_length=150, verbose_name='Привычка которая связана с другой, но не для приятных', **NULLABLE)
   periodicity = models.CharField(max_length=100, verbose_name='Периодичность выполнения привычки для напоминания в днях.')
   reward = models.CharField(max_length=250, verbose_name='Вознаграждение', **NULLABLE)
   time_to_complete = models.TimeField(verbose_name='Время на выполнение')
   is_active = models.BooleanField(verbose_name='Доступно ли всем?')
   
   def __str__(self):
      return f'{self.user} {self.action} {self.datetime} {self.place}' 
   
   class Meta:
      verbose_name = 'Привычка'
      verbose_name_plural = 'Привычки'
      ordering = ('user',)
