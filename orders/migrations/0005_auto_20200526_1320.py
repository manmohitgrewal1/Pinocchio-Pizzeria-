# Generated by Django 3.0.6 on 2020-05-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(related_name='order', to='orders.User'),
        ),
    ]
