# Generated by Django 4.2.5 on 2023-10-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
