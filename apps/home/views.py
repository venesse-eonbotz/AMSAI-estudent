# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from apps.home.models import Parent, Student, Teachers, StudentPrereg, Soa, Clocking, ParentMystudent
from pay.models import Payment, Paymentor
from soa.models import File
from event.models import Events
from .forms import FileForm
# from payment.views import Payment
import datetime, random, string, csv


# @login_required(login_url="/amsai/login/")
def index(request):
    return render(request,'home/dashboard.html')

def empty(request):
    return render(request, 'home/empty.html')


def table(request):
    if request.method == 'GET':
        query = ParentMystudent.objects.all()
        if query:
            for obj in query:
                # parent = ParentMystudent.objects.all()
                # request.session['login_info'] = {'id': parent.id}
                student = Student.objects.get(registerid=obj.mystudent_id)
                obj.student = student
            return render(request, 'parent/my_student.html', {'query': query})
        else:
            return render(request, 'parent/my_student.html')


def mystudentlist(request):
    if request.method == 'GET':
        query = ParentMystudent.objects.filter(parent=request.session['login_info'].get('id'))
        mystudent = Student.objects.all()
        if query:
            for obj in query:
                student = Student.objects.get(registerid=obj.mystudent_id)
                obj.student = student
        return render(request, 'parent/my_student.html', {'query': query, 'mystudent': mystudent})


def addStudent(request):
    registerid = request.POST.get('registerid')
    parent = request.session['login_info'].get('id')
    status = "Pending"
    ParentMystudent.objects.create(mystudent_id=registerid, parent_id=parent, status=status)
    return redirect('/mystudent/list/')


def listMystudent(request):
    if request.method == 'GET':
        query = ParentMystudent.objects.all()
        if query:
            for obj in query:
                student = Student.objects.get(registerid=obj.mystudent_id)
                parent = Parent.objects.get(id=obj.parent_id)
                obj.student = student
                obj.parent = parent
        return render(request, 'admin/addstudent_list.html', {'query': query})


def approveMystudent(request, nid):
    if request.method == 'GET':
        query = ParentMystudent.objects.get(id=nid)
        return render(request, 'admin/addstudent_approve.html', {'query': query})
    if request.method == 'POST':
        ParentMystudent.objects.filter(id=nid).update(status=request.POST.get('status'))
        return redirect('/mystudent/add/')


# def mySOA(request):
#     if request.method == 'GET':
#         query = Soa.objects.filter(parentid=request.session['login_info'].get('id'))
#         if query:
#             data = {"query": query}
#             return render(request, 'parent/my_soa.html', data)
#         else:
#             return render(request, 'parent/my_soa.html'


# def myPayment(request):
#     if request.method == 'GET':
#         query = PaymentUpload.objects.all()
#         return render(request, 'admin/payment_list.html', {'query': query})
#     else:
#         return render(request, 'admin/payment_list.html')


def paymentList(request):
    item = Payment.objects.filter(parent=request.session.get('login_info')["id"])
    if item:
        for obj in item:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, 'parent/payment_list.html', {'item': item})


def uploadPayment(request):
    if request.method == "POST":
        item = Payment()
        item.amount = request.POST.get('amount')
        item.refno = request.POST.get('refno')
        item.description = request.POST.get('description')
        item.parent_id = request.session['login_info'].get('id')
        item.student_id = request.POST.get('mystudent')

        if len(request.FILES) != 0:
            item.image = request.FILES['image']

        item.save()
        return redirect('/parent/payment/')
    if request.method == 'GET':
        status = "Approve"
        query = ParentMystudent.objects.filter(parent=request.session['login_info'].get('id'), status=status)
        if query:
            for obj in query:
                student = Student.objects.get(registerid=obj.mystudent_id)
                obj.student = student
        return render(request, 'payment/payment_add.html', {'query': query})

def uploadOR(request, nid):
    if request.method == 'GET':
        query = Payment.objects.get(id=nid)
        return render(request, 'payment/or_upload.html', {'query': query})
    if request.method == "POST":
        item = Paymentor()
        item.description = request.POST.get('description')
        item.paymentdate = request.POST.get('payment_date')
        item.student_id = request.POST.get('student')
        item.payment_id = nid
        item.orno = request.POST.get('orno')
        check = Paymentor.objects.filter(orno=item.orno)
        if len(request.FILES) != 0 and len(check) == 0:
            item.file = request.FILES['file']
            item.save()
            return redirect('/parent/payment/list/')
        else:
            warn = "OR for this payment already exists."
            return render(request, 'payment/or_upload.html', {'warn': warn})




