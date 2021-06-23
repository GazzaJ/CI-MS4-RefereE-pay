# Generated by Django 3.2.3 on 2021-06-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20210621_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='asst1_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='game',
            name='asst2_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='game',
            name='ref_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]