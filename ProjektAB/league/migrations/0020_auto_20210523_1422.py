# Generated by Django 3.1.7 on 2021-05-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0019_player_player_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_Img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
