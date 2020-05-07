from tkinter import *
import _thread
import threading

run = True; s=0; m=0; h=0
master = Tk()
w = Canvas(master, width=700, height=200)
def Run():
    global run, h, m, s

    # Delete old text
    w.delete('all')
    # Add new text
    w.create_text(
        [300, 100], anchor=CENTER, text="%s:%s:%s" % (h, m, s), font=("Consolas", 100)
        )

    s+=1
    if s == 59:
        m+=1; s=-1
    elif m == 59:
        h+=1; m=-1
    # After 1 second, call Run again (start an infinite recursive loop)
    master.after(1000, Run)


   
    
w.pack()
# master.after(1, Run)  # after 1 millisecond, start Run

chrono1 = threading.Thread(target=Run)
chrono1.start()
mainloop()
