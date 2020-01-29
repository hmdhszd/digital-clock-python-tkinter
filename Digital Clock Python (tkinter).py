from tkinter import * 
from tkinter.ttk import *
from time import strftime 



  

clock = Tk()
clock.title('Digital Clock Python (tkinter)') 

def updateclock(): 
    lbl.config(text = strftime('%H:%M:%S %p')) 
    lbl.after(1000, updateclock) 
  

lbl = Label(clock, font = ('arial', 60, 'bold'), background = 'black', foreground = 'red') 
lbl.pack(anchor = 'center') 

updateclock() 
  
mainloop() 
