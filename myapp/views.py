from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from django.shortcuts import render,redirect
from myapp.models import *
from django.http import Http404, HttpResponse
from django.db.models import Q
import datetime
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import random


# Create your views here.
def home(request):
    return render(request,'home.html')
def changepass(request):
    return render(request,'changepass.html')

def changepass_post(request):
    cpass=request.POST['cpass']
    npass=request.POST['npass']
    cfpass=request.POST['cfpass']
    res=Login.objects.filter(password=cpass)
    if res.exists():
        if npass==cfpass:
            Login.objects.filter(id=request.session['lid']).update(password=npass)
            return HttpResponse('<script>alert("change password successfully");window.location="/login"</script>')
        else:
            return HttpResponse('<script>alert("incorrect password");window.location="/changepass"</script>')
    else:
        return HttpResponse('<script>alert("incorrect password");window.location="/changepass"</script>')
        


def login(request):
    return render(request,'login.html')
def login_post(request):
    u=request.POST['username']
    p=request.POST['password']
    # user = auth.authenticate(username=u, password=p)
    # print(u)
    # print(p)

    user=Login.objects.filter(username=u,password=p)
    # print(user)
    if user.exists():
        user=user[0]

      
        # print(user.usertype)
        if user.usertype=="admin":
            return HttpResponse('<script>alert("login successfully");window.location="/adminhome"</script>')
        if user.usertype=="trainer":
            
            s=Trainer.objects.filter(LOGIN=user)
            s=s[0]
            print(s.timage)
            request.session['name']=s.tname
            # request.session['image']=s.timage
            # print(request.session['image'],'imageeeeeee')
            request.session['lid']=user.id
            return HttpResponse('<script>alert("login successfully");window.location="/trainerindex"</script>')
        if user.usertype=="trainee":
            
            s=Trainer.objects.filter(LOGIN=user)
            s=s[0]
            print(s.timage)
            request.session['name']=s.tname
            # request.session['image']=s.timage
            request.session['lid']=user.id
            return HttpResponse('<script>alert("login successfully");window.location="/traineeindex"</script>')
        else:
            return HttpResponse('<script>alert("invalid usertype");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("invalid username & password");window.location="/"</script>')
    
    # request.session['lid']=user.id

    # if user is not None:
    #     if user.is_superuser==1 and user.is_staff==1:
    #         auth.login(request,user)
    #                 # return redirect("/all_companies")
    #         return HttpResponse('<script>alert("login successfully");window.location="/adminhome"</script>')
    #
    #     elif user.is_superuser==0 and user.is_staff==1:
    #         auth.login(request, user)
    #         return HttpResponse('<script>alert("login successfully");window.location="/trainerindex"</script>')
    #     elif user.is_superuser==0 and user.is_staff==0:
    #         auth.login(request, user)
    #         return HttpResponse('<script>alert("invalid usertype");window.location="/userindex"</script>')
    # else:
    #
    #     return HttpResponse('<script>alert("invalid username & password");window.location="/"</script>')

def logout(request):
	auth.logout(request)
	return HttpResponse('<script>alert("are you sure logout");window.location="/login"</script>')


    
def adminhome(request):
    res=Trainer.objects.filter(ttype='pending').count()
    print(res)
    return render(request,'admini/adminindex.html',{'res':res})
def addtrainer(request):
    res=Department.objects.all()
    return render(request,'admini/add_trainer.html',{'Departmen':res})
