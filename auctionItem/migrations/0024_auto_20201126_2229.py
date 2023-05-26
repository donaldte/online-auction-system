# Generated by Django 3.1.3 on 2020-11-26 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0023_auto_20201126_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=1000)),
                ('lot_id', models.IntegerField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=1000)),
                ('lot_id', models.IntegerField()),
                ('Wishlisted_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 22, 29, 27, 655764)),
        ),
    ]
