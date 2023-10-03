from rest_framework import serializers

from .models import Habits
from .validators import LimitTime, RelatedHabitorReward

class HabitsSerializer(serializers.ModelSerializer):

   class Meta:
      model = Habits 
      fields = '__all__'
      validators = [
         LimitTime(field_name='time_to_complete', max_seconds=120),
         RelatedHabitorReward(related_field='related_Habit', reward_field='reward')
      ]
   
   