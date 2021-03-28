import os
import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

#<-----clear start----->
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
clear()
#<-----clear done----->

#<---------------banner-------------->
def banner():
	print("""
		      7L       7L
		    /   7L   7L   \ \n
		 ----------7L----------

          
		 SSN VALIDITY CHECKER V1       
		       """)
banner()
#<---------------banner-------------->


#<--------------------------ssn checker(multi)-------------->
def SSnV(ssnx):
	url = "https://www.ssn-check.org/verify/"+ssnx
	getDATA = requests.get(url, headers=headers)
	scrape = getDATA.content
	soup = BeautifulSoup(scrape, 'html.parser')
	final = soup.find('p').text
	if re.search('Invalid', final, re.I):
		print "[+] " + "invalid " + ":  " + ssnx
	else:
		open("results/validSSN.txt","a").write(ssnx+"valid"+"\n")
		print "[+] " + "valid   " + ":  " + ssnx

#<--------------------------ssn checker(multi)-------------->

listx =raw_input('SSN list : ')
with open(listx) as cx:
    for o in cx:
        SSnV(o)







        

	 
