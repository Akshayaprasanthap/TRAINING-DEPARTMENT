from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from myapp import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('login_post',views.login_post),
    path('adminhome',views.adminhome),
    path('addtrainer',views.addtrainer),
    path('addtrainer_post',views.addtrainer_post),
    path('view_trainer',views.view_trainer),
    path('deletetrainer/<id>',views.deletetrainer),
    path('view_register',views.view_register),
    path('maketrainer/<int:id>',views.maketrainer),
    path('maketraine/<int:id>',views.maketraine),
    path('view_both',views.view_both),
    path('view_both_post',views.view_both_post),
    path('deletetrainerfromsystem/<int:id>',views.deletetrainerfromsystem),
     path('view_leave_post',views.view_leave_post),
     path('view_leave',views.view_leave),
     path('add_dept',views.add_dept),
    path('add_dept_post',views.add_dept_post),
     path('view_dept',views.view_dept),
     path('deletedepartment/<int:id>',views.deletedepartment),
     path('allocatetrainer_post/<int:id>',views.allocatetrainer_post),
     path('allocatetrainer/<int:id>',views.allocatetrainer),
     path('view_dept_trainer',views.view_dept_trainer),
     path('allocatetrainee/<int:id>/<capacity>',views.allocatetrainee),
     path('allocatetrainee_post/<int:id>',views.allocatetrainee_post),
     path('attendence',views.attendence),
     path('add_attendence/<int:id>',views.add_attendence),
     path('add_attendence_post/<int:id>',views.add_attendence_post),
     path('view_attendence/<int:id>',views.view_attendence),
     path('view_trainee_attendence',views.view_trainee_attendence),
     path('view_stu_attendence/<int:id>',views.view_stu_attendence),
     path('aprovereq/<int:id>',views.aprovereq),
     path('rejectreq/<int:id>',views.rejectreq),
     path('addscheduler/<int:id>',views.addscheduler),
     path('addschedule/<int:id>',views.addschedule),
     path('viewschedule/<int:id>',views.viewschedule),
     path('logout/',views.logout),
#========================================================================================================================
path('view_alloc_dept',views.view_alloc_dept),
path('trainerindex',views.trainerindex),
path('view_alloc_trainee/<int:id>',views.view_alloc_trainee),
path('add_attendence_trainee/<int:id>',views.add_attendence_trainee),
path('add_attendence_trainee_post/<int:id>',views.add_attendence_trainee_post),
path('view_trainee_attendence_trainer/<int:id>',views.view_trainee_attendence_trainer),
path('view_his_attendence',views.view_his_attendence),
path('add_task_post/<int:id>',views.add_task_post),
path('add_task/<int:id>',views.add_task),
path('view_task/<int:id>',views.view_task),
path('view_trainees',views.view_trainees),
path('view_alloc_deptonly',views.view_alloc_deptonly),
path('view_trainees_class',views.view_trainees_class),
path('view_class_sch/<int:id>',views.view_class_sch),
path('view_attendence_trainee',views.view_attendence_trainee),
path('leaverqst',views.leaverqst),
path('leaverqst_post',views.leaverqst_post),
path('view_trainerleave',views.view_trainerleave),


path('traineeindex',views.traineeindex),
path('view_task_trainee',views.view_task_trainee),
path('uploadfile/<int:id>',views.uploadfile),
path('uploadfile_post/<int:id>',views.uploadfile_post),
path('leaverqst_trainee',views.leaverqst_trainee),
path('leaverqst_trainee_post',views.leaverqst_trainee_post),
path('view_traineeleave',views.view_traineeleave),
path('view_attendencetrainee',views.view_attendencetrainee),
path('changepass',views.changepass),
path('changepass_post',views.changepass_post),
path('cls_schdl',views.cls_schdl),
path('view_download/<int:id>',views.view_download),
path('view_upload/',views.view_upload),
path('download/<str:filepath>/',views.download),
# url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
