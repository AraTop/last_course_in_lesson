# Generated by Django 4.2.5 on 2023-10-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumbre', '0007_alter_habits_is_active_alter_habits_time_to_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='habits',
            name='time_complete',
            field=models.IntegerField(default=1, verbose_name='Время на выполнение в минутах'),
            preserve_default=False,
        ),
    ]
