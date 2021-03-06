# Generated by Django 3.1.7 on 2021-05-20 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_auto_20210520_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='team',
        ),
        migrations.RemoveField(
            model_name='player',
            name='role',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='adc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adc', to='league.player'),
        ),
        migrations.AddField(
            model_name='team',
            name='jung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jung', to='league.player'),
        ),
        migrations.AddField(
            model_name='team',
            name='mid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mid', to='league.player'),
        ),
        migrations.AddField(
            model_name='team',
            name='supp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supp', to='league.player'),
        ),
        migrations.AddField(
            model_name='team',
            name='top',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top', to='league.player'),
        ),
        migrations.CreateModel(
            name='Team_Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.coach')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.team')),
            ],
        ),
    ]
