from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
from costumbre.models import Habits
from costumbre.paginators import HabitsPaginator
from costumbre.permissions import AuthorPermissionsMixin
from costumbre.serialization import HabitsSerializer
from rest_framework import generics
from project import settings
from users.models import User


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


def SendMessageView(request, user_id, chat_id):
    user = User.objects.get(id=user_id)

    if not user_id or not chat_id:
        return HttpResponse("error: user_id or chat_id is missing")

    habit = Habits.objects.filter(user_id=user.pk).first()
    text = f"Здравствуйте {user.first_name}. Я буду {habit.action} в {habit.time_complete} в {habit.place}"
    token = settings.BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url).json()
    return HttpResponse('Message sent successfully.')
