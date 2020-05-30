# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
import glob
import json
import os

import pandas as pd
from django.conf import settings
from django.http import HttpResponse

from .models import Reading, FileName


# read all csv files in csv directory
def read_user_files(request):
    response_dict = {
        "duplicate_files": [],
        "wrong_format_files": []
    }

    try:
        for filename in read_csv('csv'):
            if FileName.objects.filter(file_name=filename).count() == 0:
                # save file name in FileName

                df = pd.read_csv(filename)
                df["filename"] = filename
                try:
                    save_file_data(df)
                    save_file_name(filename)
                except ValueError:
                    response_dict["wrong_format_files"].append(filename)

            else:
                response_dict["duplicate_files"].append(filename)
        if response_dict["duplicate_files"] or response_dict["wrong_format_files"]:
            return HttpResponse(json.dumps(response_dict), status=400)
        else:
            return HttpResponse("Data successfully uploaded", status=201)


    except FileNotFoundError:
        return HttpResponse("Files not found", status=404)


def read_csv(path):
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    if csv_files:
        return csv_files
    else:
        raise FileNotFoundError


def save_file_name(file_name):
    new_file = FileName(file_name=file_name)
    new_file.save()


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
