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



path="C:/Users/HH/Downloads/Kia Seltos.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia Seltos>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='3 Star Safety|17-20 kmpl|113-158 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 10.90 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


m4 = tk.Button(top, image=img,width=180,height=150)
m4.pack()
m4.place(x=30,y=170)

path="C:/Users/HH/Downloads/Kia Carens.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia Carens>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='3 Star Safety|113-158 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 10.52 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

BMW7 = tk.Button(top, image=img1,width=190,height=150)
BMW7.pack()
BMW7.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/Kia EV6.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia EV6>',fg='black',bg='gray',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='5 Star Safety',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Rs. 60.97 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

Z4 = tk.Button(top, image=img2,width=180,height=150)
Z4.pack()
Z4.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/Kia Sonet.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia Sonet>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='82-118 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. 7.99 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

XM = tk.Button(top, image=img3,width=180,height=150)
XM.pack()
XM.place(x=30,y=500)

path="C:/Users/HH/Downloads/Kia Carnival.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia Carnival>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='Expected launch - September 2024',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 40.00 LakhEstimated price',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='CarWale Confidence: Low',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

M2 = tk.Button(top, image=img4,width=180,height=150)
M2.pack()
M2.place(x=460,y=500)

path="C:/Users/HH/Downloads/Kia EV5.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Kia EV5>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='Expected launch - June 2025 (Tentative)',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 30.00 LakhEstimated price',fg='black',bg='white',font=('Arial 7 bold'))
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