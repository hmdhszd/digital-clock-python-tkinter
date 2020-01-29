from tkinter import * 
from tkinter.ttk import *
from time import strftime 


clock = Tk()
clock.title("Digital Clock Python (tkinter)")
lbl = Label(clock, text=time.strftime("%H:%M:%S") , font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
clock.mainloop()

while True:
    lbl.config(text=time.strftime("%H:%M:%S"))
    lbl.grid(column=0, row=0)



import time
print("something")
time.sleep(5.5)    # pause 5.5 seconds
print("something")




  

root = Tk() 
root.title('Clock') 
  
# This function is used to  
# display time on the label 
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'red') 
  
# Placing clock at the centre 
# of the tkinter clock 
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 
