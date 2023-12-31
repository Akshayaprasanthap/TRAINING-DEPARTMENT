# Generated by Django 3.2.20 on 2023-09-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Staff_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(default=1, max_length=200)),
                ('DEPARTMENT', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=200)),
                ('tplace', models.CharField(max_length=200)),
                ('tpin', models.CharField(max_length=200)),
                ('tpost', models.CharField(max_length=200)),
                ('tphn', models.CharField(max_length=200)),
                ('ttype', models.CharField(default=1, max_length=200)),
                ('gender', models.CharField(default=1, max_length=200)),
                ('pdf', models.ImageField(null=True, upload_to='pdf/')),
                ('temail', models.CharField(max_length=200)),
                ('timage', models.ImageField(null=True, upload_to='image/')),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('TRAINEE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='myapp.trainer')),
                ('TRAINER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Teacher', to='myapp.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Student_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STAFF_ALLOCATION', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.staff_allocation')),
                ('STUDENT', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer')),
            ],
        ),
        migrations.AddField(
            model_name='staff_allocation',
            name='STAFF',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer'),
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromdate', models.CharField(max_length=200)),
                ('todate', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('ltype', models.CharField(max_length=200)),
                ('FROMID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='attendencee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('FROMID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.trainer')),
            ],
        ),
    ]