def addtrainer_post(request):
    n=request.POST['first_name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    phone=request.POST['phone']
    email=request.POST['email']
    file=request.FILES.get('file')
    gender=request.POST['inlineRadioOptions']
    # pas=request.POST['password']
    pdf=request.FILES.get('file2')
    select=request.POST['select']
    dept=Department.objects.get(id=select)
    r=Login.objects.filter(username=email)
    if r.exists():
        return HttpResponse('<script>alert("We’re sorry. This email already exists. Please try a different email address to register");window.location="/addtrainer"</script>')
    else:
        log=Login(username=email,password='pending',usertype='pending')
        log.save()
        trainer=Trainer(tname=n,
                        tplace=place,
                        tpin=pin,
                        tpost=post,
                        tphn=phone,
                        temail=email,
                        DEPARTMENT=dept,
                        timage=file,
                        gender=gender,
                        pdf=pdf,
                        ttype='pending',
                        LOGIN=log)
        trainer.save()
        print(log)
        print(trainer)
        return HttpResponse('<script>alert("THANK YOU!!!........your registraion successful, Your password is send to your registerd mail ");window.location="/addtrainer"</script>')


def adminaddtrainer(request):
    res=Department.objects.all()
    return render(request,'admini/admin_add_tr.html',{'Departmen':res})
def adminaddtrainer_post(request):
    n=request.POST['first_name']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    phone=request.POST['phone']
    email=request.POST['email']
    file=request.FILES.get('file')
    gender=request.POST['inlineRadioOptions']
    # pas=request.POST['password']
    pdf=request.FILES.get('file2')
    select=request.POST['select']
    dept=Department.objects.get(id=select)
    r=Login.objects.filter(username=email)
    if r.exists():
        return HttpResponse('<script>alert("We’re sorry. This email already exists. Please try a different email address to register");window.location="/adminaddtrainer"</script>')
    else:
        e=email
        p=random.randint(100000, 999999)
        subject = "Your Username and Password for ZOFT TECH Website"
        message = f"Your Password is: {p} , Your username is:- - {e}" 
        recipient = e  # recipient =request.POST["inputTagName"]
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        log=Login(username=email,password=p,usertype='trainer')
        log.save()
        trainer=Trainer(tname=n,
                        tplace=place,
                        tpin=pin,
                        tpost=post,
                        tphn=phone,
                        temail=email,
                        DEPARTMENT=dept,
                        timage=file,
                        gender=gender,
                        pdf=pdf,
                        ttype='trainer',
                        LOGIN=log)
        trainer.save()
        print(log)
        print(trainer)
        return HttpResponse('<script>alert("THANK YOU!!!........your registraion successful, Your password is send to your registerd mail ");window.location="/adminhome"</script>')






def view_trainer(request):
    res=Trainer.objects.all()
    return render(request,'admini/view_trainer.html',{'student':res})

def deletetrainer(request,id):
    Trainer.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_trainer"</script>')
def view_register(request):
    res=Trainer.objects.filter(ttype='pending')
    return render(request,'admini/view register.html',{'student':res})
def maketrainer(request,id):
    res=Trainer.objects.get(LOGIN=id)
    e=res.temail
    p=random.randint(100000, 999999)
    subject = "Your Username and Password for ZOFT TECH Website"
    message = f"Your Password is: {p} , Your username is:- - {e}" 
    recipient = e  # recipient =request.POST["inputTagName"]
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
    Trainer.objects.filter(LOGIN=id).update(ttype='trainer')
    Login.objects.filter(id=id).update(usertype='trainer')
    Login.objects.filter(id=id).update(password=p)

    return HttpResponse('<script>alert("success");window.location="/view_register"</script>')

def maketraine(request,id):
    res=Trainer.objects.get(LOGIN=id)
    e=res.temail
    p=random.randint(100000, 999999)
    subject = "Your Username and Password for ZOFT TECH Website"
    message = f"Your Password is: {p} , Your username is:- - {e}" 
    recipient = e  # recipient =request.POST["inputTagName"]
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
    Trainer.objects.filter(LOGIN=id).update(ttype='trainee')
    Login.objects.filter(id=id).update(usertype='trainee')
    Login.objects.filter(id=id).update(password=p)
    return HttpResponse('<script>alert("success");window.location="/view_register"</script>')

def view_both(request):
    re=Trainer.objects.filter(Q(ttype='trainer')|Q(ttype='trainee'))
    return render(request,'admini/view both.html',{'student':re})
def view_both_post(request):
    s=request.POST['select']
    print(s,'tttttssssssssssssss')
    r=Trainer.objects.filter(ttype=s)
    print(r)
    return render(request,'admini/view both.html',{'student':r})


def deletetrainerfromsystem(request,id):
    t=attendencee.objects.get(id=id)
    m=Trainer.objects.get(id=id)
    Login.objects.get(id=m.LOGIN.id).delete()
    t.delete()
    m.delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_both"</script>')

def view_leave(request):
    re=leave.objects.all()
    return render(request,'admini/view leave request.html',{'student':re})
def view_leave_post(request):
    s=request.POST['select']
    r=leave.objects.filter(ltype=s)
    return render(request,'admini/view leave request.html',{'student':r})
def aprovereq(request,id):
    leave.objects.filter(id=id).update(status='approved')
    return HttpResponse('<script>alert("approved");window.location="/view_leave"</script>')
def rejectreq(request,id):
    leave.objects.filter(id=id).update(status='reject')
    return HttpResponse('<script>alert("reject");window.location="/view_leave"</script>')
def add_dept(request):
    return render(request,'admini/add department.html')
def add_dept_post(request):
    n=request.POST['dpt_name']
    obj=Department(department_name=n)
    obj.save()
    return HttpResponse('<script>alert("success");window.location="/add_dept"</script>')
def view_dept(request):
    res=Department.objects.all()
    return render(request,'admini/view department.html',{'student':res})
def deletedepartment(request,id):
    Department.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_dept"</script>')
def allocatetrainer(request,id):
    r=Trainer.objects.filter(ttype='trainer')
    return render(request,'admini/allocate trainer.html',{'data':r,'id':id})
def allocatetrainer_post(request,id):
    s=request.POST['select']
    tr=Staff_allocation.objects.filter(STAFF=Trainer.objects.get(id=s))
    if tr.exists():
        return HttpResponse('<script>alert("already added");window.location="/view_dept"</script>')
    else:
        c=request.POST['capacity']
        ss=Trainer.objects.get(id=s)
        did=Department.objects.get(id=id)
        obj=Staff_allocation(DEPARTMENT=did,STAFF=ss,capacity=c)
        obj.save()
        return HttpResponse('<script>alert("success");window.location="/allocatetrainer"</script>')

def view_dept_trainer(request):
    res=Staff_allocation.objects.all()
    return render(request,'admini/view depmt and trainer.html',{'data':res})


def allocatetrainee(request,id,capacity):
    r=Trainer.objects.filter(ttype='trainee')
    res=Student_allocation.objects.filter(STAFF_ALLOCATION=Staff_allocation.objects.get(id=id)).count()
    
    if float(res)<float(capacity):
       
        return render(request,'admini/allocate student.html',{'data':r,'id':id})
    else:
        return HttpResponse('<script>alert("full");window.location="/view_dept_trainer"</script>')

def allocatetrainee_post(request,id):
    s=request.POST['select']
    stu=Student_allocation.objects.filter(STUDENT=Trainer.objects.get(id=s))
    if stu.exists():
        return HttpResponse('<script>alert("already added");window.location="/view_dept_trainer"</script>')
    else:
        ss=Trainer.objects.get(id=s)
        did=Staff_allocation.objects.get(id=id)
        obj=Student_allocation(STAFF_ALLOCATION=did,STUDENT=ss)
        obj.save()
        return HttpResponse('<script>alert("success");window.location="/view_dept_trainer"</script>')
    
# def view_Trainers(request,id):
#     ss = Staff_allocation.objects.filter(DEPARTMENT=id)
#     return render(request, 'admini/view department.html', {'student': ss})


def attendence(request):
    res=Staff_allocation.objects.all()
    return render(request,'admini/attendence.html',{'data':res})
def add_attendence(request,id):
    r=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id))
    # if r.exists():
    #     return HttpResponse('<script>alert("already added");window.location="/attendence"</script>')
    # else:
    return render(request,'admini/present or absent.html',{'id':id})
