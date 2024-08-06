from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os


top =Tk()
top.title('vratika')
top.geometry('1200x600')

def on_button_click1():
    # print("Button clicked!")
    top.destroy()
    import tata

def on_button_click2():
    # print("Button clicked!")
    top.destroy()
    import KIA

def on_button_click3():
    # print("Button clicked!")
    top.destroy()
    import suzuki

def on_button_click4():
    # print("Button clicked!")
    top.destroy()
    import mercides

def on_button_click5():
    # print("Button clicked!")
    top.destroy()
    import jagbur

def on_button_click6():
    # print("Button clicked!")
    top.destroy()
    import BMW

def on_button_click7():
    # print("Button clicked!")
    top.destroy()
    import Audi




path="C:/Users/HH/Downloads/odi.jpeg"
img=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/Jaguar.jpeg"
img1=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/ta.jpeg"
img2=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/bmw.jpeg"
img3=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/suzuki.jpeg"
img4=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/mar.jpeg"
img5=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/h.jpeg"
img6=ImageTk.PhotoImage(Image.open(path))

path="C:/Users/HH/Downloads/kia.jpeg"
img7=ImageTk.PhotoImage(Image.open(path))







Audi = tk.Button(top, image=img,command=on_button_click7,width=260,height=260)
Audi.pack()
Audi.place(x=370,y=100)

jagbur = tk.Button(top, image=img1,command=on_button_click5,width=260,height=260)
jagbur.pack()
jagbur.place(x=30,y=100)

tata = tk.Button(top, image=img2,command=on_button_click1,width=260,height=260)
tata.pack()
tata.place(x=720,y=100)

bmw = tk.Button(top, image=img3,command=on_button_click6,width=260,height=260)
bmw.pack()
bmw.place(x=1070,y=100)

suzuki = tk.Button(top, image=img4,command=on_button_click3,width=260,height=260)
suzuki.pack()
suzuki.place(x=30,y=400)

mercides = tk.Button(top, image=img5,command=on_button_click4,width=260,height=260)
mercides.pack()
mercides.place(x=370,y=400)

honda = tk.Button(top, image=img6,command=on_button_click1,width=260,height=260)
honda.pack()
honda.place(x=720,y=400)

kia = tk.Button(top, image=img7,command=on_button_click2,width=260,height=260)
kia.pack()
kia.place(x=1070,y=400)



top.config(bg='black')
top.mainloop()