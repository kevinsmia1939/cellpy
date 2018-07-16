import os
import sys
import datetime
import math
from struct import unpack
import struct
import numpy as np

OLE_TIME_ZERO = datetime.datetime(1899, 12, 30, 0, 0, 0)

def ole2datetime(oledt):
    """converts from ole datetime float to datetime"""
    return OLE_TIME_ZERO + datetime.timedelta(days=float(oledt))

def datetime2ole(dt):
    """converts from datetime object to ole datetime float"""
    delta = dt - OLE_TIME_ZERO
    delta_float = delta / datetime.timedelta(days=1) # trick from SO
    return delta_float

def print_datetime_object(dt):
    """prints a date-object"""
    print(dt)
    print('ctime  :', dt.ctime())
    print('tuple  :', dt.timetuple())
    print('ordinal:', dt.toordinal())
    print('Year   :', dt.year)
    print('Mon    :', dt.month)
    print('Day    :', dt.day)


identity_dict = {
    "Run on channel": "2 (SN 25326)",
    "user": "pjsv",
    "Electrode material": "Si/C",
    "File": "Bec_03_02_C20_delith_GEIS_Soc20_steps_C02.mp",
    "Directory": r"C:\Users\BattLab1\Documents\EC-Lab\Data\SiBEC",
    "Host": "128.39.228.18",
    "Comment": "Si/C Li half cell with reference electrode",
}

#Acquisition started on : 03.15.2017 10:22:54
#Technique started on : 03.15.2017 10:22:54

identity_floats = [
    0.02, # ewe min
    2.00, # ewe max
    26.802, #  DQ, mA.h
    6.500, # Battery capacity
    0.001, # Electrode surface area (cm2)
]

identity_time_stamps = [
    (2017, 3, 15, 10, 22, 54),
    (2017, 3, 15, 10, 22, 54),
]

data = b'\x00\x00\x7f\x00\x03\xa1\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05pjsv\x00\x00C\x00-\x00L\x00a\x00b\x00\\\x00D\x00a\x00t\x00a\x00\\\x00S\x00i\x00\xeeb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x05\x9a\x00\x00\x00\x01\x00\x00\x01\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\n\xd7\xa3<\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7#<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xa0@\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04n\x02\x00\x00$\xe0\x9b\xd7-\xe7\xe4@[C:\\Users\\BattLab1\\Documents\\EC-Lab\\Data\\SiBEC\\Bec_03_02_C20_delith_GEIS_Soc20_steps_C02.mpr\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e128.39.228.181\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03USB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0511.10\x00\x0511.10\x00\x0511.10\x00\x10\x14\x06\x0814911491\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07K\x03\x00\x00*Si/C Li half cell with reference electrode\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00o\x12\x83:\x00\x00\x00\x00o\x12\x83:o\x12\x83:\x00\x00\x00\x00\x01\x00\x00\x04Si/C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00o\x12\x83:\r(unspecified)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00o\x12\x83:\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xd0@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x10\x01\x00\x00\x01\x00\x00\x00o\x12\x83:o\x12\x83:o\x12\x83:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x01\x01\x00\x00\x00\x00\x06\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xb0\x06\x00\x00\x0c\x00=\x00\x04\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00pB\x03\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00 A\x03\x01\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00 A\x02\x00\x02\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\x02\x00\x00\x00\x05\x01\x00\x00\x004C\x01\x00\x02\x00\x00\x00\x02\x00\x00\x00\xf0A\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\t\x02\x00\x00\xc8B\x02\x00\x00\x00\xc8B\x01\x00\x00\x00HB\x03\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00pA\x02\x00\x03\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\x03\x00\x00\x00\x05\x01\x00\x00\x004C\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\xf0A\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00zC\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xa0@\x02\x00\x04\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x004C\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00 A\x03\x01\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x00\x02\x00\x00\xa0@\x01\x02\x00\x00 A\x00\x00\x00\x00 A\x00\x00\xcd\xccL=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x80@\x01\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x80?\x00\x01\x07\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x01\x00\x05\x00\x00\x00\x02\x00\x00\x00\xf0B\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00 A\x03\x00\x06\x00\x00\x00\x01\x00\x00\x00\x00\x80?\x00\x01\x06\x00\x00\x00\x05\x00\x00\xcd\xcc\xcc=\x01\x00\x06\x00\x00\x00\x02\x00\x00\x00zC\x04\x01\x00\x00zC\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xf0A\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x80?\x00\x00\x07\x00\x00\x00\x05\x01\x00\x00\x00\xb4C\x01\x00\x07\x00\x00\x00\x02\x00\x00\x00\xf0A\x03\x01\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xa0A\x03\x00\x08\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\x08\x00\x00\x00\x05\x01\x00\x00\x00\xb4C\x01\x00\x08\x00\x00\x00\x02\x00\x00\x00\xfaC\x04\x01\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00pB\x02\x00\t\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\t\x00\x00\x00\x05\x01\x02\x00\x00\x00\x00\x01\x00\t\x00\x00\x00\x02\x00\x00\x00\xf0A\x03\x01\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\t\x02\x00\x00\xc8B\x02\x00\x00\x00 A\x01\x00\x00\x00HB\x03\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00pA\x02\x00\n\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\n\x00\x00\x00\x05\x01\x00\xcd\xcc\xcc=\x01\x00\n\x00\x00\x00\x00\x00\x00\x00 A\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xa0@\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xa0@\x02\x00\x0b\x00\x00\x00\x01\x01\x00\x00\x000@\x00\x00\x0b\x00\x00\x00\x05\x01\x00\x00\x00\xb4C\x01\x00\x0b\x00\x00\x00\x02\x00\x00\x00 A\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x04\x02\x00\x00\xc8B\x00\x00\x00\x00 A\x00\x00\x00\x00 A\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x80?\x01\x00\x0c\x00\x00\x00\x01\x00\x00fff@\x00\x00\x0c\x00\x00\x00\x05\x01\x00\x00\x00\xb4C\x01\x00\x0c\x00\x00\x00\x02\x00\x00\x00\xf0B\x03\x01\x00\x00\x80?\x01\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\xa0@\x0b{{{\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


