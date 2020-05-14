from tkinter import *
import pymysql
import tkinter.messagebox as mb
import time
import datetime as dt




def date():
        date = dt.datetime.now()
        format_date = f"{date:%a, %b %d %Y}"
        label3 ["text"]=format_date
        print(date)

        
def clock():
    current=time.strftime("%H:%M:%S")
    label1 ["text"]=current
    root.after(1000,clock)

def quit():
        ques=mb.askquestion("Quit","Are You Sure You Want To Quit")
        if ques=="yes":
                root.destroy()


def clear():
        name1.delete(0,END)
        class1.delete(0,END)
        address1.delete(0,END)
        adm_no1.delete(0,END)
        phone_no1.delete(0,END)
        dob1.delete(0,END)
        


def delete():
        name=name1.get()
        class2=class1.get()
        address=address1.get()
        adm_no=adm_no1.get()
        phone_no=phone_no1.get()
        dob=dob1.get()
        con=pymysql.connect(host="localhost",user="root",password="123",db="students_of_nhs")
        cursor=con.cursor()
        cursor.execute("delete from student_of_class11 where Adm_no='"+adm_no1.get()+"'")
        ques=mb.askquestion("Delete","Are You Sure You Want To Delete Data")
        if ques=="yes":
                cursor.execute("commit");
                show()
                mb.showinfo("Deleted","Data Sucessfully Deleted")
     


def update():
        name=name1.get()
        class2=class1.get()
        address=address1.get()
        adm_no=adm_no1.get()
        phone_no=phone_no1.get()
        dob=dob1.get()
        if name1=="" or class1=="" or address1=="" or adm_no=="" or phone_no1=="" or dob=="":
                 mb.showinfo("Error","All Field Required")

        else:
                con=pymysql.connect(host="localhost",user="root",password="123",db="students_of_nhs")
                cursor=con.cursor()
                cursor.execute("Update student_of_class11 set Name='"+ name +"',Class='"+ class2 +"',Phone_No='"+ phone_no +"',Address='"+ address +"',DOB='"+ dob +"' where Adm_no='"+ adm_no +"'")
                cursor.execute("commit");
                show()
                mb.showinfo("Updated","Data Sucessfully Updated")



def insert():
    name=name1.get()
    class2=class1.get()
    address=address1.get()
    adm_no=adm_no1.get()
    phone_no=phone_no1.get()
    dob=dob1.get()
    con=pymysql.connect(host="localhost",user="root",password="123",db="students_of_nhs")
    cursor=con.cursor()
    cursor.execute("insert into student_of_class11 values('"+name +"','"+adm_no +"','"+class2 +"','"+phone_no+"','"+address +"','"+ dob +"')")
    cursor.execute("commit");
    show()
    mb.showinfo("Inserted","Data Sucessfully Inserted")




def show():
    con=pymysql.connect(host="localhost",user="root",password="123",db="students_of_nhs")
    cursor=con.cursor()
    cursor.execute("select * from student_of_class11 ")
    row=cursor.fetchall()
    list1.delete(0,list1.size())

    for row in row:
        insertData=str(row[0])+'        '+row[1]+'      '+row[2]+'      '+row[3]+'      ' +row[4]+'     ' +row[5]+'  '
        list1.insert(list1.size()+1,insertData)

    

def get():
    name=name1.get()
    class2=class1.get()
    address=address1.get()
    adm_no=adm_no1.get()
    phone_no=phone_no1.get()
    dob=dob1.get()
    con=pymysql.connect(host="localhost",user="root",password="123",db="students_of_nhs")
    cursor=con.cursor()
    cursor.execute("select * from student_of_class11 where Adm_no='"+adm_no1.get()+"'")
    row=cursor.fetchall()
    for row in row:
        name1.insert(0,row[0])
        address1.insert(0,row[2])
        class1.insert(0,row[3])
        phone_no1.insert(0,row[4])
        dob1.insert(0,row[5])

   

    

root=Tk()
root.title("Student Management System")
root.geometry("800x500")
root.minsize(800,500)
root.maxsize(800,500)

#Side Frame

sideframe=Frame(root,bd="5",height="800",width="160",bg="black")
sideframe.place(x=0,y=0)


#Top Frame
topframe=Frame(root,bd="5",height="100",width="800",bg="#F8CF35")
topframe.place(x=0,y=0)
studentlabel=Label(topframe,text="Student Details",font="arial 25 bold",bg="#F8CF35")
studentlabel.place(x=300,y=10)
label1=Label(root,font="article 14 bold",bg="#F8CF35",fg="black")
label1.place(x=250,y=70)
label2=Label(root,text="Time : ",font="article 14 bold",bg="#F8CF35",fg="black")
label2.place(x=178,y=70)
clock()


label3=Label(root,text="Time : ",font="article 14 bold",bg="#F8CF35",fg="black")
label3.place(x=500,y=70)
date()




#Button
insert=Button(sideframe,text="Insert",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=insert)
insert.place(x=35,y=120)

update=Button(sideframe,text="Update",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=update)
update.place(x=35,y=180)

delete=Button(sideframe,text="Delete",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=delete)
delete.place(x=35,y=240)

get=Button(sideframe,text="Get",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=get)
get.place(x=35,y=300)

clear=Button(sideframe,text="Clear",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=clear)
clear.place(x=35,y=360)

quit1=Button(sideframe,text="Quit",bg="#F8CF35",font="arial 12 bold",height="1",width="7",command=quit)
quit1.place(x=35,y=420)

#Main Area

name1=Entry(root,bd=5)
name1.place(x=300,y=150)

class1=Entry(root,bd=5)
class1.place(x=300,y=230)

address1=Entry(root,bd=5)
address1.place(x=300,y=310)

adm_no1=Entry(root,bd=5)
adm_no1.place(x=600,y=150)

phone_no1=Entry(root,bd=5)
phone_no1.place(x=600,y=230)

dob1=Entry(root,bd=5)
dob1.place(x=600,y=310)

#Labels


name=Label(root,text="Student Name",font="arial 11 bold")
name.place(x=180,y=150)

adm_no=Label(root,text="Admission No",font="arial 11 bold")
adm_no.place(x=480,y=150)

class3=Label(root,text="Class",font="arial 11 bold")
class3.place(x=180,y=230)

phone_no=Label(root,text="Phone Number",font="arial 11 bold")
phone_no.place(x=480,y=230)

address=Label(root,text="City",font="arial 11 bold")
address.place(x=180,y=310)

dob=Label(root,text="Date Of Birth",font="arial 11 bold")
dob.place(x=480,y=310)




#List Box
list1=Listbox(root,height="9",width="64")
list1.place(x=330,y=350)
show()

root.mainloop()
