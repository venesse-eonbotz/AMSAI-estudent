import datetime, random, string, pytz, secrets, re
from time import sleep
from django.shortcuts import render, redirect
from .forms import MyForm
from apps.home.models import Users, Student, Parent, StudentPrereg
from django.contrib import messages
from settings.models import *
from twilio.rest import Client


def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)


def preRegistration(request):
    form = MyForm(request.POST)
    access = PreregSettings.objects.all()
    if request.method == 'GET':
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        refno = f"{random_chars}"
        now = datetime.datetime.today().replace(tzinfo=pytz.UTC)
        for item in access:
            if item.date_close >= now >= item.date_open:
                return render(request, 'accounts/pre-registration.html', {"refno": refno, "form": form})
            elif item.date_close < now:
                return render(request, 'accounts/prereg_pending.html', {'alert': 'Registration has ended, please consult the registrar.'})
            else:
                countdown = "%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, item.date_open))
                sleep(1)
                return render(request, 'accounts/prereg_pending.html', {'countdown': countdown, 'now': now, 'open': item.date_open})
        notify = "Registration is not currently available."
        return render(request, 'accounts/prereg_pending.html', {'notify': notify})
    if request.method == 'POST':
        studenttype = request.POST.get('studenttype')
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
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        reg_status = "Pending"
        refno = request.POST.get('refno')
        if form.is_valid():
            try:
                len(StudentPrereg.objects.get(contact=contact)) == 0
            except Exception as e:
                print(e)
                warn = "Contact number already associated with another user."
                return render(request, 'accounts/pre-registration.html', {"refno": refno, "form": form, "warn": warn})

            try:
                len(StudentPrereg.objects.get(email=email)) == 0
            except Exception as e:
                print(e)
                warn = "Email already associated with another user."
                return render(request, 'accounts/pre-registration.html', {"refno": refno, "form": form, "warn": warn})
                StudentPrereg.objects.create(firstname=firstname, middlename=middlename, lrn=lrn, studenttype=studenttype,
                                            lastname=lastname, suffix=suffix, gender=gender, birthdate=birthdate,
                                            birthplace=birthplace, religion=religion, ethnicity=ethnicity, strand=strand,
                                            email=email, level=level, curriculum=curriculum, contact=contact,
                                            dateregistered=dateregistered, address=address, mothersname=mothersname,
                                            mothersoccupation=mothersoccupation, motherscontact=motherscontact,
                                            fathersname=fathersname, fatherscontact=fatherscontact, goodmoral=goodmoral,
                                            fathersoccupation=fathersoccupation, guardiansname=guardiansname,
                                            guardianscontact=guardianscontact, guardiansoccupation=guardiansoccupation,
                                            civilstatus=civilstatus, juniorhigh=juniorhigh, junioraddress=junioraddress,
                                            seniorhigh=seniorhigh, senioraddress=senioraddress, form137=form137,
                                            techvoccourse=techvoccourse, culturalminoritygroup=culturalminoritygroup,
                                            disabilities=disabilities, birthcert=birthcert, reportcard=reportcard,
                                            esc=esc, psa=psa, number_2x2=number_2x2, password=password,
                                            reg_status=reg_status, refno=refno)
            messages.success(request, f'{refno}')
            return redirect('/amsai/pre-registration/')
        else:
            messages.error(request, 'Failed reCAPTCHA check!')
            return render(request, 'accounts/pre-registration.html', {"refno": refno, "form": form})


def registerParent(request):
    form = MyForm(request.POST)
    if request.method == 'GET':
        return render(request, 'accounts/parents_register.html', {"form": form})
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        middlename = request.POST.get('middlename')
        email = request.POST.get('email')
        dateofbirth = request.POST.get('dateofbirth')
        dateregistered = datetime.datetime.today().date()
        status = "Pending"  # Default value
        user = Parent.objects.filter(lastname=lastname, firstname=firstname)
        if len(user) != 0:
            return render(request, 'accounts/parents_register.html', {'errors': 'User already exist.', 'form': form})
        Parent.objects.create(firstname=firstname, lastname=lastname, middlename=middlename,
                              email=email, dateregistered=dateregistered, dateofbirth=dateofbirth,
                              mystatus=status)
        return redirect('/amsai/login/')


