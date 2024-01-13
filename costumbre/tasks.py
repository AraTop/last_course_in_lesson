import datetime
from celery import shared_task
import requests
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
        if not chat_id:
                continue
        
        habits = Habits.objects.filter(user_id=user.pk)

        for habit in habits:
            time = habit.datetime
            print(habit.next_repost)

            if habit.next_repost is None:
                habit.next_repost = current_date + datetime.timedelta(days=habit.periodicity + 1)
                habit.save()

            if not habit.next_repost == current_date:
                continue

            if not time.hour == current_time.hour and time.minute == current_time.minute:
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
def test_bot():
    users = User.objects.all()

    for user in users:
        chat_id = user.chat_id
        habit = Habits.objects.filter(user_id=user.pk).first()
        if habit:

            text = f"Здравствуйте {user.first_name}. Я буду {habit.action} в {habit.time_complete} в {habit.place}"
            token = settings.BOT_TOKEN
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
            requests.get(url).json()
