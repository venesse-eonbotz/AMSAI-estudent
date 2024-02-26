import datetime, random, string
from django.shortcuts import render, redirect
from .models import File
from apps.home.models import Student


# Create your views here.
def Soa(request):
    item = File.objects.all()
    if item:
        for obj in item:
            student = Student.objects.get(registerid=obj.studentid_id)
            obj.student = student
    context = {'item': item}
    # return render(request, 'payment/payment_list.html', context)
    return render(request, 'admin/soa.html', context)


def uploadSoa(request, nid):
    if request.method == 'GET':
        query = Student.objects.filter(registerid=nid)
        return render(request, 'admin/soa_upload.html', {'query': query})
    if request.method == "POST":
        item = File()
        item.date = datetime.datetime.now().date()
        randomid = ''.join(random.choices(string.digits, k=5))
        item.soano = f"{randomid}"
        item.description = request.POST.get('description')
        item.studentid_id = request.POST.get('registerid')

        if len(request.FILES) != 0:
            item.file = request.FILES['file']

        item.save()
        return redirect('/soa/')
