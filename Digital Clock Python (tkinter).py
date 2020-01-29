from tkinter import * 
from tkinter.ttk import *
from time import strftime 



  

clock = Tk()
clock.title('Digital Clock Python (tkinter)') 

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
lbl = Label(clock, font = ('arial', 60, 'bold'), background = 'black', foreground = 'red') 
lbl.pack(anchor = 'center') 

time() 
  
mainloop() 
