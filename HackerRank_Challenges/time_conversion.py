# solution of https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s.split(":")[0])
    minutes = s.split(":")[1]
    seconds = s.split(":")[2][:2]
    if s[-2:] == "PM":
        if hour == 12:
            return s[:-2]
        else:
            hour = hour + 12
        return str(hour)+":"+minutes+":" + str(seconds)
    elif s[-2:] == "AM":
        if hour == 12:
            hour = "00"
            return hour+":"+minutes+":" + str(seconds)
        else:
            return s[:-2]
