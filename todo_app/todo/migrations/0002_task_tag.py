# Generated by Django 2.2 on 2019-04-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