def add_attendence_post(request,id):
    d=request.POST['date']
    p=request.POST['select']
    fid=Trainer.objects.get(id=id)
    # d=datetime.datetime.now().strftime("%Y-%m-%d")
    r=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date=d)
    if r.exists():
        return HttpResponse('<script>alert("already added");window.location="/attendence"</script>')
    else:
        obj=attendencee(FROMID=fid,status=p,typee='trainer',date=d)
    
        obj.save()
        return HttpResponse('<script>alert("success");window.location="/attendence"</script>')

def view_attendence(request,id):
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id)).order_by('date')
    return render(request,'admini/view attendence.html',{'data':res,'id':id})

def view_attendence_post(request,id):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']

    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date__range=[fdate, tdate]).order_by('date')
    if not res:
        alert_message = f'<script>alert("No results found between {fdate} to {tdate}"); window.location="/view_attendence/{id}"</script>'
        return HttpResponse(alert_message)

    return render(request,'admini/view attendence.html',{'data':res,'id':id,'from':fdate,'to':tdate})

def view_trainee_attendence(request):
    res=Student_allocation.objects.all()
    print(res)
    return render(request,'admini/view trainee attendence.html',{'data':res})

def view_stu_attendence(request,id):
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id)).order_by('date')
    return render(request,'admini/view student attendense.html',{'data':res,'id':id})

