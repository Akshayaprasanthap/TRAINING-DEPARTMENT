# Generated by Django 3.2.20 on 2023-10-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_file_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='File_upload',
        ),
    ]