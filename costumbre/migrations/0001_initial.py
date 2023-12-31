# Generated by Django 4.2.5 on 2023-10-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250, verbose_name='Место где нужно выполнять прывычку')),
                ('datetime', models.DateTimeField(verbose_name='Время, когда необходимо выполнять привычку')),
                ('action', models.CharField(max_length=250, verbose_name='Действие, которое представляет из себя привычка')),
                ('sign_of_a_pleasant_habit', models.CharField(max_length=150, verbose_name='Приятная привычка')),
                ('related_Habit', models.CharField(max_length=150, verbose_name='Привычка которая связана с другой, но не для приятных')),
                ('periodicity', models.CharField(max_length=100, verbose_name='Периодичность выполнения привычки для напоминания в днях.')),
                ('reward', models.CharField(max_length=250, verbose_name='Вознаграждение')),
                ('time_to_complete', models.TimeField(verbose_name='Время на выполнение')),
                ('is_active', models.BooleanField(verbose_name='Доступно ли всем?')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ('user',),
            },
        ),
    ]
