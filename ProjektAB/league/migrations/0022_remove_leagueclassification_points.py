# Generated by Django 3.1.7 on 2021-05-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0021_auto_20210523_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leagueclassification',
            name='points',
        ),
    ]
