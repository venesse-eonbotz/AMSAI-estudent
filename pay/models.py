from django.db import models
import os, datetime
from apps.home.models import Student, Parent

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Payment(models.Model):
    refno = models.CharField(max_length=20, blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='student')
    parent = models.ForeignKey(Parent, models.DO_NOTHING, db_column='parent')
    amount = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to=filepath, blank=True, null=True)


def orpath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%m%d')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('OR/', filename)


class Paymentor(models.Model):
    orno = models.AutoField(primary_key=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='payment', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=orpath, blank=True, null=True)
    paymentdate = models.CharField(max_length=50, blank=True, null=True)
