# Generated by Django 3.2.18 on 2023-10-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_trainer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pdf',
            field=models.ImageField(null=True, upload_to='pdf/'),
        ),
    ]