def ORList(request):
    query = Paymentor.objects.all()
    return render(request, 'payment/or_view.html', {'query': query})


def ORParentsView(request, nid):
    try:
        item = Paymentor.objects.filter(payment=nid)
        return render(request, 'payment/or_view.html', {'item': item})
    except Payment.DoesNotExist:
        return render(request, 'payment/or_view.html')



def soa(request):
    if request.method == 'GET':
        query = File.objects.all()
        if query:
            for obj in query:
                student = Student.objects.get(registerid=obj.studentid_id)
                obj.student = student
        return render(request, 'admin/soa.html', {'query': query})
    else:
        return render(request, 'admin/soa.html')


def adminPayment(request):
    item = Payment.objects.all().order_by('-id')
    if item:
        for obj in item:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, 'parent/payment_list.html', {'item': item})


def parentSoa(request, nid):
    query = File.objects.filter(studentid=nid)
    if query:
        for obj in query:
            student = Student.objects.get(registerid=obj.studentid_id)
            obj.student = student
    return render(request, 'parent/view_soa.html', {'query': query})



def soa_upload(request):
    if request.method == 'GET':
        student = Student.objects.all()
        return render(request, 'admin/soa_upload.html', {'student': student})
    if request.method == 'POST':
        upload = Soa()
        randomid = ''.join(random.choices(string.digits, k=5))
        upload.soano = f"{randomid}"
        studentid = request.POST.get('studentid')
        upload.studentid_id = studentid

        if len(request.FILES) != 0:
            upload.file = request.FILES['doc']
            # warn = {"warn": 'Please upload a file'}
            # return render(request, 'admin/soa_upload.html', warn)
        upload.save()

        return redirect('/soa/')


def teacherlist(request):
    if request.method == 'GET':
        users = Teachers.objects.all()
        if users:
            data = {"users": users}
            return render(request, 'admin/teachers.html', locals())
        else:
            return render(request, 'admin/teachers.html', locals())

def registrationList(request):
    if request.method == 'GET':
        users = Parent.objects.all()
        if users:
            data = {"users": users}
            return render(request, 'parent/registration_list.html', locals())
        else:
            return render(request, 'parent/registration_list.html', locals())


def approveRegistration(request, nid):
    if request.method == 'GET':
        users = Parent.objects.get(id=nid)
        return render(request, 'parent/registration_approval.html', {'users': users})
    if request.method == 'POST':
        Parent.objects.filter(id=nid).update(mystatus=request.POST.get('status'))
        return redirect('/registration/list/')

def studentList(request):
    if request.method == 'GET':
        users = Student.objects.all()
        if users:
            data = {"users": users}
            return render(request, 'student/student_list.html', locals())
        else:
            return render(request, 'parent/student_list.html', locals())


def dashboard(request):
    student = Student.objects.all()
    event = Events.objects.all()
    entry = Clocking.objects.filter(date=datetime.datetime.now().date())
    count = len(student)
    event = len(event)
    date = datetime.datetime.now().date()
    entry = len(entry)
    return render(request, 'home/dashboard.html', {'count': count, 'event': event,
                                                   'date': date, 'entry': entry})


def clocking(request):
    if request.method == 'GET':
        query = Clocking.objects.filter(student=request.session.get('login_info')["registerid"])
        if query:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)
        else:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)


def check_attendance(request, nid):
    query = Clocking.objects.filter(student=nid).order_by('-date')
    if query:
        for obj in query:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, "parent/mystudent_attendance.html", {'query': query})


def monitor(request):
    if request.method == 'GET':
        query = Clocking.objects.all()
        if query:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)
        else:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)

def clockinAM(request):
    user = Student.objects.get(registerid=request.session['login_info'].get('registerid'))
    date = datetime.datetime.now().date()
    inam = datetime.datetime.now().time()
    am = "--"
    amtime = datetime.time(11, 59)
    clock = Clocking.objects.filter(student=user, date=date).exists()
    if clock:
        query = Clocking.objects.filter(student=user)
        data = {"query": query}
        warn = {"warn": 'Cannot time you in.'}
        return render(request, 'student/clocking.html', data | warn)
    else:
        if inam <= amtime:
            Clocking.objects.create(student=user, date=date, inam=inam, outam=am, inpm=am, outpm=am)
            return redirect('/student/time/')
        else:
            query = Clocking.objects.filter(student=user)
            data = {"query": query}
            warn = {"warn": 'Cannot time you in.'}
            return render(request, 'student/clocking.html', data | warn)

