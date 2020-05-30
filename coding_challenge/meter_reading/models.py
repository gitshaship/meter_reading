# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Reading(models.Model):
    record_indicator = models.IntegerField()
    nmi = models.CharField(max_length=10)
    register_id = models.CharField(max_length=10)
    meter_serial_number = models.CharField(max_length=10)
    meter_reading_value = models.CharField(max_length=20)
    reading_date_time = models.DateTimeField(verbose_name='Reading Date Time')
    file_name = models.CharField(max_length=200)
