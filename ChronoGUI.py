import tkinter as tk
import threading
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def Timer(chronumber):
        x = 0
        i = 1
        while i != 0:
            x+=chronumber
            time.sleep(1)
            print(x)

    def timerThread():
        chrono = threading.Thread(target=Timer(1), name='Chronometer')
        chrono.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()