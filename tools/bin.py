import os
import base64
import json
import urllib
from colorama import Fore, Style, Back
from multiprocessing.dummy import Pool as fucker

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

#<----------------main--------------------->
def Binx(binxx):
	try:
		url = 'https://lookup.binlist.net/'+binxx
		output = json.load(urllib.urlopen(url))
		print(y+binxx +m+" \- "+output['scheme']+" - "+b+output['type']+" - " +c+output["country"]["name"]+" - "+w+output["bank"]["name"]+g)
		savebinx = open('results/knownBIN.txt', 'a')
		savebinx.write(binxx +" - "+output['scheme']+" - "+output['type']+" - " +output["country"]["name"]+" - "+output["bank"]["name"] + '\n' +"-------------------------------------"+"\n")
	except:
		print(y+binxx +r+"\n \- "+"not valid bin/check manually"+g)
		savebinx = open('results/unknownBIN.txt', 'a')
		savebinx.write(binxx + "\n")
#<----------------main--------------------->

#<-----------banner-------------->
banner ='X19fX19TZXh5aVNleApfX19faVNleHlpU2V4eQpfX195aVNleHlpU2V4eWkKX19faVNleHlpU2V4eWlTCl9fX2lTZXh5aVNleHlpUwpfX2lTZXh5aVNleHlpU2UKX2lTZXh5aVNleHlpU2UKX2lTZXh5aVNleHlpU2UKX2lTZXh5aVNleHlpU2V4eWkKaVNleHlpU2V4eWlTZXh5aVNleHkKaVNleHlpU2V4eWlTZXh5aVNleHlpU2UKaVNleHlpU2V4eWlTZXh5aVNleHlpU2V4Cl9pU2V4eWlfX2lTZXh5aVNleHlpU2V4Cl9fX2lTZXhfX19faVNleHlpU2V4eWkKX19faVNleF9fX19faVNleHlpU2V4eQpfX19pU2V4X19fX19pU2V4eWlTZXh5CiBfX19faVNleF9fX19pU2V4eWlTZXh5ICBfX18gX19fIF8gIF8gICAgX19fIF8gIF8gX19fIF9fXyBfICBfX19fXyBfX18gCiBfX19fX2lTZV9fX19pU2V4eWlTZXggIHwgXyApXyBffCBcfCB8ICAvIF9ffCB8fCB8IF9fLyBfX3wgfC8gLyBfX3wgXyBcCiBfX19fX19pU2VfX2lTZXh5aVNleHkgIHwgXyBcfCB8fCAuYCB8IHwgKF9ffCBfXyB8IF98IChfX3wgJyA8fCBffHwgICAvCiBfX19fX19faVNleHlpU2V4eWlTZXggIHxfX18vX19ffF98XF98ICBcX19ffF98fF98X19fXF9fX3xffFxfXF9fX3xffF9cCg=='
print(base64.b64decode(banner))
#<-----------banner-------------->


binlistx = open(raw_input(g+"Bin list :"), 'r').readlines()
se = fucker(10)
se.map(Binx, binlistx)
se.close()
se.join()

if __name__ == '__main__':
    print(g+"\n ./logout ")