def registerStudent(request):
    if request.method == 'GET':
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        refno = f"{random_chars}"
        return render(request, 'accounts/student_register.html', {"refno": refno})
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        studenttype = request.POST.get('studenttype')
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
        status = "Pending"
        refno = request.POST.get('refno')
        user = Student.objects.create(firstname=firstname, middlename=middlename, lrn=lrn,
                                            lastname=lastname, suffix=suffix, gender=gender, birthdate=birthdate,
                                            birthplace=birthplace, religion=religion, ethnicity=ethnicity, strand=strand,
                                            email=email, level=level, curriculum=curriculum, contact=contact,
                                            dateregistered=dateregistered, address=address, mothersname=mothersname,
                                            mothersoccupation=mothersoccupation, motherscontact=motherscontact,
                                            fathersname=fathersname, fatherscontact=fatherscontact, goodmoral=goodmoral,
                                            fathersoccupation=fathersoccupation, guardiansname=guardiansname,
                                            guardianscontact=guardianscontact, guardiansoccupation=guardiansoccupation,
                                            civilstatus=civilstatus, juniorhigh=juniorhigh, junioraddress=junioraddress,
                                            seniorhigh=seniorhigh, senioraddress=senioraddress, form137=form137,
                                            techvoccourse=techvoccourse, culturalminoritygroup=culturalminoritygroup,
                                            disabilities=disabilities, birthcert=birthcert, reportcard=reportcard,
                                            esc=esc, psa=psa, number_2x2=number_2x2, password=password,
                                            status=status, refno=refno)
        return render(request, 'home/dashboard.html', locals())


