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



path="C:/Users/HH/Downloads/odiQ3.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi Q3>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='5 Star Safety|14 kmpl|192 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 44.25 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


Q3 = tk.Button(top, image=img,width=180,height=150)
Q3.pack()
Q3.place(x=30,y=170)

path="C:/Users/HH/Downloads/Q3 Sportback.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi Q3 Sportback>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='5 Star Safety|193 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 54.76 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

Sportback = tk.Button(top, image=img1,width=190,height=150)
Sportback.pack()
Sportback.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/Audi e-tron GT.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi e-tron GT>',fg='black',bg='yellow',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='5 Star Safety',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Rs. 1.72 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

etron = tk.Button(top, image=img2,width=180,height=150)
etron.pack()
etron.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/Audi S5.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi S5 Sportback>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='5 Star Safety|10 kmpl|349 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. 77.32 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

S5 = tk.Button(top, image=img3,width=180,height=150)
S5.pack()
S5.place(x=30,y=500)

path="C:/Users/HH/Downloads/Audi Q5.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi Q5>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='5 Star Safety|13 kmpl|261-265 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 65.51 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

altroz = tk.Button(top, image=img4,width=180,height=150)
altroz.pack()
altroz.place(x=460,y=500)

path="C:/Users/HH/Downloads/Audi A8 L.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Audi A8 L>',fg='black',bg='white',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='344 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 25.00 LakhEstimated price',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1100,y=570)

l4 = Label(top,text='Rs. 1.34 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1100,y=600)

altroz = tk.Button(top, image=img5,width=180,height=150)
altroz.pack()
altroz.place(x=890,y=500)


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