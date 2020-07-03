# Generated by Django 3.0.6 on 2020-05-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200527_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'Pending'), ('C', 'Confirmed')], max_length=1),
        ),
    ]
