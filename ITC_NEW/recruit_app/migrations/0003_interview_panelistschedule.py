# Generated by Django 3.1 on 2021-03-09 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruit_app', '0002_panelist_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PanelistSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Available_from', models.DateTimeField()),
                ('Available_till', models.DateTimeField()),
                ('Panelname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.panelist')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interview_time', models.DateTimeField()),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.candidate')),
                ('Panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit_app.panelist')),
            ],
        ),
    ]
