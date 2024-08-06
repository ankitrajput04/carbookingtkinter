from tkinter import*
from tkinter import Tk, Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import os


root =Tk()
root.title('Welcome')
root.geometry('1200x600')




def singin():
    import pymysql as sql
    db = sql.connect(host='localhost',user='root',password='8860',db='pythonproject1')
    cur=db.cursor()

    cur.execute("select * from car3 where username=%s and password=%s",(e1.get(),e2.get()))
    row = cur.fetchone()

    if row is None:
        messagebox.showerror("Error", "Invalid username password")
    else:
        root.destroy()
        os.system("python logos.py")
        

path="C:/Users/HH/Downloads/bc.jpg"
img=ImageTk.PhotoImage(Image.open(path))

A2=Label(root,image=img)
A2.pack()
l1 = Label(root,text='LogIn',bg='white',font=('Arial 20 bold'))
l1.place(x=650,y=10)

l2 = Label(root,text='Username',fg='black',bg='white',font=('Arial 10 bold'))
l2.place(x=40,y=34)

e1 = Entry(root,font=('Arial 15 bold'))
e1.place(x=120,y=30)

l3 = Label(root,text='Password',fg='black',bg='white',font=('Arial 10 bold'))
l3.place(x=40,y=80)

e2 = Entry(root,font=('Arial 15 bold'),show='*')
e2.place(x=120,y=76)

b1 = Button(root,text='SignIn', bg='green',font=('Arial 10 bold'),command=singin)
b1.place(x=200,y=120)


# top.config(bg='green')
root.mainloop()