import threading
import threading
import time


def Timer(chronumber):
    x = 0
    i = 1
    while i != 0:
        x+=chronumber
        time.sleep(1)
        print(x)
# https://youtu.be/IEEhzQoKtQU

if __name__ == '__main__':
    chrono = threading.Thread(target=Timer(1), name='Chronometer')
    chrono2 = threading.Thread(target=Timer(2), name='Chronometer2')