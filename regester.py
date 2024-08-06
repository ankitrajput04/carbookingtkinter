from tkinter import*
from PIL import Image,ImageTk
from tkinter import Tk, Label, PhotoImage
from tkinter import ttk
from tkinter import messagebox
import random

top=Tk()
top.title('ankit')
top.geometry('1200x600')

def insert():
    k = e1.get()
    k2 = e2.get()
    k3 = e3.get()
   
    import pymysql as sql
    db = sql.connect(host='localhost',user='root',password='8860',db='pythonproject1')
    cur=db.cursor()  #cursor is a inbuild method exicute your query
    

    v = random.randint(1000,99999)
    s="insert into car3 values('%s','%s','%s','%s')"%(k,k2,v,k3)
    reuslt = cur.execute(s)


    if reuslt>0:
        messagebox.showinfo("Result","Your record insert successfully")
        messagebox.showinfo("regestration_id",v)
    else:
        messagebox.showinfo("Result","Record not inserted")
    db.commit()
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')

# path="C:/Users/HH/Downloads/Screenshot_23-7-2024_14412_www.bing.com.jpeg"
# img = ImageTk.PhotoImage(Image.open(path))

# l7 =Label(top,image=img)
# l7.pack()

path="C:/Users/HH/Downloads/bc.jpg"
img=ImageTk.PhotoImage(Image.open(path))

l4=Label(top,image=img)
l4.pack()


def login():
    top.destroy()
    import login




l1 = Label(top,text='Admin-registration',bg='white',font=('Arial 20 bold'))
l1.place(x=550,y=10)

l2 = Label(top,text='Name',fg='black',bg='white',font=('Arial 10 bold'))
l2.place(x=10,y=20)

e1 = Entry(top,font=('Arial 15 bold'))
e1.place(x=90,y=20)

l3 = Label(top,text='Email',fg='black',bg="white",font=('Arial 10 bold'))
l3.place(x=10,y=65)

e2 = Entry(top,font=('Arial 15 bold'))
e2.place(x=90,y=65)

l4 = Label(top,text='Password',fg='black',bg='white',font=('Arial 10 bold'))
l4.place(x=10,y=110)

e3 = Entry(top,font=('Arial 15 bold'),show='*')
e3.place(x=90,y=110)

b1 = Button(top,text='SignUp', bg='yellow',font=('Arial 10 bold'),command=insert)
b1.place(x=120,y=150)

b2 = Button(top,text='Login',bg='green',font=('Arial 10 bold'),command=login)
b2.place(x=200,y=150)

# top.config(bg='green')
top.mainloop()