print("PARSING")
#
# sep = b"\x00\x00"
#
# divided = data.split(sep)
# for d in divided:
#     if d:
#         print(d)
#         if len(d)>=4:
#             print(np.fromstring(d,dtype='<a4', count=1)[0], end="")
#         else:
#             print("short", end="")
#         print()


#
#
# first_part = b'\x00\x00\x7f\x00\x03\xa1\x01\x00'
# print(len(first_part))
# unpacker = '<d'
# a = unpack(unpacker, first_part)
# b = unpack(unpacker, data[0:8])
#
# print(a)
# print(b)
#
#
# s = 1
#
# dtypes = [
#     'f2',
#     'f4',
#     'f8',
#     '<f8',
#     '>f8',
#     'i2',
#     'i4',
#     'i8',
#     'u2',
#     'u4',
#     'u8',
#     'a8',
#     'S8',
# ]
#
# float_to_search_for = 0.001
# print("\nchecking dtypes")
# for s in range(0,100,4):
#     print(f"{s}: {data[s:8]}")
#     for dtype in dtypes:
#         print(f"  dtype: {dtype}", end=", ")
#         c = np.fromstring(data[s:], dtype=dtype, count=1)[0]
#         try:
#             c_string = c.decode('utf-8')
#         except AttributeError:
#             print("-not string", end=", ")
#             print(f"\n     nummber: {c}", end="")
#         except UnicodeDecodeError:
#             print("-could not decode", end=", ")
#         else:
#             print(f"\n     string: {c_string}", end="")
#         finally:
#             print("")

    # print(data[s:8])
    # print(c)

#sys.exit()


number_of_bytes = len(data)
print("Looking for symmetries")
print(f"Number of bytes: {number_of_bytes}")
for j in range(1,number_of_bytes):
    if not number_of_bytes % j:
        print(f" divisible [{j}] : {int(number_of_bytes/j)}")
    # else:
    #     print(number_of_bytes % j)
print("\nLooking for strings - method one:")
for key in identity_dict:
    string = identity_dict[key]
    start = data.find(string.encode())
    if start > 0:
        print(f"{string}: {start}:{start+len(string)}")
    else:
        print(f"{string}: NOT FOUND!")


print("\nLooking for datetime stamps:")
# Acquisition started on : 03.15.2017 10:22:54
stamps = []
for time_stamp in identity_time_stamps:
    year, month, day, hour, minute, second = time_stamp
    d = datetime.datetime(year, month, day, hour, minute, second)
    print(f"Stamp: {d}")
    ole = datetime2ole(d)
    binary = struct.pack('<d', ole)
    print(f"   ole-float: {ole}")
    print(f"   binary: {binary}")
    start = data.find(binary)
    if start > 0:
        print(f"   : {start}:{start+len(binary)}")
        stamps.append((d, start, start+len(binary)))
    else:
        print(f"   : NOT FOUND!")





print("\n\nJust some testing in the end....")
for d, s1, s2 in stamps:
    date_stamp_1 = data[s1:s2]
    date_float_1 = unpack('<d', date_stamp_1)[0]
    print(date_stamp_1)
    print(f"\nconverging to float: {date_float_1}")
    ole2 = np.fromstring(data[s1:],dtype='<f8', count=1)[0]
    print(f"checking if we get the same when using numpy.fromstring:\n                     {ole2}")
    date_datetime = ole2datetime(ole2)
    print(f"Then it is time to convert to a time-stamp: {date_datetime}")
    print(f"compare with what we were searching for: {d}?")

print("SUCCESS")
