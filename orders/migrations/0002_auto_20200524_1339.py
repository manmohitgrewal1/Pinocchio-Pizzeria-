# Generated by Django 3.0.6 on 2020-05-24 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(related_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]
