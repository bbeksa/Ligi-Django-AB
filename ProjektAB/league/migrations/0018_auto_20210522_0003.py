# Generated by Django 3.1.7 on 2021-05-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0017_auto_20210522_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sezon',
            name='begin_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sezon',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]