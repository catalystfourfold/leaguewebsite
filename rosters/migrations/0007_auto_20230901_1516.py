# Generated by Django 3.2.20 on 2023-09-01 19:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0006_auto_20230901_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='result',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='game',
            name='opponent',
        ),
        migrations.AddField(
            model_name='game',
            name='day',
            field=models.CharField(default='Wed', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='rosters.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default='F', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='venue',
            field=models.CharField(default='Caledonia', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='visitors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='rosters.team'),
            preserve_default=False,
        ),
    ]
