from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)
class Department(models.Model):
    department_name=models.CharField(max_length=200)

class Trainer(models.Model):
    tname=models.CharField(max_length=200)
    tplace=models.CharField(max_length=200)
    tpin=models.CharField(max_length=200)
    tpost=models.CharField(max_length=200)
    tphn=models.CharField(max_length=200)
    ttype=models.CharField(max_length=200,default=1)
    gender=models.CharField(max_length=200, default=1)
    pdf=models.ImageField(upload_to="pdf/", null=True)
    temail=models.CharField(max_length=200)
    # email=models.CharField(max_length=200)
    timage=models.ImageField(upload_to="image/", null=True)
    LOGIN=models.ForeignKey(Login,default=1,on_delete=models.CASCADE)
    DEPARTMENT=models.ForeignKey(Department,default=1,on_delete=models.CASCADE)
    # user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)

class leave(models.Model):
    FROMID=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=200)
    todate=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    ltype=models.CharField(max_length=200)

class Staff_allocation(models.Model):
    DEPARTMENT=models.ForeignKey(Department,default=1,on_delete=models.CASCADE)
    STAFF=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE)
    capacity=models.CharField(max_length=200,default=1)
class Student_allocation(models.Model):
    STAFF_ALLOCATION=models.ForeignKey(Staff_allocation,on_delete=models.CASCADE,default=1)
    STUDENT=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE)
class attendencee(models.Model):
    FROMID=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE)
    typee=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    
class Task(models.Model):
    TRAINEE=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE,related_name='Student')
    task=models.CharField(max_length=200)
    start_date=models.CharField(max_length=200)
    end_date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    TRAINER=models.ForeignKey(Trainer,default=1,on_delete=models.CASCADE,related_name='Teacher')
    file=models.FileField(upload_to="media/task/", null=True)
    

class File_upload(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='media/task/',null=True)

# def __str__(self):
#     return self.filename
    

class classschedule(models.Model):
    Staffallocation=models.ForeignKey(Staff_allocation,default=1,on_delete=models.CASCADE)
    fromdate=models.CharField(max_length=200)
    todate=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
