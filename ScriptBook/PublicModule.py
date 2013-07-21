# -*- coding: utf-8 -*-
'''
Created on 20 июля 2013 г.

@author: Sasha
'''

import shutil
import os
import time
import sys
from datetime import datetime, timedelta, date, time as dt_time

def CheckFileExists(sName):
    d = date