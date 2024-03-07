from django.shortcuts import render, redirect
import datetime
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

def refreshEvent(request):
    status = 0
    date = datetime.datetime.today().date()
    Events.objects.filter(date__lt=date).update(status=status)
    return redirect('/amsai/events/')


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
    return render(request, 'home/dashboard.html', {'count': count, 'event': event, 'parent': parent,
                                                   'date': date, 'entry': entry, 'prereg': prereg, 'student': student,
                                                   'mystudent': mystudent, 'pay': pay, 'soa': soa, 'sum': sum,
                                                   'item': item})