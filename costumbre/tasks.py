from celery import shared_task
from django.urls import reverse
import requests
import telegram
from project import settings

@shared_task
def send_message_bot(request):
   url = reverse('send_message')
   response = requests.post(url)

   if response.status_code == 200:
      print('Сообщение успешно отправлено.')
   else:
      print('Произошла ошибка при отправке сообщения.')

@shared_task
def delay_message_bot(chat_id, message):
   bot = telegram.Bot(token=settings.TOKEN)
   bot.send_message(chat_id=chat_id, text=message)
