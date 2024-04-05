# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.home.models import *
from pay.models import Payment, Paymentor
from soa.models import File
from event.models import Events
import datetime, random, string, csv, secrets
from twilio.rest import Client

account_sid = 'AC4e437002042e19f5ec0ee34ab255dfa8'
auth_token = '5591067702d42e5ca20946c5a50e93d8'
client = Client(account_sid, auth_token)

# @login_required(login_url="/amsai/login/")
def index(request):
    return render(request,'home/dashboard.html')

def empty(request):
    return render(request, 'home/empty.html')


def mystudentlist(request):
    query = ParentMystudent.objects.filter(parent=request.session['login_info'].get('id'))
    mystudent = Student.objects.all()
    if query:
        for obj in query:
            student = Student.objects.get(registerid=obj.mystudent_id)
            obj.student = student
    return render(request, 'parent/my_student.html', {'query': query, 'mystudent': mystudent})


def addStudent(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        return render(request, 'parent/mystudent_add.html')
    if request.method == 'POST':
        lrn = request.POST.get('lrn')
        parent = request.session['login_info'].get('id')
        status = "Pending"
        try:
            student = Student.objects.get(lrn=lrn)
        except Exception as e:
            print(e)
            query = ParentMystudent.objects.filter(parent=request.session['login_info'].get('id'))
            mystudent = Student.objects.all()
            if query:
                for obj in query:
                    student = Student.objects.get(registerid=obj.mystudent_id)
                    obj.student = student
            warn = 'Invalid LRN number.'
            return render(request, 'parent/my_student.html', {'query': query, 'mystudent': mystudent, 'warn': warn})

        ParentMystudent.objects.create(mystudent_id=student.registerid, parent_id=parent, status=status)
        return redirect('/mystudent/list/')


def removeMyStudent(request, nid):
    ParentMystudent.objects.get(id=nid).delete()
    return redirect('/mystudent/list/')

def listMystudent(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
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
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        query = ParentMystudent.objects.get(id=nid)
        return render(request, 'admin/addstudent_approve.html', {'query': query})
    if request.method == 'POST':
        ParentMystudent.objects.filter(id=nid).update(status=request.POST.get('status'))
        return redirect('/amsai/parent_student_list/')


def paymentList(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    item = Payment.objects.filter(parent=request.session.get('login_info')["id"])
    if item:
        for obj in item:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, 'parent/payment_list.html', {'item': item})


def uploadPayment(request):
    if request.method == "POST":
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

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
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
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
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    return render(request, 'payment/or_view.html', {'query': query})


def ORParentsView(request, nid):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    try:
        item = Paymentor.objects.filter(payment=nid)
        return render(request, 'payment/or_view.html', {'item': item})
    except Payment.DoesNotExist:
        return render(request, 'payment/or_view.html')


def soa(request):
    if request.method == 'GET':
        query = File.objects.all()
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        if query:
            for obj in query:
                student = Student.objects.get(registerid=obj.studentid_id)
                obj.student = student
        return render(request, 'admin/soa.html', {'query': query})
    else:
        return render(request, 'admin/soa.html')


def adminPayment(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    item = Payment.objects.all().order_by('-id')
    if item:
        for obj in item:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, 'parent/payment_list.html', {'item': item})


def parentSoa(request, nid):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    query = File.objects.filter(studentid=nid)
    if query:
        for obj in query:
            student = Student.objects.get(registerid=obj.studentid_id)
            obj.student = student
    return render(request, 'parent/view_soa.html', {'query': query})


def soa_upload(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
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
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        users = Teachers.objects.all()
        if users:
            data = {"users": users}
            return render(request, 'admin/teachers.html', locals())
        else:
            return render(request, 'admin/teachers.html', locals())

def registrationList(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

        users = Parent.objects.all().order_by('dateregistered')
        if users:
            data = {"users": users}
            return render(request, 'parent/registration_list.html', locals())
        else:
            return render(request, 'parent/registration_list.html', locals())


def approveRegistration(request, nid):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

        users = Parent.objects.get(id=nid)
        return render(request, 'parent/registration_approval.html', {'users': users})
    if request.method == 'POST':
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        username = f"{random_chars}"
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        Parent.objects.filter(id=nid).update(username=username, password=password, mystatus=request.POST.get('status'))
        return redirect('/registration/list/')


def studentList(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    student = Student.objects.filter(lrn__isnull=False, lastname__isnull=False).order_by("lastname")
    if student:
        data = {"student": student}
        return render(request, 'student/student_list.html', locals())
    else:
        return render(request, 'parent/student_list.html', locals())


def clocking(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

        query = EntryMonitoring.objects.filter(student=request.session.get('login_info')["registerid"]).order_by('-id')
        if query:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)
        else:
            data = {"query": query}
            return render(request, 'student/clocking.html', data)


def check_attendance(request, nid):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    query = EntryMonitoring.objects.filter(student=nid).order_by('-date')
    if query:
        for obj in query:
            student = Student.objects.get(registerid=obj.student_id)
            obj.student = student
    return render(request, "parent/mystudent_attendance.html", {'query': query})


def monitor(request):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        query = EntryMonitoring.objects.all().order_by('-date')
        return render(request, 'student/clocking.html', {'query': query})


def clocking_interface(request):
    date = datetime.datetime.now().date()
    item = Events.objects.all()
    if request.method == 'GET':
        return render(request, 'student/clocking_interface.html', {'date': date, 'item': item})
    if request.method == 'POST':
        date = datetime.datetime.today().date()
        value = request.POST.get('registerid')
        clockin = datetime.datetime.now().time().strftime('%I:%M %p')
        clockout = datetime.datetime.now().time().strftime('%I:%M %p')
        data = EntryMonitoring.objects.filter(student=value, date=date, clockout=None).exists()
        event = Events.objects.all()
        if data:
            try:
                check = Student.objects.get(registerid=value)
            except Exception as e:
                print(e)
                warn = 'Invalid Student ID.'
                return render(request, 'student/clocking_interface.html', {'date': date, 'event': event, 'warn': warn})
            if check:
                unmasked = str(check.lrn)
                unmasked1 = str(check.lastname)
                unmasked2 = str(check.firstname)
                check.lrn = len(unmasked[:-4]) * "*" + unmasked[-2:]
                check.lastname = len(unmasked1[:-4]) * "*" + unmasked1[-2:]
                check.firstname = len(unmasked2[:-4]) * "*" + unmasked2[-2:]
            if len(EntryMonitoring.objects.filter(student=value, date=date)) == 1:
                message = client.messages.create(
                    from_='+19382533493',
                    body=f'DATE: {date}, {clockin} \n {check.lrn} left school premises.',
                    to='+639949912050'
                )
                print(message.body)
                EntryMonitoring.objects.filter(student=value, date=date, clockout=None).update(clockout=clockout)
                return render(request, 'student/clocking_interface.html', {'event': event, 'check': check})
            else:
                EntryMonitoring.objects.filter(student=value, date=date, clockout=None).update(clockout=clockout)
                return render(request, 'student/clocking_interface.html', {'event': event, 'check': check})
        else:
            try:
                check = Student.objects.get(registerid=value)
            except Exception as e:
                print(e)
                warn = 'Invalid Student ID.'
                return render(request, 'student/clocking_interface.html', {'date': date, 'event': event, 'warn': warn})
            if check:
                unmasked = str(check.lrn)
                unmasked1 = str(check.lastname)
                unmasked2 = str(check.firstname)
                check.lrn = len(unmasked[:-4]) * "*" + unmasked[-2:]
                check.lastname = len(unmasked1[:-4]) * "*" + unmasked1[-2:]
                check.firstname = len(unmasked2[:-4]) * "*" + unmasked2[-2:]
            if len(EntryMonitoring.objects.filter(student=value, date=date)) == 0:
                EntryMonitoring.objects.create(student_id=check.registerid, date=date, clockin=clockin, clockout=None)
                message = client.messages.create(
                    from_='+19382533493',
                    body=f'DATE: {date}, {clockout} \n {check.lrn} entered school premises.',
                    to='+639949912050'
                )
                print(message.body)
                return render(request, 'student/clocking_interface.html', {'event': event, 'check': check})
            else:
                EntryMonitoring.objects.create(student_id=check.registerid, date=date, clockin=clockin, clockout=None)
                return render(request, 'student/clocking_interface.html', {'event': event, 'check': check})

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
            message = client.messages.create(
                from_='+19893680649',
                body=f'LRN number:{user} entered on {date} {inam}',
                to='+639456678590'
            )
            print(message.body)
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
        message = client.messages.create(
            from_='+19893680649',
            body=f'LRN number:{user} entered on {date} {outam}',
            to='+639456678590'
        )
        print(message.body)
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
            if Clocking.objects.filter(student=user, date=date).exists():
                query = Clocking.objects.filter(student=user)
                data = {"query": query}
                warn = {"warn": 'Cannot time you in.'}
                return render(request, 'student/clocking.html', data | warn)
            else:
                message = client.messages.create(
                    from_='+19893680649',
                    body=f'LRN number:xxxx entered on {date} {inpm}',
                    to='+639456678590'
                )
                print(message.body)
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
    outpm = datetime.datetime.now().time()
    pmtime = datetime.time(12, 00)
    pm = "--"
    clock = Clocking.objects.filter(student=user, date=date, outpm=pm).exists()
    if clock:
        if outpm >= pmtime:
            Clocking.objects.filter(student=user, date=date).update(outpm=outpm)
            message = client.messages.create(
                from_='+19893680649',
                body=f'LRN number:xxxx entered on {date} {outpm}',
                to='+639456678590'
            )
            print(message.body)
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


def exportPrereg(request):
    gender = request.POST.get('gender')
    date = request.POST.get('date')
    student = StudentPrereg.objects.filter(gender=gender, dateregistered__year=date)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Pre-registration({year}{month}).csv"'

    writer = csv.writer(response)
    if gender == "All":
        student = StudentPrereg.objects.all()
        writer.writerow(['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
                         'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact, item.email])  # rows
        return response
    else:
        writer.writerow(
            ['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
             'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact,
                             item.email])  # rows
        return response


def exportPreregNew(request):
    gender = request.POST.get('gender')
    date = request.POST.get('date')
    student = StudentPrereg.objects.filter(gender=gender, dateregistered__year=date, studenttype="New")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Pre-registration({month}{year}).csv"'

    writer = csv.writer(response)
    if gender == "All":
        student = StudentPrereg.objects.filter(dateregistered__year=date, studenttype="New")
        writer.writerow(['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
                         'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact, item.email])  # rows
        return response
    else:
        writer.writerow(
            ['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
             'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact,
                             item.email])  # rows
        return response


def exportPreregOld(request):
    gender = request.POST.get('gender')
    date = request.POST.get('date')
    student = StudentPrereg.objects.filter(gender=gender, dateregistered__year=date, studenttype="Old")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="Pre-registration({month}{year}).csv"'

    writer = csv.writer(response)
    if gender == "All":
        student = StudentPrereg.objects.filter(dateregistered__year=date, studenttype="Old")
        writer.writerow(['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
                         'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact, item.email])  # rows
        return response
    else:
        writer.writerow(
            ['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
             'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
        for item in student:
            writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
                             item.birthdate, item.address, item.ethnicity, item.religion, item.contact,
                             item.email])  # rows
        return response


def exportClocking(request):
    month = request.POST.get('month')
    year = request.POST.get('year')
    student = request.POST.get('student')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Entry Monitor.csv"'

    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return render(request, 'accounts/login.html')

    writer = csv.writer(response)
    if request.session['login_info'].get('userrole'):
        # date = request.POST.get('date')
        # strpdate = datetime.datetime.strptime(str(date), "%Y-%m")

        if student == "All":
            writer.writerow(['Last Name', 'First Name', 'Date', 'In', 'Out'])  # header
            clock = EntryMonitoring.objects.filter(date__year=year, date__month=month)
            for item in clock:
                user = Student.objects.get(registerid=item.student_id)
                item.user = user
                writer.writerow([item.user.lastname, item.user.firstname, item.date, item.clockin, item.clockout])  # rows
            return response
        else:
            writer.writerow(['Last Name', 'First Name', 'Date', 'In', 'Out'])  # header
            user = Student.objects.get(lrn=student)
            clock = EntryMonitoring.objects.filter(student=user.registerid, date__year=year, date__month=month)
            for item in clock:
                user = Student.objects.get(registerid=item.student_id)
                item.user = user
                writer.writerow([item.user.lastname, item.user.firstname, item.date, item.clockin, item.clockout])  # rows
            return response
    elif request.session['login_info'].get('registerid'):
        user = request.session['login_info'].get('registerid')
        clock = EntryMonitoring.objects.filter(student=user, date__year=year, date__month=month)
        writer.writerow(['Date', 'In', 'Out'])  # header
        for item in clock:
            student = Student.objects.get(registerid=item.student_id)
            item.student = student
            writer.writerow([item.student.lastname, item.student.firstname, item.date, item.clockin, item.clockout])  # rows
        return response


def studentReglist(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')

    list = Student.objects.all()
    return render(request, 'admin/student_registration_list.html', {'list': list})


def approveStudentreg(request, nid):
    if request.method == "GET":
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
        query = Student.objects.get(registerid=nid)
        return render(request, 'admin/student_registration_approve.html', {'query': query})
    if request.method == "POST":
        status = request.POST.get('status')
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(15))
        Student.objects.filter(registerid=nid).update(password=password, status=status)
        return redirect('/amsai/student_registration/list/')


def preregList(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    list = StudentPrereg.objects.all().order_by('-studentid')
    return render(request, 'admin/pre-registration_list.html', {'list': list})


def preregNew(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    list = StudentPrereg.objects.filter(studenttype="New")
    return render(request, 'admin/pre-registration_new.html', {'list': list})


# def preregNewExport(request):
#     student = Student.objects.all()
#     date = datetime.datetime.now().date()
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="Students.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['LRN', 'Last Name', 'First Name', 'Middle Name', 'Suffix', 'Gender', 'Date of Birth', 'Address',
#                      'Ethnicity', 'Religion', 'Contact', 'Email'])  # header
#     for item in student:
#         writer.writerow([item.lrn, item.lastname, item.firstname, item.middlename, item.suffix, item.gender,
#                          item.birthdate, item.address, item.ethnicity, item.religion, item.contact, item.email])  # rows
#
#     return response


def preregOld(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    list = StudentPrereg.objects.filter(studenttype="Old")
    return render(request, 'admin/pre-registration_old.html', {'list': list})


def approvePrereg(request, nid):
    query = StudentPrereg.objects.get(registerid=nid)
    if request.method == "GET":
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')
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
        refno = request.POST.get('refno')
        reg_status = request.POST.get('reg_status')
        password = request.POST.get('password')
        if reg_status == 'Approve':
            StudentPrereg.objects.filter(registerid=nid).update(reg_status=reg_status)
            check = Student.objects.filter(refno=refno)
            if len(check) == 0:
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
                warn = 'Student already exist.'
                return render(request, 'admin/pre-registration_approve.html', {'warn': warn, 'query': query})
        else:
            StudentPrereg.objects.filter(registerid=nid).update(reg_status=reg_status)
            return redirect('/amsai/pre-registration/list/')


def pageUnavailable(request):
    return render(request, 'home/page-500.html')