# from django.contrib.auth.decorators import login_required
# # @login_required(login_url="/amsai/login/")
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'is_active': True})
    if request.method == 'POST':
        account = request.POST.get("account")
        username = request.POST.get("username")
        password = request.POST.get("password")
        users = Users.objects.filter(username=username)
        student = Student.objects.filter(lrn=username)
        parent = Parent.objects.filter(username=username)
        applicant = StudentPrereg.objects.filter(refno=username)
        if account == "admin":
            if len(users):
                for user in users:
                    if password == user.password:
                        request.session['login_info'] = {'lrn': user.username, 'userrole': user.userrole, 'name': user.name}
                        print(1)
                        return redirect('/amsai/dashboard/')
                    else:
                        return render(request, "accounts/login.html",
                                      {'warn': 'You have entered an invalid username or password'})
            if users is None:
                return redirect('/amsai/dashboard/')
            else:
                return render(request, "accounts/login.html",
                              {'warn': 'You have entered an invalid username or password'})

        elif account == "student":
            if len(student):
                for user in student:
                    if password == user.password:
                        request.session['login_info'] = {'registerid': user.registerid, 'refno': user.refno, 'status': user.status,
                                                         'lrn': user.lrn, 'firstname': user.firstname, 'lastname': user.lastname,
                                                         'middlename': user.middlename, 'suffix': user.suffix, 'gender': user.gender,
                                                         'birthdate': user.birthdate, 'birthplace': user.birthplace, 'address': user.address,
                                                         'ethnicity': user.ethnicity, 'religion': user.religion, 'contact': user.contact, 'email': user.email,
                                                         'level': user.level, 'strand': user.strand, 'fathersname': user.fathersname,
                                                         'fathersoccupation': user.fathersoccupation, 'fatherscontact': user.fatherscontact,
                                                         'mothersname': user.mothersname, 'mothersoccupation': user.mothersoccupation,
                                                         'motherscontact': user.motherscontact, 'guardiansname': user.guardiansname,
                                                         'guardianscontact': user.guardianscontact, 'guardiansoccupation': user.guardiansoccupation,
                                                         'curriculum': user.curriculum, 'civilstatus': user.civilstatus,
                                                         'junioraddress': user.junioraddress, 'senioraddress': user.senioraddress,
                                                         'juniorhigh': user.juniorhigh, 'seniorhigh': user.seniorhigh, 'techvoccourse': user.techvoccourse,
                                                         'culturalminoritygroup': user.culturalminoritygroup, 'disabilities': user.disabilities,
                                                         'birthcert': user.birthcert, 'goodmoral': user.goodmoral, 'form137': user.form137,
                                                         'reportcard': user.reportcard, 'esc': user.esc, 'psa': user.psa, 'number_2x2': user.number_2x2,
                                                         'last_login': user.last_login}
                        if request.session['login_info'].get('status') == "Approve":
                            if request.session['login_info'].get('last_login') == 0:
                                return redirect('/amsai/first_login/changepass/')
                            else:
                                return redirect('/amsai/dashboard/')
                        elif request.session['login_info'].get('status') == "Pending":
                            return redirect('/amsai/')
                        else:
                            return render(request, 'home/page-403.html')
                    else:
                        return render(request, "accounts/login.html", {'warn': 'You have entered an invalid username or password'})
            if users is None:
                return redirect('/amsai/dashboard/')
            else:
                return render(request, "accounts/login.html",
                              {'warn': 'You have entered an invalid username or password'})

        elif account == "parent":
            if len(parent):
                for user in parent:
                    if password == user.password:
                        request.session['login_info'] = {'id': user.id, 'username': user.username, 'mystatus': user.mystatus,
                                                         'lastname': user.lastname, 'firstname': user.firstname,
                                                         'middlename': user.middlename, 'dateofbirth': user.dateofbirth,
                                                         'email': user.email}
                        print(1)
                        if request.session['login_info'].get('mystatus') == "Approve":
                            return redirect('/amsai/dashboard/')
                        elif request.session['login_info'].get('mystatus') == "Decline":
                            return render(request, 'home/page-403.html')
                        else:
                            return redirect('/amsai/')
                    else:
                        return render(request, "accounts/login.html",
                                      {'warn': 'You have entered an invalid username or password'})
            if users is None:
                return redirect('/amsai/dashboard/')
            else:
                return render(request, "accounts/login.html",
                              {'warn': 'You have entered an invalid username or password'})

        elif account == "applicant":
            if len(applicant):
                for user in applicant:
                    if password == user.password:
                        request.session['login_info'] = {'registerid': user.registerid, 'refno': user.refno, 'reg_status': user.reg_status,
                                                         'studentid': user.studentid, 'studenttype': user.studenttype, 'lrn': user.lrn,
                                                         'firstname': user.firstname, 'lastname': user.lastname, 'middlename': user.middlename,
                                                         'suffix': user.suffix, 'gender': user.gender, 'birthdate': user.birthdate,
                                                         'birthplace': user.birthplace, 'address': user.address, 'ethnicity': user.ethnicity,
                                                         'religion': user.religion, 'contact': user.contact, 'email': user.email,
                                                         'level': user.level, 'strand': user.strand, 'fathersname': user.fathersname,
                                                         'fathersoccupation': user.fathersoccupation, 'fatherscontact': user.fatherscontact,
                                                         'mothersname': user.mothersname, 'mothersoccupation': user.mothersoccupation,
                                                         'motherscontact': user.motherscontact, 'guardiansname': user.guardiansname,
                                                         'guardianscontact': user.guardianscontact, 'guardiansoccupation': user.guardiansoccupation,
                                                         'curriculum': user.curriculum, 'civilstatus': user.civilstatus,
                                                         'junioraddress': user.junioraddress, 'senioraddress': user.senioraddress,
                                                         'juniorhigh': user.juniorhigh, 'seniorhigh': user.seniorhigh, 'techvoccourse': user.techvoccourse,
                                                         'culturalminoritygroup': user.culturalminoritygroup, 'disabilities': user.disabilities,
                                                         'birthcert': user.birthcert, 'goodmoral': user.goodmoral, 'form137': user.form137,
                                                         'reportcard': user.reportcard, 'esc': user.esc, 'psa': user.psa, 'number_2x2': user.number_2x2,
                                                         }
                        print(1)
                        if request.session['login_info'].get('reg_status') == "Approve":
                            return redirect('/amsai/')
                        elif request.session['login_info'].get('reg_status') == "Pending":
                            return redirect('/amsai/')
                        else:
                            return render(request, 'home/page-403.html')
                    else:
                        return render(request, "accounts/login.html",
                                      {'warn': 'You have entered an invalid username or password'})
            if users is None:
                return redirect('/amsai/dashboard/')
            else:
                return render(request, "accounts/login.html",
                              {'warn': 'You have entered an invalid username or password'})
    else:
        return render(request, "home/dashboard.html")


