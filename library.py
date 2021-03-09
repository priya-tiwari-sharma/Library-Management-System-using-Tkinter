from tkinter import *
import tkinter as tk
import datetime
import random
from tkinter import messagebox
import sqlite3
from tkinter import filedialog

d=sqlite3.connect("Library3.db")
c=d.cursor()

q=("create table if not exists Student3(MEMBER text,REFERENCE text,FIRSTNAME text, SURNAME text, ADDRESS text,PINCODE text,MOBILE integer,"
        "BOOKID text, TITLE text, AUTHOR text, BORROWED text,DATEDUE text,loandays text, RETURNFINE text)" )

c.execute(q)
d.commit()
d.close()


screen=Tk()
screen.config(bg='orange')
screen.title("library")
screen.geometry('1350x750+0+0')

#----------------frame

frame=Frame(screen)
frame['relief']=SUNKEN
frame.config(bg='grey')
frame.pack(fill=BOTH,expand=TRUE)


topframe=Frame(frame,relief=SUNKEN,bg='white',bd='10',borderwidth=10)
topframe.pack(side=TOP)

midframe=Frame(frame,relief=SUNKEN,bg='white',bd='10',borderwidth=10,padx=10,pady=10)
# midframe.pack(side=LEFT)
midframe.place(x=0,y=100)

rightframe=Frame(frame,relief=SUNKEN,bg='white',bd='10',borderwidth=10,padx=10,pady=10)
# rightframe.pack(side=RIGHT)
rightframe.place(x=750,y=100)
#------------------------------------title library
titlelib=Label(topframe,text='LIBRARY DATABASE MANAGEMENT SYSTEM',font=('bold',45),bg='pink')
titlelib.grid(row=0,column=0)

#-------------------------------------lable and entry

l1=Label(midframe,text='LIBRARY MEMBERSHIP INFO***',relief=SUNKEN,font=('bold',8),fg='blue',bd=15,borderwidth=10)
l1.grid(row=0,column=0)

