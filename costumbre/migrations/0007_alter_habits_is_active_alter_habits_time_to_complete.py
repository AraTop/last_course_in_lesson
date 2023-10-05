# Generated by Django 4.2.5 on 2023-10-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumbre', '0006_alter_habits_sign_of_a_pleasant_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='is_active',
            field=models.BooleanField(verbose_name='Доступно ли всем'),
        ),
        migrations.AlterField(
            model_name='habits',
            name='time_to_complete',
            field=models.TimeField(verbose_name='Время на выполнение  в минутах'),
        ),
    ]