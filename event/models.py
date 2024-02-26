from django.db import models
import datetime, os, string

# Create your models here.
def eventpath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('events/', filename)


class Events(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    venue = models.CharField(max_length=45, blank=True, null=True)
    # date = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=eventpath, blank=True, null=True)
    manager = models.CharField(max_length=100, blank=True, null=True)
    attendees = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(max_length=45, blank=True, null=True)
    status = models.BooleanField(default=1)

    class Meta:
        managed = True
        db_table = 'events'