# Generated by Django 3.2.20 on 2023-09-30 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_trainer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='user',
        ),
    ]
