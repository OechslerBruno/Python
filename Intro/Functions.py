# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:08:39 2021

@author: Bruno
"""
from datetime import datetime

def print_date():
    print('The time is ' + str(datetime.now()))
    print()

def get_Initials(name, force_UpperCase=True):
    if force_UpperCase:
        return name[0:1].upper()
    else:
        return name[0:1]
    
print_date()

name = str(input('Your name....: '))
lastName = str(input('Your lastname: '))

print_date()

initial = get_Initials(name)
print(initial)

initial = get_Initials(lastName, False)
print(initial)
