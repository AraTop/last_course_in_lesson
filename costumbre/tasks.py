import datetime
from celery import shared_task
from django.urls import reverse
import requests
import telegram
from costumbre.models import Habits
from project import settings
from users.models import User


@shared_task
def send_message_bot():
    current_time = datetime.datetime.now().time()
    current_date = datetime.date.today()
    users = User.objects.all()
    print(users)

    for user in users:
        chat_id = user.chat_id
        habits = Habits.objects.filter(user_id=user.pk)

        for habit in habits:
            time = habit.datetime
            print(habit.next_repost)

            if habit.next_repost is None:
                habit.next_repost = current_date + datetime.timedelta(days=habit.periodicity + 1)
                habit.save()

            if not habit.next_repost == current_date:
                continue

            if not chat_id:
                print("user")
                continue

            if not time.hour == current_time.hour and time.minute == current_time.minute:
                print("user")
                continue

            user_id = user.pk
            url = F'http://127.0.0.1:8000/costumbre/send_message/{user_id}/{chat_id}/'
            response = requests.get(url)

            if response.status_code == 200:
                print('Сообщение успешно отправлено.')
            else:
                print('Произошла ошибка при отправке сообщения.')

            print(response.status_code)

            habit.next_repost = current_date + datetime.timedelta(days=habit.periodicity + 1)
            habit.save()


@shared_task
def delay_message_bot(chat_id, message):
    bot = telegram.Bot(token=settings.BOT_TOKEN)
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print(chat_id, message)
    except Exception as e:
        print(f"error: {e}")