l2=Label(midframe,text='MEMBER TYPE',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l2.grid(row=1,column=0,sticky=W)

l3=Label(midframe,text='REFRENCE NO',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l3.grid(row=2,column=0,sticky=W)

l4=Label(midframe,text='First Name',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l4.grid(row=3,column=0,sticky=W)

l5=Label(midframe,text='SURNAME',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l5.grid(row=4,column=0,sticky=W)

l6=Label(midframe,text='ADDRESS',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l6.grid(row=5,column=0,sticky=W)

l7=Label(midframe,text='PINCODE',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l7.grid(row=6,column=0,sticky=W)

l8=Label(midframe,text='MOBILE NO:',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l8.grid(row=7,column=0,sticky=W)


e1=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e1.grid(row=1,column=1)
e1.insert(0,0)


e2=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e2.grid(row=2,column=1)
e2.insert(0,0)


e3=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e3.grid(row=3,column=1)
e3.insert(0,0)


e4=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e4.grid(row=4,column=1)
e4.insert(0,0)

e5=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e5.grid(row=5,column=1)
e5.insert(0,0)

e6=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e6.grid(row=6,column=1)
e6.insert(0,0)


e7=Entry(midframe,borderwidth=10,bg='grey',fg='yellow')
e7.grid(row=7,column=1)
e7.insert(0,0)

#***********************************************2nd on leftframe

l9=Label(midframe,text='BOOK ID',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l9.grid(row=1,column=2,sticky=W)

l10=Label(midframe,text='BOOK TITLE',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l10.grid(row=2,column=2,sticky=W)

l11=Label(midframe,text='AUTHOR',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l11.grid(row=3,column=2,sticky=W)

l12=Label(midframe,text='DATE BORROWED',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l12.grid(row=4,column=2,sticky=W)

l13=Label(midframe,text='DATE DUE',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l13.grid(row=5,column=2,sticky=W)

l14=Label(midframe,text='DAYS OF LOAN',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l14.grid(row=6,column=2,sticky=W)

l15=Label(midframe,text='LATE RETURN FINE',relief=SUNKEN,font=('bold',18),bd=15,borderwidth=10)
l15.grid(row=7,column=2,sticky=W)


e8=Entry(midframe,borderwidth=10,bg='grey')
e8.grid(row=1,column=3)
e8.insert(0,0)


e9=Entry(midframe,borderwidth=10,bg='grey')
e9.grid(row=2,column=3)
e9.insert(0,0)


e10=Entry(midframe,borderwidth=10,bg='grey')
e10.grid(row=3,column=3)
e10.insert(0,0)


e11=Entry(midframe,borderwidth=10,bg='grey')
e11.grid(row=4,column=3)
e11.insert(0,0)

e12=Entry(midframe,borderwidth=10,bg='grey')
e12.grid(row=5,column=3)
e12.insert(0,0)

e13=Entry(midframe,borderwidth=10,bg='grey')
e13.grid(row=6,column=3)
e13.insert(0,0)


e14=Entry(midframe,borderwidth=10,bg='grey')
e14.grid(row=7,column=3)
e14.insert(0,0)

#--------------------------------------------------RECEIPT

scrollbar=Scrollbar(rightframe)
scrollbar.grid(row=0,column=1,sticky=NS)

scrollbar1=Scrollbar(rightframe,orient=HORIZONTAL)
scrollbar1.grid(row=1,column=0,sticky=EW)

booklist=Listbox(rightframe,height=23,width=85,bd=10,borderwidth=5,yscrollcommand=scrollbar.set)
# booklist.bind('<<listboxSelect>>',selectedbook)
booklist.grid(row=0,column=0)
scrollbar.config(command=booklist.yview)

booklist=Listbox(rightframe,height=23,width=85,bd=10,borderwidth=5,xscrollcommand=scrollbar1.set)
booklist.grid(row=0,column=0)
scrollbar1.config(command=booklist.xview)



#--------------------------------------
bottomframe=Frame(frame,relief=RAISED,bd=10,borderwidth=5,bg='white',padx=20,pady=20)
bottomframe.pack(side=BOTTOM)
#bottomframe.place(x=0,y=400)

ba=Button(frame,bg='orange',text='   ADD DATA   ',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda:add1())
#ba.grid(row=18,column=0)
ba.place(x=120,y=530)

bd=Button(frame,text='DISPLAY DATA',bg='orange',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda:display1())
# bd.grid(row=18,column=1)
bd.place(x=350,y=530)

bc=Button(frame,bg='orange',text='CLEAR DATA',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda:clear1())
bc.place(x=600,y=530)

bS=Button(frame,bg='orange',text=' SEARCH DATA  ',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda :search1())
bS.place(x=90,y=610)

bu=Button(frame,bg='orange',text='UPDATE DATA',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda:selectedbook())
bu.place(x=350,y=610)

bD=Button(frame,bg='orange',text='DELETE DATA',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda :delete1())
bD.place(x=600,y=610)

be=Button(frame,bg='red',text='     EXIT    ',font=('bold',20),relief=RAISED,bd=20,borderwidth=10,command=lambda :exit1())
be.place(x=900,y=610)


#------------------------------------exit command

def exit1():
    response=tk.messagebox.askyesno("EXIT WINDOW",'Do you want to EXIT?')
    if response==1:
        screen.destroy()
        return


#----------------------------------clear data

def clear1():

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)

    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)

    e1.insert(0,'0')
    e2.insert(0,'0')
    e3.insert(0,'0')
    e4.insert(0,'0')
    e5.insert(0,'0')
    e6.insert(0,'0')
    e7.insert(0,'0')
    e8.insert(0,'0')
    e9.insert(0,'0')
    e10.insert(0,'0')
    e11.insert(0,'0')
    e12.insert(0,'0')
    e13.insert(0,'0')
    e14.insert(0,'0')
    booklist.delete(0,END)




#------------------------------------data base adding data

def add1():

    r1=tk.messagebox.askokcancel('DATA','DATA has been successfully added')
    d=sqlite3.connect("Library3.db")
    c=d.cursor()

    item1=e1.get()



    q=("create table if not exists Student3(MEMBER text,REFERENCE text,FIRSTNAME text, SURNAME text, ADDRESS text,PINCODE text,MOBILE integer,"
        "BOOKID text, TITLE text, AUTHOR text, BORROWED text,DATEDUE text,loandays text, RETURNFINE text)" )
    c.execute(q)

    c.execute("insert into Student3(MEMBER ,REFERENCE ,FIRSTNAME , SURNAME , ADDRESS ,PINCODE ,MOBILE,BOOKID , TITLE , AUTHOR , BORROWED ,DATEDUE ,loandays , RETURNFINE)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()
        ,e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get()))

    booklist.delete(0,END)
    booklist.insert(END,"MEMBER TYPE="+e1.get()+",REFRENCE NO="+e2.get()+",FIRST NAME ="+e3.get()+",SURNAME="+e4.get()+"ADDRESS="+e5.get()+"PINCODE="+e6.get()
                    +",MOBILE NO=="+e7.get()+",BOOK ID="+e8.get()+"BOOK TITLE="+e9.get()+"AUTHOR="+e10.get()+"DATE BORROWED"+e11.get()+"DATE DUE"+e12.get()
                    +"DAYS OF LOAN"+e13.get()+"LATE RETURN FINE"+e14.get())




    d.commit()
    d.close()

#---------------------------------DISPLAY DATA

def display1():



    d=sqlite3.connect("Library3.db")
    c=d.cursor()

    c.execute("select * from Student3")
    record=c.fetchall()
    d.commit()
    d.close()

    for i in record:
        booklist.insert(END,i)



#---------------------------------------------update data

def selectedbook():
    global sb
    searchbk=booklist.curselection()[0]
    sb=booklist.get(searchbk)

    e1.delete(0,END)
    e1.insert(END,sb[0])
    e2.delete(0,END)
    e2.insert(END,sb[1])
    e3.delete(0,END)
    e3.insert(END,sb[2])
    e4.delete(0,END)
    e4.insert(END,sb[3])
    e5.delete(0,END)
    e5.insert(END,sb[4])
    e6.delete(0,END)
    e6.insert(END,sb[5])
    e7.delete(0,END)
    e7.insert(END,sb[6])
    e8.delete(0,END)
    e8.insert(END,sb[7])

    e9.delete(0,END)
    e9.insert(END,sb[8])
    e10.delete(0,END)
    e10.insert(END,sb[9])
    e11.delete(0,END)
    e11.insert(END,sb[10])
    e12.delete(0,END)
    e12.insert(END,sb[11])

    e13.delete(0,END)
    e13.insert(END,sb[12])
    e14.delete(0,END)
    e14.insert(END,sb[13])

#-----------------------------------------------DELETE DATA

d=sqlite3.connect("Library3.db")
c=d.cursor()

q=("create table if not exists Student3(MEMBER text,REFERENCE text,FIRSTNAME text, SURNAME text, ADDRESS text,PINCODE text,MOBILE integer,"
        "BOOKID text, TITLE text, AUTHOR text, BORROWED text,DATEDUE text,loandays text, RETURNFINE text)" )

c.execute(q)
d.commit()
d.close()

def delete1(MEMBER='',REFERENCE='',FIRSTNAME='', SURNAME='' , ADDRESS='',PINCODE='',MOBILE='',BOOKID='', TITLE='', AUTHOR='', BORROWED='',DATEDUE='',loandays='', RETURNFINE=''):


    d=sqlite3.connect("Library3.db")
    c=d.cursor()

    c.execute("DELETE from Student3 WHERE MEMBER=? OR REFERENCE=? OR FIRSTNAME=? OR SURNAME=? OR ADDRESS=? OR PINCODE=? OR MOBILE=? OR BOOKID=? OR TITLE=? OR AUTHOR=? OR BORROWED=? OR DATEDUE=? OR loandays=? OR RETURNFINE=?",\
              (MEMBER ,REFERENCE ,FIRSTNAME , SURNAME , ADDRESS ,PINCODE ,MOBILE,BOOKID , TITLE , AUTHOR , BORROWED ,DATEDUE ,loandays , RETURNFINE))


    d.commit()
    d.close()


    clear1()
    display1()

#------------------------------------------SEARCH DATA
def search1(MEMBER='',REFERENCE='',FIRSTNAME='', SURNAME='' , ADDRESS='',PINCODE='',MOBILE='',BOOKID='', TITLE='', AUTHOR='', BORROWED='',DATEDUE='',loandays='', RETURNFINE=''):


    d=sqlite3.connect("Library3.db")
    c=d.cursor()

    c.execute("SELECT * from Student3 WHERE MEMBER=? OR REFERENCE=? OR FIRSTNAME=? OR SURNAME=? OR ADDRESS=? OR PINCODE=? OR MOBILE=? OR BOOKID=? OR TITLE=? OR AUTHOR=? OR BORROWED=? OR DATEDUE=? OR loandays=? OR RETURNFINE=?",\
              (MEMBER ,REFERENCE ,FIRSTNAME , SURNAME , ADDRESS ,PINCODE ,MOBILE,BOOKID , TITLE , AUTHOR , BORROWED ,DATEDUE ,loandays , RETURNFINE))

    row=c.fetchall()


    d.commit()
    d.close()

    for i in row:
        booklist.insert(END,i)






#----------------------------------------------------------
screen.mainloop()
