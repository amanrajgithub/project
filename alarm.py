from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.ttk import *
from playsound import playsound
obj=Tk()
obj.geometry("400x300")
def alarm() :
    if c1.get()=='AM' :
        x=int(e1.get())
        y=int(e2.get())
    if c1.get()=='PM' :
        x=int(e1.get()) + 12
        y=int(e2.get())
    showinfo('Notification','Alarm has been set . ')
    while True :
        if x==datetime.datetime.now().hour and y==datetime.datetime.now().minute:
            playsound('alarm_clock.mp3')
            break
l1=Label(obj,text="TIME (HOURS) : ")
l2=Label(obj,text="TIME (MINUTES) : ")
l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
e1=Entry(obj)
e2=Entry(obj)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
b1=Button(obj,text='SET',command=alarm)
b1.grid(row=3,column=2)
c1=Combobox(obj,values=['AM','PM'])
c1.grid(row=2,column=2)
l3=Label(obj,text='AM/PM')
l3.grid(row=2,column=1)
obj.mainloop()