# force user to change password for first login
def changePassword(request):
    if request.method == 'GET':
        return render(request, 'accounts/change_password.html')
    if request.method == 'POST':
        user = request.session['login_info'].get('registerid')
        password = request.POST.get('pass2')
        Student.objects.filter(registerid=user).update(last_login=1, password=password)
        return redirect('/amsai/dashboard/')


def reset_request(request):
    account_sid = 'AC4e437002042e19f5ec0ee34ab255dfa8'
    auth_token = '5591067702d42e5ca20946c5a50e93d8'

    random_no = ''.join(random.choices(string.digits, k=6))
    client = Client(account_sid, auth_token)
    if request.method == 'GET':
        code = f"{random_no}"
        return render(request, 'accounts/reset_request.html', {'code': code})
    if request.method == 'POST':
        code = random_no
        email = request.POST.get('email')
        try:
            student = Student.objects.get(contact=email)
        except Exception as e:
            print(e)
            warn = "User does not exist."
            return render(request, 'accounts/reset_request.html', {'warn': warn})

        # contact number format
        inp = student.contact
        pattern = r"0"
        mat = re.search(pattern, inp)
        if mat and mat.start() == 0:  # <-- change is here!
            contact = re.sub(pattern, '+63', inp, 1)
        else:
            contact = inp

        # send sms verification code
        message = client.messages.create(
            from_='+19382533493',
            body=f'Your verification code is: {code}',
            to=contact
        )
        print(message.body)

        messages.success(request, f'{code}')
        messages.warning(request, f'{email}')
        return redirect('/amsai/reset_password/code/')


def input_code(request):
    if request.method == 'GET':
        return render(request, 'accounts/reset_password_code.html')
    if request.method == 'POST':
        code = request.POST.get('code')
        code1 = request.POST.get('input')
        email = request.POST.get('email')
        if code1 == code:
            messages.success(request, f'{email}')
            return redirect('/amsai/forgot_password/')
        else:
            warn = "Invalid code."
            return render(request, 'accounts/reset_password_code.html', {'warn': warn})


def forgotPassword(request):
    if request.method == 'GET':
        return render(request, 'accounts/forgot_password.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Student.objects.get(contact=email)
        password = request.POST.get('pass2')
        try:
            Student.objects.get(contact=email)
        except Exception as e:
            print(e)
            warn = "User does not exist."
            return render(request, 'accounts/forgot_password.html', {'warn': warn})

        Student.objects.filter(contact=user.contact).update(password=password)
        return redirect('/amsai/login/')


def viewResult(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    return render(request, 'accounts/view_result.html')


def parentResult(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    return render(request, 'parent/registration_result.html')


def studentResult(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    return render(request, 'student/registration_result.html')


def index(request):
    return render(request,'home/dashboard.html')

def empty(request):
    return render(request, 'home/empty.html')

def logout(request):
    request.session.clear()
    return redirect('/amsai/login/')

