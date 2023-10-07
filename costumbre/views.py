from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from costumbre.models import Habits
from costumbre.paginators import HabitsPaginator
from costumbre.permissions import AuthorPermissionsMixin
from costumbre.serialization import HabitsSerializer
from rest_framework import generics
from costumbre.tasks import delay_message_bot

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

@method_decorator(login_required, name='dispatch')
class SendMessageView(View):
   def get(self, request, *args, **kwargs):
      user = request.user
      chat_id = user.chat_id
      if not chat_id:
         return "error: chat_id"
      
      message = f"Здравствуйте {user.first_name}, пришло время выполнять привычки."
      delay_message_bot.delay(chat_id=chat_id, message=message)

      return HttpResponse('Message sent successfully.')