import tkinter as tk
import threading
import time


def Timer(chronumber):
    x = 0
    i = 1
    while i != 0:
        x+=chronumber
        time.sleep(1)
        print(x)

def Starter(): 
    chrono.start()
    chrono2.start()




if __name__ == '__main__':
    chrono = threading.Thread(target=Timer(1), name='Chronometer')
    
    chrono2 = threading.Thread(target=Timer(2), name='Chronometer2')
    
