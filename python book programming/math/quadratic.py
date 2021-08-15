# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:47:43 2021

@author: HP
"""

import math

def main():
    print ("This program finds the real solutions to a quadratic")
    a = int()
    b = int()
    c = int()
    a= input("Please enter the coefficients a : ")
    b = input("Please enter the coefficients  b : ")
    c = input("Please enter the coefficients c: ")
    
    discRoot = math.sqrt(b * b - 4 * a *c )
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print ("The solutions are:", root1, root2)
    
main();

    
