from django.shortcuts import render, redirect
from settings.models import PreregSettings


# Create your views here.
def preregSettings(request):
    settings = PreregSettings.objects.all()
    count = len(settings)
    if request.method == "GET":
        return render(request, "settings/prereg_settings.html", {'settings': settings, 'count': count})
    if request.method == "POST":
        date_open = request.POST.get("date_open")
        date_close = request.POST.get("date_close")
        if count == 0:
            PreregSettings.objects.create(date_open=date_open, date_close=date_close)
            return redirect('/amsai/prereg_settings/')
        else:
            warn = {'warn': 'You can only add one option. Please edit the existing option to make some changes.'}
            return render(request, 'settings/prereg_settings.html', {'settings': settings} | warn)
    return render(request, 'settings/prereg_settings.html')


def preregSettingsDelete(request, nid):
    PreregSettings.objects.get(id=nid).delete()
    return redirect('/amsai/prereg_settings/')