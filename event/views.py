from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.home.models import *
from pay.models import *
from soa.models import *
import time
from .models import Events

# Create your views here.
def event(request):
    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')
    item = Events.objects.all().order_by('-date')
    context = {'item': item}
    return render(request, 'admin/events.html', {'item': item})


def uploadEvent(request):
    if request.method == "POST":
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

        item = Events()
        item.title = request.POST.get('title')
        item.venue = request.POST.get('venue')

        try:
            date = request.POST.get('date')
            date_object = datetime.datetime.strptime(date, '%a %b %d %Y %I:%M %p')
        except Exception as e:
            print(e)
            return render(request, 'admin/events_add.html', {'warn': 'Invalid date format.'})

        item.date = date_object
        item.manager = request.POST.get('manager')
        item.attendees = request.POST.get('attendees')
        item.description = request.POST.get('description')
        item.date_posted = datetime.datetime.today().date()
        if len(request.FILES) != 0:
            item.image = request.FILES['image']

        item.save()
        return redirect('/amsai/events/')

    return render(request, 'admin/events_add.html')


def editEvent(request, nid):
    if request.method == 'GET':
        try:
            request.session['login_info']
        except Exception as e:
            print(e)
            return redirect('/amsai/login/')

        query = Events.objects.get(id=nid)
        if query.image == "":
            query.image = None
        return render(request, 'admin/events_edit.html',{'query': query})
    if request.method == 'POST':
        item = Events()
        item.id = nid
        item.title = request.POST.get('title')
        item.venue = request.POST.get('venue')
        date = request.POST.get('date')
        date_object = datetime.datetime.strptime(date, '%a %b %d %Y %I:%M %p')
        item.date = date_object
        item.manager = request.POST.get('manager')
        item.attendees = request.POST.get('attendees')
        item.description = request.POST.get('description')
        item.date_posted = datetime.datetime.today().date()
        if len(request.FILES) != 0:
            item.image = request.FILES['image']
        item.save()
        return redirect('/amsai/events/')

def refreshEvent(request):
    status = 0
    date = datetime.datetime.today().date()
    Events.objects.filter(date__lt=date).update(status=status)
    return redirect('/amsai/events/')


def dashboard(request):
    count = len(Student.objects.all())
    mcount =len(Student.objects.filter(gender="Male")) + len(Student.objects.filter(gender="M"))
    mcount = str(format((mcount / count * 100), ".2f")) + '%'
    fcount = len(Student.objects.filter(gender="Female")) + len(Student.objects.filter(gender="F"))
    fcount = str(format((fcount / count * 100), ".2f")) + '%'
    year = datetime.datetime.today().year
    event = len(Events.objects.filter(date__year=year))
    date = datetime.datetime.now().date()
    entry = len(EntryMonitoring.objects.filter(date=datetime.datetime.now().date()))
    entry_yesterday = len(EntryMonitoring.objects.filter(date=datetime.datetime.now().date() - datetime.timedelta(days=1)))
    prereg = len(StudentPrereg.objects.filter(reg_status="Pending"))
    male = len(StudentPrereg.objects.filter(reg_status="Pending", gender="Male"))
    male = str((male/prereg)*100) + '%'
    female = len(StudentPrereg.objects.filter(reg_status="Pending", gender="Female"))
    female = str((female / prereg) * 100) + '%'
    student = len(Student.objects.filter(status="Pending")) + len(Student.objects.filter(status__isnull=True))
    parent = len(Parent.objects.filter(mystatus="Pending"))
    mystudent = len(ParentMystudent.objects.filter(status="Pending"))
    pay = len(Payment.objects.all()) - len(Paymentor.objects.all())
    soa = len(Student.objects.all()) - len(File.objects.all())
    sum = prereg + student + parent + mystudent + pay + soa
    item = Events.objects.all()

    try:
        request.session['login_info']
    except Exception as e:
        print(e)
        return redirect('/amsai/login/')

    for obj in item:
        obj.description = obj.description[:250] + '...'
    event_list = Events.objects.filter(status=1).order_by('-date')
    return render(request, 'home/dashboard.html', {'count': count, 'event': event, 'parent': parent,
                                                   'date': date, 'entry': entry, 'prereg': prereg, 'student': student,
                                                   'mystudent': mystudent, 'pay': pay, 'soa': soa, 'sum': sum,
                                                   'item': item, 'event_list': event_list, 'male': male, 'female': female,
                                                   'mcount': mcount, 'fcount': fcount, 'entry_yesterday': entry_yesterday})