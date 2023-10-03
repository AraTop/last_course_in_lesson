# Generated by Django 4.2.5 on 2023-10-03 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('costumbre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habits',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Habits', to=settings.AUTH_USER_MODEL),
        ),
    ]