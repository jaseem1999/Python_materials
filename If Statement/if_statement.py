# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:13:13 2021

@author: HP
"""

print("enter your score")
score = float(input())
if score >= 95:
    print('pass Grade S')
elif score >= 90:
    print('Pass Grade A+ ')
elif score >= 85:
    print('Pass Grade A ')
elif score >= 80:
    print(' Pass Grade B+')
elif score >= 75 :
    print ('Pass Grade B')
elif score >=70 :
    print('Pass Grade C+')
elif score >=60:
    print('Pass')
else:
        print('fail')