from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os


top =Tk()
top.title('Odis')
top.geometry('1200x600')

def on_button_click():
    # print("Button clicked!")
    top.destroy()
    import orderbooking



path="C:/Users/HH/Downloads/Jaguar F-Pace.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Jaguar F-Pace>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='5 Star Safety|12-19 kmpl|201-543 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 72.90 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


m4 = tk.Button(top, image=img,width=180,height=150)
m4.pack()
m4.place(x=30,y=170)

path="C:/Users/HH/Downloads/Jaguar I-Pace.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Jaguar I-Pace>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='5 Star Safety',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 1.26 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

BMW7 = tk.Button(top, image=img1,width=190,height=150)
BMW7.pack()
BMW7.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/Jaguar E-Pace.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Jaguar E-Pace>',fg='black',bg='yellow',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='Rs. 71.00 LakhEstimated price',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Expected launch - October 2025 (Tentative)',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='CarWale Confidence: Low',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

Z4 = tk.Button(top, image=img2,width=180,height=150)
Z4.pack()
Z4.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/Jaguar F-TYPE.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Jaguar F-TYPE>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='Petrol. Automatic',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. Rs.1 - 1.56 Cr',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

FTYPE = tk.Button(top, image=img3,width=180,height=150)
FTYPE.pack()
FTYPE.place(x=30,y=500)

path="C:/Users/HH/Downloads/BMW M2.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='BMW M2>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='10 kmpl|453 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 99.90 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

M2 = tk.Button(top, image=img4,width=180,height=150)
M2.pack()
M2.place(x=460,y=500)

path="C:/Users/HH/Downloads/BMW X5.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='BMW X5>',fg='black',bg='white',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='12 kmpl|282-375 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 97.00 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1100,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1100,y=600)

X5 = tk.Button(top, image=img5,width=180,height=150)
X5.pack()
X5.place(x=890,y=500)


b1 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
b1.place(x=240,y=300)

b2 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
b2.place(x=680,y=300)

b3 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
b3.place(x=1110,y=300)

b4 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
b4.place(x=240,y=630)

altroz1 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
altroz1.place(x=670,y=630)

altroz2 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
altroz2.place(x=1100,y=630)


top.config(bg='black')
top.mainloop()