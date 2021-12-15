# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:43:23 2021

@author: April Miksch
"""

from tkinter import *
import sys
sys.path.append(".")
from PictureHandling import Picture as pic

window = Tk()
window.title("Unlock! - Python interface")
window.geometry('500x500')

#lbl = Label(window, text="Load Setup")
#lbl.grid(column=10, row=0)

pic_obj = pic()
global counter 


# Create label
l = Label(window, text = "Unlock! Digital escape adventure")
l.config(font =("Courier", 14))

l.pack()
# Create text widget and specify size.
output = Text(window, height = 5, width = 52)


txt = Entry(window,width=50)
txt.place(x=100, y=202)

def load_scenario():
    global counter
    output.delete(1.0, END)
    scenario = txt.get()
    try:
        pic_obj.read_scenario_file(scenario)
        output.insert(END, "Scenario loaded sucessfully")
        key_list = list(pic_obj.imgs.keys())
        int_keys = [digits_only(x) for x in key_list]
        counter=max(int_keys)+1
        pic_obj.open("Introf", idx=counter)
        counter +=1
        pic_obj.open("Introb",idx=counter)
        txt.delete(0, END)
    except IOError:
        output.insert(END, "Scenario file not found")
    
  
    
btn_setup = Button(window, text="Load Scenario", command=load_scenario)
btn_setup.place(x=10, y=200)


txt_open = Entry(window,width=50)
txt_open.place(x=100, y=242)


output.pack()



def open_pictures():
     global counter
     output.delete(1.0, END)
     pics = [convert_digits_only(x) for x in txt_open.get().rstrip().split(" ")]
     
     
     for pic in pics:
         if str(pic) in pic_obj.imgs:
             
             if isinstance(pic, str):
                 counter += 1
                 pic_obj.open(pic, idx=counter)
             elif isinstance(pic, int):
                 pic_obj.open(pic)
             else:
                 output.insert(END, "Cards are only identified by int or str")
                 
         else:
             output.insert(END, "Card {} does not exist \n".format(pic))
             
     txt_open.delete(0, END)
     
btn_open = Button(window, text="Find card", command=open_pictures)
btn_open.place(x=10, y=240)


txt_close = Entry(window,width=50)
txt_close.place(x=100, y=282)

def close_pictures():
    output.delete(1.0, END)
    pics = [convert_digits_only(x) for x in txt_close.get().rstrip().split(" ")]
    for pic in pics:
        if str(pic) in pic_obj.imgs:
            pic_obj.close(pic)

    txt_close.delete(0, END)
    
btn_close = Button(window, text="Put away card", command=close_pictures)
btn_close.place(x=10, y=280)


def convert_digits_only(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return s

def digits_only(s):
    try:
        return int(s)
    except(ValueError, TypeError):
      return 0 





window.mainloop()
