# Generated by Django 3.2.20 on 2023-10-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20231005_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]