# Generated by Django 5.0.6 on 2024-05-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageelement',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
