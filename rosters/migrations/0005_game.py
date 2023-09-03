# Generated by Django 3.2.20 on 2023-09-01 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0004_auto_20230831_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_played', models.DateField()),
                ('result', models.CharField(choices=[('win', 'Win'), ('loss', 'Loss'), ('tie', 'Tie')], max_length=10)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='rosters.team')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rosters.division')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='rosters.team')),
            ],
        ),
    ]
