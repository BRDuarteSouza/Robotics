# mel_debug.py
# Make debug messages
#Author: Bruno Duarte <brduarte95@gmail.com>

from datetime import datetime

try:
    from termcolor import colored
    color = True
except ImportError:
    print("Please install termcolor!")

def info(msg):
    time = str(datetime.now())
    text = colored("INFO :","blue",attrs = ['bold','underline'])
    print("[{}] {} {}".format(time,text,msg))

def debug(msg):
    time = str(datetime.now())
    text = colored("DEBUG :","green", attrs = ['bold','underline'])
    print("[{}] {} {}".format(time,text,msg))

def warn(msg):
    time = str(datetime.now())
    text = colored("WARN :","yellow", attrs = ['bold','underline'])
    print("[{}] {} {}".format(time,text,msg))

def error(msg):
    time = str(datetime.now())
    text = colored("ERROR :","red", attrs = ['bold', 'underline'])
    print("[{}] {} {}".format(time,text,msg))
