from tkinter import *
from tkinter import messagebox
import random






uppcase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXUZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*?><:;{}[]"


upper,lower,nums,syms = True,True,True,True

all = ""

if upper:
    all += uppcase_letters

if lower:
    all += lowercase_letters


if nums:
    all += digits

if syms:
    all += symbols


length = 20
amount = 1








def gen():
    password = "".join(random.sample(all,length))        #joins all the strings together and samples charactors from them
    messagebox.showinfo("Generated password", "GENERATED PASSWORD : "+password) #messagebox.showinfo REQUIRES 2 arguments the title and the text that you want to display or it wont work

window = Tk()
label = Label(window,text="Password Generator",font = ("arial",20))
label.pack()
window.geometry("500x500")


button = Button(text = "generate",command = gen)
button.pack()

window.mainloop()