def view_stu_attendence_post(request,id):
    status=request.POST['status']
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date__range=[fdate, tdate],status=status).order_by('date')
    if not res:
        alert_message = f'<script>alert("No results found between {fdate} to {tdate}"); window.location="/view_stu_attendence/{id}"</script>'
        return HttpResponse(alert_message)
    return render(request,'admini/view student attendense.html',{'data':res,'id':id,'from':fdate,'to':tdate,'status':status})

def addschedule(request,id):
    return render(request,'admini/addschedule.html',{'id':id})
def addscheduler(request,id):
    fromdate=request.POST['fdate']
    todate=request.POST['tdate']
    time=request.POST['time']
    r=Staff_allocation.objects.get(id=id)
    trainer=classschedule(fromdate=fromdate,
                    todate=todate,
                    time=time,
                    Staffallocation=r,)
    trainer.save()
    return HttpResponse('<script>alert("success");window.location="/view_dept_trainer"</script>')
def viewschedule(request,id):
    res=classschedule.objects.filter(Staffallocation=Staff_allocation.objects.get(id=id))
    print(id,"iiii")
    print(res)
    return render(request,'admini/view_schedule.html',{'res':res})

def view_students(request,id):
    ss = Student_allocation.objects.filter(STAFF_ALLOCATION=id)
    return render(request, 'admini/view_traine.html', {'student': ss})




# ============================================================================================================
#                                       TRAINERS
# ============================================================================================================
def trainerindex(request):
    r=Trainer.objects.get(LOGIN=request.session['lid'])
    res=Staff_allocation.objects.filter(STAFF=r)
    if res.exists():
        res=res[0]
        ss=Student_allocation.objects.filter(STAFF_ALLOCATION_id=res).count()
        aa=Staff_allocation.objects.filter(STAFF=r).count()
        print(r,'rrr')
        print(res,'iiiii')
        print(ss,'3333')
    
        print(aa)
        return render(request,'trainer/trainerindex.html',{'ss':ss,'aa':aa})
    else:
        return render(request,'trainer/trainerindex.html')
    


def viewprofile(request):
    trainer=Trainer.objects.get(LOGIN=request.session['lid'])#.....select * from tablename where id = 7;
    return render(request,'trainer/viewprofile.html',{'trainer':trainer})

def view_trainees(request):
    r = Trainer.objects.get(LOGIN=request.session['lid'])
    res = Staff_allocation.objects.get(STAFF=r)
    ss = Student_allocation.objects.filter(STAFF_ALLOCATION=res)
    return render(request, 'trainer/view_trainees_details.html', {'student': ss})

