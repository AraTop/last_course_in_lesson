from datetime import timedelta
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class LimitTime:
   def __init__(self, field_name, max_seconds):
      self.field_name = field_name
      self.max_seconds = max_seconds

   def __call__(self, attrs):
      time_to_complete = attrs.get(self.field_name)
      now_time = timezone.now() 
      three_hours = timedelta(hours=3)
      current_time = now_time + three_hours

      hours = current_time.hour
      minutes = current_time.minute
      seconds = current_time.second

      current_time_seconds = (hours * 3600) + (minutes * 60) + seconds
      time_to_complete_seconds = (time_to_complete.hour * 3600) + (time_to_complete.minute * 60) + time_to_complete.second

      if time_to_complete_seconds - current_time_seconds > self.max_seconds:
         raise ValidationError(
            f'Поле "{self.field_name}" не может быть больше {self.max_seconds} секунд.'
         )

class RelatedHabitorReward:
   def __init__(self, related_field, reward_field):
      self.related_field = related_field
      self.reward_field = reward_field

   def __call__(self, data):
      related_value = data.get(self.related_field)
      reward_value = data.get(self.reward_field)

      if related_value and reward_value:
         raise ValidationError(
            f'Можно заполнить только одно из полей: {self.related_field} или {self.reward_field}'
         )
