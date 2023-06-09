# Generated by Django 3.2 on 2023-04-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
