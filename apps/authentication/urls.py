# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import (registerParent, login, logout, preRegistration, viewResult, parentResult,
                    registerStudent, studentResult, changePassword, reset_request, input_code, forgotPassword)
from apps.home import views
from soa.views import Soa, uploadSoa
from event.views import event, uploadEvent, refreshEvent, dashboard, editEvent
from django.conf import settings
from django.conf.urls.static import static
# from home.forms import UploadView

urlpatterns = [
    # authentication
    path('amsai/login/', login, name="login"),
    # path('register/', register_user, name="register"),
    path('amsai/reset_password/', reset_request),
    path('amsai/reset_password/code/', input_code),
    path('amsai/forgot_password/', forgotPassword),
    path('amsai/first_login/changepass/', changePassword),
    path('amsai/pre-registration/', preRegistration),
    path('amsai/pre-registration/result/', viewResult),
    path('register/parent/', registerParent, name="parent_register"),
    path("logout/", logout, name="logout"),

    #student
    path('student/register/', registerStudent),
    path('amsai/student_registration/result/', studentResult),
    path('student/list/',  views.studentList),
    path('student/AM-in/', views.clockinAM),
    path('student/AM-out/', views.clockoutAM),
    path('student/PM-in/', views.clockinPM),
    path('student/PM-out/', views.clockoutPM),
    path('student/time/',  views.clocking),

    #parent
    path('mystudent/list/', views.mystudentlist),
    path('mystudent/<int:nid>/remove/', views.removeMyStudent),
    path('mystudent/<nid>/attendance/', views.check_attendance),
    path('amsai/parent_registration/', registerParent),
    path('amsai/parent_registration/result/', parentResult),
    path('mystudent/<nid>/soa/view/', views.parentSoa),
    path('parent/OR/<int:nid>/view/', views.ORParentsView),
    # path('parent/SOA/upload/', views.soa_upload),
    path('parent/payment/', views.paymentList),
    path('parent/payment/upload/', views.uploadPayment),

    #admin
    path('teachers/list/', views.teacherlist),
    path('amsai/teachers_list/export/', views.exportTeacherList),
    path('amsai/clocking/export/', views.exportClocking),
    path('parent/payment/list/', views.adminPayment),
    path('parent/OR/<int:nid>/', views.uploadOR),
    path('parent/OR/', views.ORList),
    path('amsai/pre-registration/list/', views.preregList),
    path('amsai/pre-registration/new/', views.preregNew),
    path('amsai/pre-registration/old/', views.preregOld),
    path('amsai/student_registration/list/', views.studentReglist),
    path('amsai/pre-registration/list/<int:nid>/update/', views.approvePrereg),
    path('amsai/student_registration/list/<int:nid>/update/', views.approveStudentreg),
    path('soa/', Soa),
    path('soa/upload/<int:nid>/', uploadSoa),
    path('amsai/events/', event),
    path('amsai/events/add/', uploadEvent),
    path('amsai/events/<int:nid>/edit/', editEvent),
    path('amsai/events/refresh/', refreshEvent),
    path('student/monitor/', views.monitor),
    path('mystudent/add/', views.approveMystudent),
    path('mystudent/add/<nid>/approve/', views.approveMystudent),
    path('amsai/student_list/export/', views.exportStudentList),
    path('amsai/parent_student_list/', views.listMystudent),

    # approval
    path('registration/list/',  views.registrationList),
    path('registration/approval/<int:nid>/',  views.approveRegistration),

    # navs
    # path('table/', views.table, name="table"),
    path('amsai/dashboard/', dashboard),
    path('amsai/', views.empty),

    # search
    # path('mystudent/list/search/', views.searchBar, name="search"),

    # new interface for clocking
    path('amsai/clocking_interface/', views.clocking_interface),

    # settings
    # path('amsai/prereg_setings/', views.preregSettings)

    #export
    path('amsai/pre-registration/list/export/', views.exportPrereg),
    path('amsai/pre-registration/new/export/', views.exportPreregNew),
    path('amsai/pre-registration/old/export/', views.exportPreregOld),

    # error
    path('amsai/page-unavailable/', views.pageUnavailable)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

