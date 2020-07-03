# Generated by Django 3.0.6 on 2020-05-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200527_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('large', models.FloatField(max_length=20)),
                ('small', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('large', models.FloatField(max_length=20)),
                ('small', models.FloatField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.ManyToManyField(blank=True, to='orders.SubTopping'),
        ),
    ]
