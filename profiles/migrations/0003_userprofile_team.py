# Generated by Django 3.2.3 on 2021-08-19 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0011_auto_20210819_1215'),
        ('profiles', '0002_auto_20210708_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.team'),
        ),
    ]
