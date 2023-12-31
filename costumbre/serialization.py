from rest_framework import serializers
from .models import Habits
from .validators import LimitHabits, LimitTime, Limitdays, RelatedHabitorReward


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = ('user', 'place', 'datetime', 'action', 'sign_of_a_pleasant_habit', 'related_Habit', 'periodicity',
                  'reward', 'time_complete', 'is_active')
        validators = [
         LimitTime(field_name='time_complete', max_seconds=120),
         RelatedHabitorReward(related_field='related_Habit', reward_field='reward'),
         Limitdays(field_name='periodicity', max_days=7),
         LimitHabits(field_name_1='sign_of_a_pleasant_habit', field_name_2='reward', field_name_3='related_Habit')
                     ]
