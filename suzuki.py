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



path="C:/Users/HH/Downloads/Maruti Jimny.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Jimny>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='16 kmpl|103 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 12.74 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


Jimny = tk.Button(top, image=img,width=180,height=150)
Jimny.pack()
Jimny.place(x=30,y=170)

path="C:/Users/HH/Downloads/Maruti Grand Vitara.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Grand Vitara>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='19-27 kmpl|87-102 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 10.87 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

GrandVitara = tk.Button(top, image=img1,width=190,height=150)
GrandVitara.pack()
GrandVitara.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/Maruti Alto K10.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Alto K10>',fg='black',bg='yellow',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='2 Star Safety|24-33 kmpl|56-66 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Rs. 3.99 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='CarWale Confidence: Low',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

Alto = tk.Button(top, image=img2,width=180,height=150)
Alto.pack()
Alto.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/Maruti Baleno.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Baleno>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='22-30 kmpl|76-88 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. 6.66 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

Baleno = tk.Button(top, image=img3,width=180,height=150)
Baleno.pack()
Baleno.place(x=30,y=500)

path="C:/Users/HH/Downloads/Maruti Suzuki Dzire.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Dzire>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='2 Star Safety|22-31 kmpl|76-89 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 6.56 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

Dzire = tk.Button(top, image=img4,width=180,height=150)
Dzire.pack()
Dzire.place(x=460,y=500)

path="C:/Users/HH/Downloads/Maruti Fronx.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Maruti Fronx>',fg='black',bg='white',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='20-28 kmpl|76-99 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 7.51 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1100,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1100,y=600)

Fronx = tk.Button(top, image=img5,width=180,height=150)
Fronx.pack()
Fronx.place(x=890,y=500)


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