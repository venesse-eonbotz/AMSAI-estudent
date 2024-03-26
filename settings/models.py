from django.db import models


# Create your models here.
class PreregSettings(models.Model):
    date_open = models.DateTimeField(max_length=45, blank=True, null=True)
    date_close = models.DateTimeField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prereg_settings'


class WebAppSettings(models.Model):
    date_open = models.DateTimeField(max_length=45, blank=True, null=True)
    date_close = models.DateTimeField(max_length=45, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'webapp_settings'