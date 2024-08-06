from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os


top =Tk()
top.title('Tata')
top.geometry('1200x600')

def on_button_click():
    # print("Button clicked!")
    top.destroy()
    import orderbooking



path="C:/Users/HH/Downloads/pu.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Punch>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=240,y=170)

l2 = Label(top,text='5 Star Safety|18-26 kmpl|72-87 bh',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=210)

l3 = Label(top,text='Rs. 6.13 Lakh onwards',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=270)


punch = tk.Button(top, image=img,width=180,height=150)
punch.pack()
punch.place(x=30,y=170)

path="C:/Users/HH/Downloads/nexon.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Nexon>',fg='black',bg='blue',font=('Arial 10 bold'))
l1.place(x=680,y=170)

l2 = Label(top,text='5 Star Safety|17-24 kmpl|113-118 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=680,y=210)

l3 = Label(top,text='Rs. 11.80 Lakh onwards Offers',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=680,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=680,y=270)

nexon = tk.Button(top, image=img1,width=190,height=150)
nexon.pack()
nexon.place(x=460,y=170)
 
path="C:/Users/HH/Downloads/har.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Harrier>',fg='black',bg='yellow',font=('Arial 10 bold'))
l1.place(x=1110,y=170)

l2 = Label(top,text='5 Star Safety|14-16 kmpl|168 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1110,y=210)

l3 = Label(top,text='Rs. 14.99 LakhonwardsOffers',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1110,y=240)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1110,y=270)

harrier = tk.Button(top, image=img2,width=180,height=150)
harrier.pack()
harrier.place(x=900,y=170)


 
path="C:/Users/HH/Downloads/safari.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Safari>',fg='black',bg='brown',font=('Arial 10 bold'))
l1.place(x=240,y=500)

l2 = Label(top,text='5 Star Safety|14-16 kmpl|168 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=240,y=540)

l3 = Label(top,text='Rs. 15.49 LakhonwardsOffers',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=240,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=240,y=600)

safari = tk.Button(top, image=img3,width=180,height=150)
safari.pack()
safari.place(x=30,y=500)

path="C:/Users/HH/Downloads/Altroz.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Altroz>',fg='black',bg='red',font=('Arial 10 bold'))
l1.place(x=670,y=500)

l2 = Label(top,text='5 Star Safety|18-26 kmpl|72-118 bhp',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=670,y=540)

l3 = Label(top,text='Rs. 15.49 LakhonwardsOffers',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=670,y=570)

l4 = Label(top,text='Avg. Ex-Showroom price',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=670,y=600)

altroz = tk.Button(top, image=img4,width=180,height=150)
altroz.pack()
altroz.place(x=460,y=500)

path="C:/Users/HH/Downloads/Tata Harrier EV.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

l1 = Label(top,text='Tata Harrier EV>',fg='black',bg='gray',font=('Arial 10 bold'))
l1.place(x=1100,y=500)

l2 = Label(top,text='Expected launch - March 2025 (Tentative)',fg='black',bg='white',font=('Arial 7 bold'))
l2.place(x=1100,y=540)

l3 = Label(top,text='Rs. 24.00 LakhEstimated price',fg='black',bg='white',font=('Arial 7 bold'))
l3.place(x=1100,y=570)

l4 = Label(top,text='CarWale Confidence: Low',fg='black',bg='white',font=('Arial 7 bold'))
l4.place(x=1100,y=600)

EV = tk.Button(top, image=img5,width=180,height=150)
EV.pack()
EV.place(x=890,y=500)


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