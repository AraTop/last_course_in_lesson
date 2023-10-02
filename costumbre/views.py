from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from costumbre.models import Habits

@method_decorator(login_required, name='dispatch')
class HabitsCreateView(CreateView):
   model = Habits
   fields = ('user', 'place', 'datetime', 'action', 'sign_of_a_pleasant_habit', 'related_Habit', 'periodicity', 'reward', 'time_to_complete', 'is_active')
   success_url = '/#/'
   template_name = 'costumbre/habits_create.html'

@method_decorator(login_required, name='dispatch')
class HabitsDeleteView(DeleteView):
   model = Habits
   success_url = '/#/' 
   template_name = 'costumbre/habits_delete.html'
   
@method_decorator(login_required, name='dispatch')
class HabitsListView(ListView):
   model = Habits
   template_name = 'costumbre/habits_list.html'

@method_decorator(login_required, name='dispatch')
class HabitsUpdateView(UpdateView):
   model = Habits
   fields = ('user', 'place', 'datetime', 'action', 'sign_of_a_pleasant_habit', 'related_Habit', 'periodicity', 'reward', 'time_to_complete', 'is_active')
   success_url = '/#/'
   template_name = 'costumbre/habits_edit.html'

@method_decorator(login_required, name='dispatch')
class HabitsDetailView(DetailView):
   model = Habits
   template_name = 'costumbre/habits_detail.html'