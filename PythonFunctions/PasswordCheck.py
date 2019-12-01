# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:49:01 2019

@author: gvandeyk
"""

Help_StrongPassword = '''Criterias of strong password:
         \n0.Minimum length of 8 chars
         \n1.One small letter
         \n2.One capital letter
         \n3.One special character
         \n4.One numeric value'''


def passw(password):
    StrongPassword = [False for x in range(5)]
#
# 0. length
# 1. lowercase char
# 2. Uppercase char
# 3. Numeric
# 4. Special or blank char
#
    if len(password) >= 8:
        StrongPassword[0] = True
    else:
        return False
    for i in password:
        if(i.islower()):
            StrongPassword[1] = True
        elif(i.isupper()):
            StrongPassword[2] = True
        elif(i.isdecimal()):
            StrongPassword[3] = True
        else:
            StrongPassword[4] = True
    return not(False in StrongPassword)


password = input('Enter the password : ')
while (passw(password) is False):
    print('pasword is weak ... please try again')
    print(Help_StrongPassword)
    password = input('Enter a new password : ')
print('password is strong')
