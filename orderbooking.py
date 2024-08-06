from tkinter import*
from PIL import Image,ImageTk
from tkinter import Tk, Label, PhotoImage
from tkinter import ttk
from tkinter import messagebox
from pymysql import Error
import random

top=Tk()
top.title('Orderbooking')
top.geometry('1200x600')

def price():
    k = e7.get()

    import pymysql as sql
    db = sql.connect(host='localhost',user='root',password='8860',db='pythonproject1')
    cur=db.cursor()
    s = "select * from carprice1 where car_models=%s"
    d = cur.execute(s,k)
    result=cur.fetchall()
    if d<=0:
        messagebox.showinfo("result","record not found")
    else:
        for i in tv.get_children():
            tv.delete(i)
        for row in result:  
            Brand_name = row[0]
            Car_models = row[1]
            Price = row[2]
            gst_price = row[3]
            
            tv.insert("",'end', values=(Brand_name,Car_models,Price,gst_price))



def insert():
    k5= e1.get()
    k6 = e6.get()
    k7 = e7.get()
    k8 = e5.get()
    k9 = clicked.get()

    k1 = e2.get()
    k2 = e3.get()
    k3 = e4.get()

   
    
   
    import pymysql as sql
    db = sql.connect(host='localhost',user='root',password='8860',db='pythonproject1')
    cur=db.cursor()  #cursor is a inbuild method exicute your query
    
    # s = "insert into booking values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5,k6,k7,k8,v)
    v = random.randint(1000,99999)
    s="insert into orders values('%s','%s','%s','%s','%s','%s')"%(v,k5,k6,k7,k8,k9)
    if(k8!='%s'):
        messagebox.showerror("Error","Please check your user id")
    s1="insert into persondetaile values('%s','%s','%s')"%(k1,k2,k3)
    
    result = cur.execute(s)
    result1 = cur.execute(s1)




    if result>0:
        messagebox.showinfo("Result","Your record insert successfull")
        messagebox.showinfo("order id",v)
        
    else:
        messagebox.showerror("Result","Record not inserted")
    db.commit()
    
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')
    e6.delete(0,'end')
    e7.delete(0,'end')
    e8.delete(0,'end')
    



tv = ttk.Treeview(top)
tv['column']=('brand_name', 'Car_models','Price','Gst_Price')
tv.column('#0',width=0, stretch=NO)
tv.column('brand_name',anchor=CENTER,width=100)
tv.column('Car_models',anchor=CENTER,width=150)
tv.column('Price',anchor=CENTER,width=120)
tv.column('Gst_Price',anchor=CENTER,width=80)


tv.heading('brand_name',text='Brand Name', anchor=CENTER)
tv.heading('Car_models',text='Car models ', anchor=CENTER)
tv.heading('Price',text='Price', anchor=CENTER)
tv.heading('Gst_Price',text='Gst_Price', anchor=CENTER)

tv.place(x=610,y=400)
# tv.place(x=610,y=0)

# path="C:/Users/HH/Downloads/bc.jpg"
# img=ImageTk.PhotoImage(Image.open(path))

# A1=Label(top,image=img)
# A1.pack()


l2 = Label(top,text='Name',fg='black',bg='white',font=('Arial 15 bold'))
l2.place(x=70,y=155)

e1 = Entry(top,font=('Arial 20 bold'))
e1.place(x=210,y=150)

l3 = Label(top,text='Father-Name',fg='black',bg="white",font=('Arial 15 bold'))
l3.place(x=70,y=205)

e2 = Entry(top,font=('Arial 20 bold'))
e2.place(x=210,y=200)

l4 = Label(top,text='Adhaar-No.',fg='black',bg='white',font=('Arial 15 bold'))
l4.place(x=70,y=260)

e3 = Entry(top,font=('Arial 20 bold'))
e3.place(x=210,y=255)

l4 = Label(top,text='DL-No.',fg='black',bg='white',font=('Arial 15 bold'))
l4.place(x=70,y=310)

e4 = Entry(top,font=('Arial 20 bold'))
e4.place(x=210,y=305)

l4 = Label(top,text='user_id',fg='black',bg='white',font=('Arial 15 bold'))
l4.place(x=70,y=365)

e5 = Entry(top, font=('Arial 20 bold'))
e5.place(x=210,y=360)

F3 = Frame(top,height=200, width=1200)
F3.place(x=80,y=462)

l21 = Label(top,text='Brand-Name',fg='black',bg='white',font=('Arial 12 bold'))
l21.place(x=600,y=150)

e6 = Entry(top,font=('Arial 15 bold'))
e6.place(x=760,y=150)

l3 = Label(top,text='Car-Model',fg='black',bg="white",font=('Arial 12 bold'))
l3.place(x=600,y=205)

e7 = Entry(top,font=('Arial 15 bold'))
e7.place(x=760,y=200)

l3 = Label(top,text='date(YYYY-MM-DD)',fg='black',bg="white",font=('Arial 12 bold'))
l3.place(x=600,y=260)

e8 = Entry(top,font=('Arial 15 bold'))
e8.place(x=760,y=260)


m = ['Select-State','Andhra Pradesh','Arunachal Pradesh','Assam',
     'Bihar','Chhattisgarh','Goa','Gujarat','	Haryana',
     'Himachal Pradesh','Jammu and Kashmir','Jharkhand','Gujarat',
     'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur',
     'Meghalaya','Mizoram','Nagaland','Odisha','Punjab',
     'Rajasthan','Sikkim','Tamil Nadu','Telangana',
     'Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
clicked = StringVar()
clicked.set('Select-state')



# cb = ttk.Combobox(top,state='readonly',values=m,font=('Arial 19 bold'))
drop = OptionMenu(top,clicked,*m)
# drop.pack()
drop.place(x=203,y=420)

# F1 = Frame(top,height=200, width=370,bg='green')
# F1.place(x=600,y=400)

b1 = Button(top,text='Submit', bg='green',font=('Arial 15 bold'),command=insert)
b1.place(x=300,y=600)

b2 = Button(top,text='Price', bg='blue',font=('Arial 15 bold'),command=price)
b2.place(x=800,y=600)



# top.config(bg='black')
top.mainloop()