def view_trainees_class(request):
    r = Trainer.objects.get(LOGIN=request.session['lid'])
    res = Staff_allocation.objects.filter(STAFF=r)
    print(res,'000000000000000000000000000')
    for i in res:
        print(i.id)
        a=i.id
        ss = Student_allocation.objects.filter(STAFF_ALLOCATION=a)
        for r in ss:
            sss=classschedule.objects.filter(Staffallocation=r.id)
    print(ss)
    return render(request, 'trainer/trainees_class.html', {'student': sss})


def view_class_sch(request):
    r = Trainer.objects.get(LOGIN=request.session['lid'])
    re = Staff_allocation.objects.filter(STAFF=r)
    print(re,'000000000000000000000000000')
    for i in re:
            res=classschedule.objects.filter(Staffallocation=i.id)
            print(res,'wwwwwwwww')

            return render(request,'trainer/view_class_schedule.html',{'res':res})
    
def viewschedule_post(request,id):
    res=classschedule.objects.filter(Staffallocation=Staff_allocation.objects.get(id=id))
    print(id,"iiii")
    print(res)
    return render(request,'trainer/view_class_schedule.html',{'res':res})
    

def view_alloc_dept(request):
    res=Staff_allocation.objects.filter(STAFF=Trainer.objects.get(LOGIN=request.session['lid']))
    print('id===',request.session['lid'])
    print('staff===',res)
    return render(request,'trainer/view department.html',{'student':res})


def view_alloc_deptonly(request):
    res=Staff_allocation.objects.filter(STAFF=Trainer.objects.get(LOGIN=request.session['lid']))
    return render(request,'trainer/view departmentonly.html',{'student':res})

def view_alloc_trainee(request,id):
    print('idd====',id)
    # re=Staff_allocation.objects.filter(STAFF=id)
    # print(re,'ooooooooooooooooooo')
    # for i in re:

    res=Student_allocation.objects.filter(STAFF_ALLOCATION=id)
    print(res,'dettttttttttttttttttttttttttt')
    return render(request,'trainer/view_trainees.html',{'student':res})

def add_attendence_trainee(request,id):
    return render(request,'trainer/present or absent.html',{'id':id})
def add_attendence_trainee_post(request,id):
    d=request.POST['date']
    p=request.POST['select']
    fid=Trainer.objects.get(id=id)
    # d=datetime.datetime.now().strftime("%Y-%m-%d")
    r=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date=d).order_by('date')
    if r.exists():
        return HttpResponse('<script>alert("already added");window.location="/view_alloc_dept"</script>')
    else:
        obj=attendencee(FROMID=fid,status=p,typee='trainee',date=d)
        obj.save()
        return HttpResponse('<script>alert("success");window.location="/view_alloc_dept"</script>')
    
def view_trainee_attendence_trainer(request,id):
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id)).order_by('date')
    return render(request,'trainer/view attendence.html',{'data':res,'id':id})

def view_attendence_trainee_post(request,id):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=attendencee.objects.filter(typee='trainee',date__range=[fdate, tdate]).order_by('date')
    if not res:
        alert_message = f'<script>alert("No results found between {fdate} to {tdate}"); window.location="/view_trainee_attendence_trainer/{id}"</script>'
        return HttpResponse(alert_message)

    return render(request,'trainer/view attendence.html',{'data':res,'id':id,'from':fdate,'to':tdate})



def view_attendence_trainee(request,id):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=attendencee.objects.filter(typee='trainee',date__range=[fdate, tdate]).order_by('date')
    
    # res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date__range=[fdate, tdate]).order_by('date')

    return render(request,'trainer/view_trainee attendence.html',{'data':res,'id':id})


    
# def view_his_attendence(request,id):
#     res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id)).order_by('date')
#     return render(request,'trainer/view his attendence.html',{'data':res,'id':id})


def view_his_attendence(request):
    e=Trainer.objects.get(LOGIN=request.session['lid'])
    res=attendencee.objects.filter(FROMID=e).order_by('date')
    return render(request,'trainer/view his attendence.html',{'data':res,'id':e.id})

