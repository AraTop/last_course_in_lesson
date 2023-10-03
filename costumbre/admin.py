from django.contrib import admin
from costumbre.models import Habits

@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
   list_display = ('user', 'place', 'datetime', 'action', 'sign_of_a_pleasant_habit', 'related_Habit', 'periodicity', 'reward', 'time_to_complete', 'is_active')