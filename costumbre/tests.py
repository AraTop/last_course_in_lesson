import datetime
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Habits
from rest_framework.test import APIClient


class HabitsCRUDAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='lololohka057@gmail.com',
            is_superuser=True,
            is_staff=True,
            is_active=True
                )
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='lololohka057@gmail.com', password='12345')
        # response_data = json.loads(response.content)
        # self.access_token = response_data.get('access')

    def test_create_habit(self):
        new_habit_data = {
            'user': self.user.pk,
            'place': 'test',
            'datetime': datetime.time(),
            'action': 'test',
            'sign_of_a_pleasant_habit': 'test',
            'periodicity': 1,
            'time_complete': 2,
            'is_active': True
        }
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('costumbre:create_habits'), data=new_habit_data)
        self.habit = Habits.objects.get(user_id=self.user.pk)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_habits(self):
        new_habit_data = {
            'user': self.user.pk,
            'place': 'test',
            'datetime': datetime.time(),
            'action': 'test',
            'sign_of_a_pleasant_habit': 'test',
            'periodicity': 1,
            'time_complete': 2,
            'is_active': True
        }
        response = self.client.post(reverse('costumbre:create_habits'), data=new_habit_data)
        habit = Habits.objects.get(user_id=self.user.pk)
        response = self.client.get(reverse('costumbre:detail_habits', args=[habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        new_habit_data = {
            'user': self.user.pk,
            'place': 'test',
            'datetime': datetime.time(),
            'action': 'test',
            'sign_of_a_pleasant_habit': 'test',
            'periodicity': 1,
            'time_complete': 2,
            'is_active': True
        }
        updated_habit_data = {
            'user': self.user.pk,
            'place': 'test_1',
            'datetime': datetime.time(),
            'action': 'test_1',
            'sign_of_a_pleasant_habit': 'test_1',
            'periodicity': 1,
            'time_complete': 2,
            'is_active': True
        }
        response = self.client.post(reverse('costumbre:create_habits'), data=new_habit_data)
        habit = Habits.objects.get(user_id=self.user.pk)
        response = self.client.put(reverse('costumbre:update_habits', args=[habit.id]), data=updated_habit_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        new_habit_data = {
            'user': self.user.pk,
            'place': 'test',
            'datetime': datetime.time(),
            'action': 'test',
            'sign_of_a_pleasant_habit': 'test',
            'periodicity': 1,
            'time_complete': 2,
            'is_active': True
        }
        response = self.client.post(reverse('costumbre:create_habits'), data=new_habit_data)
        habit = Habits.objects.get(user_id=self.user.pk)
        response = self.client.delete(reverse('costumbre:delete_habits', args=[habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
