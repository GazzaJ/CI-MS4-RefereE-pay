# Generated by Django 3.2.3 on 2021-08-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0010_auto_20210719_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['club_name']},
        ),
        migrations.AlterField(
            model_name='venue',
            name='postcode',
            field=models.CharField(max_length=50),
        ),
    ]
