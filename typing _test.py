import tkinter as tk
import time
import threading
import random

class TypeSpeadGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Spead Test")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0D0D0D") 

        self.texts = open("texts.txt" , "r").read().split("\n")

        self.frame = tk.Frame(self.root, bg="#001545")

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts) ,font=("Arial", 16), fg="white", bg="#001545", wraplength=700 ,justify="center")
        self.sample_label.grid(row=0 , column=0 , columnspan=2 , padx=5 , pady=5)
        

        self.input_entry = tk.Entry(self.frame , width=48 , font=("Arial", 18), bg="white", fg="#0032d3", insertbackground="white", relief="solid", bd=2)
        self.input_entry.grid(row=1 , column=0 , columnspan=2 , padx=5 , pady=5)
        self.input_entry.bind("<KeyRelease>" , self.start )

        self.spead_label = tk.Label(self.frame, text="Spead: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS " ,font=("Arial", 16), fg="white", bg="#001545")
        self.spead_label.grid(row=2 , column=0 , columnspan=2 , padx=5 , pady=5)

        self.reset_button = tk.Button(self.frame, text="Reset" , command=self.reset , font=("Arial", 14), bg="#0032d3", fg="white", relief="flat")
        self.reset_button.grid(row=3 , column=0, columnspan=2 , padx=5 , pady=5)

        self.frame.pack(expand=True)
        self.counter = 0
        self.running = False
        self.started = False

        self.root.mainloop()

    def start(self , event):
        if not self.running:
            if not event.keycode in ["Shift", "Control", "Alt"]:
                self.running =True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")


    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split()) / self.counter
            wpm = wps * 60
            self.spead_label.config(text=f"Spead\n{cps:.2f} CPS\n{cpm:.2f} CPM \n{wps:.2f} WPS \n{wpm:.2f} WPS")

    def reset(self):
        self.running = False
        self.counter = 0
        self.spead_label.config(text="Spead: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0 , tk.END)

TypeSpeadGUI()