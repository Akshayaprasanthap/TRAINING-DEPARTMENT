# Generated by Django 3.2.20 on 2023-10-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20231004_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(null=True, upload_to='pdf/'),
        ),
    ]
