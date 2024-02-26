from django.db import models
import datetime, os
from apps.home.models import Student

# Create your models here.
def soapath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%m%d')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('files/', filename)

class File(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE, default="")
    soano = models.CharField(max_length=11, default="")
    description = models.TextField(max_length=191)
    file = models.FileField(upload_to=soapath, null=True, blank=True)
    date = models.CharField(max_length=30, default="")
    status = models.CharField(max_length=20, default="")