#love you anika
#code with pain
from colorama import Fore, Style, Back
import requests
import os
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'

#<-----clear start----->
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
clear()
#<-----clear done----->

#<-----banner----->
def Banner():
    bb = open('tools/banner.txt', 'r').read()
    print bb.format(g, r, g, r, g, r, g, r, g, r, g, r, g, c, g, r, g, r, g, r, g, w, g, m, g, w, g)
Banner()
#<-----done----->

#<--------menu----------->
def menu():
		print("""
\033[91m[1]  \033[95mPAYPAL CHECKER \033[92m(MAIL)
\033[91m[2]  \033[95mBIN    CHECKER \033[92m
\033[91m[3]  \033[95mSSN    CHECKER \033[92m
\033[91m[000] \033[95mCHECK FOR UPDATE
			""")
menu()
#<--------done----------->

#<-------------import and go----------------->
doIT = raw_input("WHAT YOU WANA DO \033[91m> ")
if doIT == '1':
    os.system('cmd /k "python tools/paypal.py"')
if doIT == '2':
    os.system('cmd /k "python tools/bin.py"')
if doIT == '3':
    os.system('cmd /k "python tools/ssn.py"')
if doIT == '000':
    page = requests.get('https://raw.githubusercontent.com/Th3-b4G/xchecker/main/updateDATA.txt')
    print(page.content)

    
