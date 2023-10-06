import datetime
from celery import shared_task
from django.urls import reverse
import requests
import telegram
from costumbre.models import Habits
from project import settings

@shared_task
def send_message_bot(request):
   current_time = datetime.datetime.now().time()
   current_date = datetime.date.today()
   user = request.user
   chat_id = user.chat_id
   habits = Habits.objects.filter(user_id=user.pk) 

   for habit in habits:
      time = habit.datetime

      if habit.next_repost == None:
         habit.next_repost = current_date + datetime.timedelta(days=habit.periodicity + 1)
         habit.save()

      if not habit.next_repost == current_date:
         return

      if not chat_id:
         return
      
      if not time == current_time:
         return
      
      url = reverse('send_message')
      response = requests.post(url)

      if response.status_code == 200:
         print('Сообщение успешно отправлено.')
      else:
         print('Произошла ошибка при отправке сообщения.')

      habit.next_repost = current_date + datetime.timedelta(days=habit.periodicity + 1)
      habit.save()

@shared_task
def delay_message_bot(chat_id, message):
   bot = telegram.Bot(token=settings.TOKEN)
   bot.send_message(chat_id=chat_id, text=message)