def clockoutAM(request):
    user = Student.objects.get(registerid=request.session['login_info'].get('registerid'))
    date = datetime.datetime.now().date()
    outam = datetime.datetime.now().time()
    outtime = datetime.time(12, 00)
    am = "--"
    clock = Clocking.objects.filter(student=user, date=date, outam=am).exists()
    if clock and outam <= outtime:
        Clocking.objects.filter(student=user, date=date).update(outam=outam)
        return redirect('/student/time/')
    else:
        query = Clocking.objects.filter(student=user)
        data = {"query": query}
        warn = {"warn": 'Cannot time you out.'}
        return render(request, 'student/clocking.html', data | warn)


def clockinPM(request):
    user = Student.objects.get(registerid=request.session['login_info'].get('registerid'))
    date = datetime.datetime.now().date()
    inpm = datetime.datetime.now().time()
    pmtime = datetime.time(12, 00)
    pm = "--"
    clock = Clocking.objects.filter(student=user, date=date, inpm=pm).exists()
    if clock:
        check = Clocking.objects.filter(student=user, date=date, inpm=pm, inam=pm)
        if check and inpm >= pmtime:
            Clocking.objects.filter(student=user, date=date).update(inpm=inpm)
            return redirect('/student/time/')
        else:
            query = Clocking.objects.filter(student=user)
            data = {"query": query}
            warn = {"warn": 'Cannot time you in.'}
            return render(request, 'student/clocking.html', data | warn)
    else:
        if inpm >= pmtime:
            Clocking.objects.create(student=user, date=date, inpm=inpm, inam=pm, outam=pm, outpm=pm)
            return redirect('/student/time/')
        else:
            query = Clocking.objects.filter(student=user)
            data = {"query": query}
            warn = {"warn": 'Cannot time you in.'}
            return render(request, 'student/clocking.html', data | warn)



def clockoutPM(request):
    user = Student.objects.get(registerid=request.session['login_info'].get('registerid'))
    date = datetime.datetime.now().date()
    inpm = datetime.datetime.now().time()
    outpm = datetime.datetime.now().time()
    pmtime = datetime.time(12, 00)
    pm = "--"
    clock = Clocking.objects.filter(student=user, date=date, outpm=pm).exists()
    if clock:
        if outpm >= pmtime:
            Clocking.objects.filter(student=user, date=date).update(outpm=outpm)
            return redirect('/student/time/')
        else:
            query = Clocking.objects.filter(student=user)
            data = {"query": query}
            warn = {"warn": 'Cannot time you out.'}
            return render(request, 'student/clocking.html', data | warn)
    else:
        query = Clocking.objects.filter(student=user)
        data = {"query": query}
        warn = {"warn": 'Cannot time you out.'}
        return render(request, 'student/clocking.html', data | warn)


def exportStudentList(request):
    student = Student.objects.all()
    date = datetime.datetime.now().date()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Students.csv"'

    writer = csv.writer(response)
    writer.writerow(['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
                     'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
    for item in student:
        writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                         item.birthdate, item.address, item.ethnicity, item.religion, item.contact, item.email])  # rows

    return response


def exportTeacherList(request):
    student = Teachers.objects.all()
    date = datetime.datetime.now().date()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Teachers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Last Name', 'First Name', 'Gender', 'Contact', 'Address'])  # header
    for item in student:
        writer.writerow([item.lastname, item.firstname, item.gender, item.contactno, item.address ])  # rows

    return response


def exportClocking(request):
    clock = Clocking.objects.all()
    date = datetime.datetime.now().date()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Entry Monitor.csv"'

    writer = csv.writer(response)
    writer.writerow(['', '', '', 'AM', '', 'PM', ''])
    writer.writerow(['Last Name', 'First Name', 'Date', 'In', 'Out', 'In', 'Out'])  # header
    for item in clock:
        student = Student.objects.get(registerid=item.student_id)
        item.student = student
        writer.writerow([item.student.lastname, item.student.firstname, item.date, item.inam, item.outam, item.inpm, item.outpm ])  # rows

    return response


