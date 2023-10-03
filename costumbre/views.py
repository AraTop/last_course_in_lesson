from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from costumbre.models import Habits
from costumbre.paginators import HabitsPaginator
from costumbre.permissions import AuthorPermissionsMixin
from costumbre.serialization import HabitsSerializer
from rest_framework import generics

@method_decorator(login_required, name='dispatch')
class HabitsCreateView(generics.CreateAPIView):
   serializer_class = HabitsSerializer

@method_decorator(login_required, name='dispatch')
class HabitsDeleteView(AuthorPermissionsMixin, generics.DestroyAPIView):
   queryset = Habits.objects.all()
   
@method_decorator(login_required, name='dispatch')
class HabitsListView(generics.ListAPIView):
   serializer_class = HabitsSerializer
   queryset = Habits.objects.all()
   pagination_class = HabitsPaginator

@method_decorator(login_required, name='dispatch')
class HabitsUpdateView(AuthorPermissionsMixin, generics.UpdateAPIView):
   serializer_class = HabitsSerializer
   queryset = Habits.objects.all()

@method_decorator(login_required, name='dispatch')
class HabitsDetailView(generics.RetrieveAPIView):
   serializer_class = HabitsSerializer
   queryset = Habits.objects.all()