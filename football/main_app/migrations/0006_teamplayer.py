# Generated by Django 3.2 on 2023-04-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20230410_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.ManyToManyField(to='main_app.Player')),
                ('team', models.ManyToManyField(to='main_app.Team')),
            ],
        ),
    ]