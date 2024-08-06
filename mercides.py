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
    import index

''

path="C:/Users/HH/Downloads/Mercedes-Benz G-Class.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz G-Class>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='5 Star Safety|6 kmpl|326-577 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 2.55 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


Jimny = tk.Button(top, image=img,width=180,height=150)
Jimny.pack()
Jimny.place(x=30,y=170)

path="C:/Users/HH/Downloads/Mercedes-Benz Maybach S-Class.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz Maybach S-Class>',fg='black',bg='blue',font=('Arial 9 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='7-9 kmpl|496-603 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 2.72 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

GrandVitara = tk.Button(top, image=img1,width=190,height=150)
GrandVitara.pack()
GrandVitara.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/Mercedes-Benz GLC.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz GLC>',fg='black',bg='yellow',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='5 Star Safety|194-255 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Rs. 75.90 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

Benz = tk.Button(top, image=img2,width=180,height=150)
Benz.pack()
Benz.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/Mercedes-Benz C-Class.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz C-Class>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='197-255 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. 61.85 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

Baleno = tk.Button(top, image=img3,width=180,height=150)
Baleno.pack()
Baleno.place(x=30,y=500)

path="C:/Users/HH/Downloads/Mercedes-Benz Maybach GLS.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz Maybach GLS>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='550 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 3.35 Croreonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

Dzire = tk.Button(top, image=img4,width=180,height=150)
Dzire.pack()
Dzire.place(x=460,y=500)

path="C:/Users/HH/Downloads/Mercedes-Benz GLC Coupe.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Mercedes-Benz GLC Coupe>',fg='black',bg='white',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='5 Star Safety|12-16 kmpl|241-255 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 72.50 Lakhonwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1100,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1100,y=600)

Fronx = tk.Button(top, image=img5,width=180,height=150)
Fronx.pack()
Fronx.place(x=890,y=500)


b1 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'),command=on_button_click)
b1.place(x=240,y=300)

b2 = Button(top,text='Book-Now', bg='green',font=('Arial 10 bold'))
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