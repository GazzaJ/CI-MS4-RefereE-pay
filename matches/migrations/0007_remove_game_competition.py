# Generated by Django 3.2.3 on 2021-07-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_game_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='competition',
        ),
    ]