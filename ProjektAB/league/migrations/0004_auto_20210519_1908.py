# Generated by Django 3.1.7 on 2021-05-19 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_coach_nick'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nationality',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='nick',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
