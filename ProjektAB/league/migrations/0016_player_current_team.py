# Generated by Django 3.1.7 on 2021-05-21 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0015_auto_20210521_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_team', to='league.team'),
        ),
    ]