def studentReglist(request):
    list = Student.objects.all()
    return render(request, 'admin/student_registration_list.html', {'list': list})


def approveStudentreg(request, nid):
    if request.method == "GET":
        query = Student.objects.get(registerid=nid)
        return render(request, 'admin/student_registration_approve.html', {'query': query})
    if request.method == "POST":
        status = request.POST.get('status')
        Student.objects.filter(registerid=nid).update(status=status)
        return redirect('/amsai/student_registration/list/')


def preregList(request):
    list = StudentPrereg.objects.all()
    return render(request, 'admin/pre-registration_list.html', {'list': list})


def approvePrereg(request, nid):
    if request.method == "GET":
        query = StudentPrereg.objects.get(registerid=nid)
        return render(request, 'admin/pre-registration_approve.html', {'query': query})
    if request.method == "POST":
        lrn = request.POST.get('lrn')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        suffix = request.POST.get('suffix')
        gender = request.POST.get('gender')
        birthdate = request.POST.get('birthdate')
        birthplace = request.POST.get('birthplace')
        religion = request.POST.get('religion')
        ethnicity = request.POST.get('ethnicity')
        email = request.POST.get('email')
        level = request.POST.get('level')
        strand = request.POST.get('strand')
        contact = request.POST.get('contact')
        dateregistered = datetime.datetime.now().date()
        address = request.POST.get('address')
        mothersname = request.POST.get('mothersname')
        mothersoccupation = request.POST.get('mothersoccupation')
        motherscontact = request.POST.get('motherscontact')
        fathersname = request.POST.get('fathersname')
        fathersoccupation = request.POST.get('fathersoccupation')
        fatherscontact = request.POST.get('fatherscontact')
        guardiansname = request.POST.get('guardiansname')
        guardiansoccupation = request.POST.get('guardiansoccupation')
        guardianscontact = request.POST.get('guardianscontact')
        curriculum = request.POST.get('curriculum')
        civilstatus = request.POST.get('civilstatus')
        juniorhigh = request.POST.get('juniorhigh')
        seniorhigh = request.POST.get('seniorhigh')
        junioraddress = request.POST.get('junioraddress')
        senioraddress = request.POST.get('senioraddress')
        techvoccourse = request.POST.get('techvoccourse')
        culturalminoritygroup = request.POST.get('culturalminoritygroup')
        disabilities = request.POST.get('disabilities')
        birthcert = request.POST.get('birthcert')
        form137 = request.POST.get('form137')
        goodmoral = request.POST.get('goodmoral')
        reportcard = request.POST.get('reportcard')
        esc = request.POST.get('esc')
        psa = request.POST.get('psa')
        number_2x2 = request.POST.get('number_2x2')
        password = request.POST.get('password')
        refno = request.POST.get('refno')
        reg_status = request.POST.get('reg_status')
        password = request.POST.get('password')
        if reg_status == 'Approve':
            StudentPrereg.objects.filter(registerid=nid).update(reg_status=reg_status)
            Student.objects.create(refno=refno, lrn=lrn, firstname=firstname, lastname=lastname, middlename=middlename,
                                 suffix=suffix, gender=gender, birthdate=birthdate, birthplace=birthplace,
                                 religion=religion, ethnicity=ethnicity, strand=strand, email=email, level=level,
                                 curriculum=curriculum, contact=contact, dateregistered=dateregistered,  address=address,
                                 mothersname=mothersname, mothersoccupation=mothersoccupation,
                                 motherscontact=motherscontact, fathersname=fathersname, fatherscontact=fatherscontact,
                                 fathersoccupation=fathersoccupation, guardiansname=guardiansname,
                                 guardianscontact=guardianscontact, guardiansoccupation=guardiansoccupation,
                                 civilstatus=civilstatus, juniorhigh=juniorhigh, junioraddress=junioraddress,
                                 seniorhigh=seniorhigh, senioraddress=senioraddress, form137=form137, psa=psa,
                                 techvoccourse=techvoccourse, culturalminoritygroup=culturalminoritygroup,
                                 disabilities=disabilities, birthcert=birthcert, reportcard=reportcard,  esc=esc,
                                 number_2x2=number_2x2, goodmoral=goodmoral, password=password, status=reg_status)
            return redirect('/amsai/pre-registration/list/')
        else:
            StudentPrereg.objects.filter(registerid=nid).update(reg_status=reg_status)
            return redirect('/amsai/pre-registration/list/')

