from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.home.models import *
from pay.models import *
from soa.models import *
import time
from .models import Events

# Create your views here.
def event(request):
    item = Events.objects.all().order_by('-date', 'status')
    # for item.date in item:
    #     item.date.datetime().strftime('%Y/%m/%d %H:%M:%S')
    context = {'item': item}
    # return render(request, 'payment/payment_list.html', context)
    return render(request, 'admin/events.html', {'item': item})


def uploadEvent(request):
    if request.method == "POST":
        item = Events()
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

    return render(request, 'admin/events_add.html')


def editEvent(request, nid):
    if request.method == 'GET':
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


# @login_required(login_url="/amsai/login/")
def dashboard(request):
    count = len(Student.objects.all())
    event = len(Events.objects.all())
    date = datetime.datetime.now().date()
    entry = len(Clocking.objects.filter(date=datetime.datetime.now().date()))
    prereg = len(StudentPrereg.objects.filter(reg_status="Pending"))
    student = len(Student.objects.filter(status="Pending")) + len(Student.objects.filter(status__isnull=True))
    parent = len(Parent.objects.filter(mystatus="Pending"))
    mystudent = len(ParentMystudent.objects.filter(status="Pending"))
    pay = len(Payment.objects.all()) - len(Paymentor.objects.all())
    soa = len(Student.objects.all()) - len(File.objects.all())
    sum = prereg + student + parent + mystudent + pay + soa
    item = Events.objects.all()
    for obj in item:
        obj.description = obj.description[:250] + '...'
    event_list = Events.objects.all().order_by('-date', 'status')[:2]
    return render(request, 'home/dashboard.html', {'count': count, 'event': event, 'parent': parent,
                                                   'date': date, 'entry': entry, 'prereg': prereg, 'student': student,
                                                   'mystudent': mystudent, 'pay': pay, 'soa': soa, 'sum': sum,
                                                   'item': item, 'event_list': event_list})