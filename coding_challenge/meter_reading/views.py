# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import glob
# Create your views here.
import os

import pandas as pd
from django.conf import settings
from django.http import HttpResponse

from .models import Reading


# read all csv files in csv directory
def read_user_files(request):
    try:
        for filename in read_csv('csv'):
            df = pd.read_csv(filename)
            df["filename"] = filename
            save_file_data(df)
        return HttpResponse("Data successfully uploaded", status=201)
    except FileNotFoundError:
        return HttpResponse("Files not found", status=404)


def read_csv(path):
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    if csv_files:
        return csv_files
    else:
        raise FileNotFoundError


def save_file_data(dataframe):
    readings = []

    for row in dataframe.iterrows():

        if row[1][0] == 250:
            try:
                readings.append(
                    Reading(
                        record_indicator=row[1][0],
                        nmi=row[1][1],
                        register_id=row[1][3],
                        meter_serial_number=row[1][6],
                        meter_reading_value=row[1][13],
                        reading_date_time=pd.to_datetime(row[1][14], format=settings.DATETIME_FORMAT),
                        file_name=row[1]['filename'],
                    )
                )
            except ValueError:
                raise ValueError
    Reading.objects.bulk_create(readings)