def view_his_attendence_post(request,id):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date__range=[fdate, tdate]).order_by('date')
    if not res:
        alert_message = f'<script>alert("No results found between {fdate} to {tdate}"); window.location="/view_his_attendence"</script>'
        return HttpResponse(alert_message)
     
    return render(request,'trainer/view his attendence.html',{'data':res,'id':id,'from':fdate,'to':tdate})


def add_task(request,id):
    return render(request,'trainer/add_task.html',{'id':id})
def add_task_post(request,id):
    print(id)
    tas=request.POST['task']
    sdate=request.POST['sdate']
    edate=request.POST['edate']
    fid=Trainer.objects.get(id=id)
    print(fid)
    r=Trainer.objects.get(LOGIN=request.session['lid'])
    print(r,'trainee iddddd')
    obj=Task(TRAINER=r,TRAINEE=fid,task=tas,status='assigned',start_date=sdate,end_date=edate)
    obj.save()
    return HttpResponse('<script>alert("success");window.location="/view_alloc_dept"</script>')
def view_task(request,id):
    # print(id,'iddd')
    # l=Trainer.objects.get(LOGIN=request.session['lid'])
    # print(l,'llllllllllllll')
    res=Task.objects.filter(TRAINEE=id).order_by('-start_date').values()
    return render(request,'trainer/view task.html',{'data':res})

def view_downloads(request,id):
    # res={'file':Task.objects.filter(TASK_id=id)}
    print(id,"ioooooooooooooooo")
    res=File_upload.objects.filter(task=id)
    # print(res.TASK.file)
    return render(request, 'trainer/view_downloads.html', {'data': res})

def leaverqst(request):
    return  render(request,'trainer/leaverequest.html')
def leaverqst_post(request):
    fdate=request.POST['fdate']
    edate = request.POST['tdate']
    reason = request.POST['reason']
    res=leave(fromdate=fdate,todate=edate,reason=reason,status='pending',FROMID=Trainer.objects.get(LOGIN=request.session['lid']),ltype='trainer')
    res.save()
    return HttpResponse('<script>alert("success");window.location="/leaverqst"</script>')

def view_trainerleave(request):
    res=leave.objects.filter(FROMID=Trainer.objects.get(LOGIN=request.session['lid']))
    return  render(request,'trainer/view_leave.html',{'data':res})


###################################
#############################################################################################################3

def traineeindex(request):
    r=Trainer.objects.get(LOGIN=request.session['lid'])
    print(r)
    # res=Staff_allocation.objects.get(STAFF=r)
    # ss=Student_allocation.objects.filter(STAFF_ALLOCATION=res).count()
    # aa=Staff_allocation.objects.filter(STAFF=r).count
    rr=Task.objects.filter(TRAINEE=Trainer.objects.get(LOGIN=request.session['lid'])).count()
    print(rr,'counttttttttttttttttttt')
    return render(request,'trainee/teainee_index.html',{'rr':rr})

def viewtprofile(request):
    trainer=Trainer.objects.get(LOGIN=request.session['lid'])#.....select * from tablename where id = 7;
    return render(request,'trainee/viewtprofile.html',{'trainer':trainer})



def view_task_trainee(request):
    e=Trainer.objects.get(LOGIN=request.session['lid'])
    res=Task.objects.filter(TRAINEE=e).order_by('-end_date')
    if res.exists():
        for i in res:
            r=File_upload.objects.filter(task=i)
            if r.exists():
                r=r[0]
                print(r)
                ar=[]
                # for ij in r:
                ar.append({
                    "id":r.id,
                    "file":r.file
                })
                print(ar,'rrrrrrrrrrrrrrrrrrrrr')
            else:
                # return HttpResponse('<script>alert("no task added");window.location="/traineeindex"</script>')
                return render(request, 'trainee/task.html', {'data': res})

    
        
    # file=File_upload.objects.filter(task__id=res)
    # file=file[0]
    # print(file,"fffffffffffffffffffffffffffffffffff")
    # print(res.TASK.file)
        return render(request, 'trainee/task.html', {'data': res,'data2':ar})
    else:
        return HttpResponse('<script>alert("no task added");window.location="/traineeindex"</script>')




