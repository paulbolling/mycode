#!/usr/bin/env python3
import calendar


for i in range(1,13):
    lilcal = calendar.month(2018, i)
    print("\n\nHere is a tiny calendar: \n")
    print(lilcal)