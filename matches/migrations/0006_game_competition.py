# Generated by Django 3.2.3 on 2021-07-12 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='competition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='matches.competition'),
            preserve_default=False,
        ),
    ]
