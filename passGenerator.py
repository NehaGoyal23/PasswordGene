# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:02:13 2019

@author: ecs
"""

import random
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length= input("password length?")
length= int(length)

for p in range(3):
    password= ''
    for c in range(length):
        password+=random.choice(chars)
    print(password)