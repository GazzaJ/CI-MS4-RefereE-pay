# Generated by Django 3.2.3 on 2021-07-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_remove_fee_nonpayment_fine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp', models.CharField(max_length=100)),
            ],
        ),
    ]