def view_download(request,id):
    # res={'file':Task.objects.filter(TASK_id=id)}
    print(id,"ioooooooooooooooo")
    res=File_upload.objects.filter(task=id)
    # print(res.TASK.file)
    return render(request, 'trainee/view_download.html', {'data': res})

# def download(request,path):
#     file_path=os.path.joining(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path,'rb')as fh:
#             response=HttpResponse(fh.read(),content_type="application/file")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response
#     raise Http404

def uploadfile(request,id):
    return render(request, 'trainee/upload_file.html',{'id':id})

def uploadfile_post(request,id):
    print('et')
    file = request.FILES.get('file3')
    print(file)
    print('id',id)
    # r=Task.objects.filter(TRAINEE=Trainer.objects.get(LOGIN=request.session['lid'])).filter(id=id)
    r= Task.objects.get(id = id)
    t=File_upload.objects.filter(task_id=id)
    if t.exists():
           return HttpResponse('<script>alert("task already submitted");window.location="/view_task_trainee"</script>')
    else:

    # r.file=file
    # file = File_upload(task_id = r, file = file)
        Task.objects.filter(id=r.id).update(status="submitted")
        file = File_upload(task_id = r.id, file = request.FILES.get('file3'))
        print('saved')
        # r.update(file=file)
        file.save()
        print('cnfrm')
        
        # return render(request,'trainee/task.html', {'data': r})
        return redirect(view_task_trainee)

    # Task.objects.filter(id=id).update(file=file,status="submitted")
    # return HttpResponse('<script>alert("success");window.location="/view_task_trainee"</script>')










def view_upload(request):
    res=Task.objects.filter(TASK=Task.objects.filter(TRAINEE_id=id))
    return render(request,'trainee/view_download.html',{'student':res})

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:

    # uploaded_file = File_upload.objects.get(id=id)
            response = HttpResponse(fh.read(), content_type='application/file')
            response['Content-Disposition'] = 'inline; filename=' +os.path.basename(file_path)
            return response
    raise Http404


def leaverqst_trainee(request):
    return  render(request,'trainee/leaverequest_trainee.html')
def leaverqst_trainee_post(request):
    fdate=request.POST['fdate']
    edate = request.POST['tdate']
    reason = request.POST['reason']
    res=leave(fromdate=fdate,todate=edate,reason=reason,status='pending',FROMID=Trainer.objects.get(LOGIN=request.session['lid']),ltype='trainee')
    res.save()
    return HttpResponse('<script>alert("success");window.location="/leaverqst_trainee"</script>')
def view_traineeleave(request):
    res=leave.objects.filter(FROMID=Trainer.objects.get(LOGIN=request.session['lid']))
    return  render(request,'trainee/view_trainee_leave.html',{'data':res})

def view_attendencetrainee(request):
    e=Trainer.objects.get(LOGIN=request.session['lid'])
    print(e,'pppppppppppp')
    res=attendencee.objects.filter(FROMID=e).order_by('date')
    return render(request,'trainee/view_traineeattendence.html',{'data':res,'id':e.id})

def view_attendencetrainee_post(request,id):
    fdate=request.POST['fdate']
    tdate=request.POST['tdate']
    res=attendencee.objects.filter(FROMID=Trainer.objects.get(id=id),date__range=[fdate,tdate]).order_by('date')
    if not res:
        alert_message = f'<script>alert("No results found between {fdate} to {tdate}"); window.location="/view_attendencetrainee"</script>'
        return HttpResponse(alert_message)
    return render(request,'trainee/view_traineeattendence.html',{'data':res,'id':id,'from':fdate,'to':tdate})





def cls_schdl(request):
    x=Trainer.objects.get(LOGIN=request.session['lid'])
    print(x,'xxxxx')
    re=Student_allocation.objects.get(STUDENT=x)
    r=re.STAFF_ALLOCATION
    print(r,'77777777777')
    res=classschedule.objects.filter(Staffallocation=r)
    return render(request,'trainee/vw_cls_schdl.html',{'res':res})
    