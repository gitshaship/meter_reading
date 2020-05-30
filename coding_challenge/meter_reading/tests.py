# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import unittest

import pandas as pd

from .models import Reading
from .views import save_file_data


# Create your tests here.

class TestMeterReadings(unittest.TestCase):

    def test_write_data_to_model(self):
        dict_data = [[250, 2291137510, 11., 1., 11., 11., 'R4ZFLS6ZY1UV', 'E', 55893., 20031015100333,
                      'A', None, None, 56311., 20040107100333, 'A', None, None, 418., 'kWh', 20040331.,
                      20040107100333, 20040107100333, 'csv\\downloaded234.csv']]
        df = pd.DataFrame(dict_data,
                          columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                   'filename'])
        save_file_data(df)
        self.assertEqual(Reading.objects.filter()[0].record_indicator, 250)

    def test_write_wrong_formatted_data(self):
        # create a data sample with missing column
        dict_data = [[250, 229113751110, 1., 11., 11., 'R4ZFLS6ZY1UV', 'E', 55893., 20031015100333,
                      'A', None, None, 56311., 20040107100333, 'A', None, None, 418., 'kWh', 20040331.,
                      20040107100333, 20040107100333, 'csv\\downloaded234.csv']]
        df = pd.DataFrame(dict_data,
                          columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                   'filename'])
        self.assertRaises(ValueError, save_file_data, df)