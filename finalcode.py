import mysql.connector

from tkinter import *
from tkcalendar import DateEntry
root = Tk()
root.title('Myfirstapp')
root.geometry('600x600')
Rollnov = IntVar()
Label(root,text = "Rollno").grid(row = 0,column = 0)
Entry(root,textvariable = Rollnov).grid(row = 0,column = 1)
Rollnov.set('')

Namev = StringVar()
Label(root,text = "Name").grid(row = 1,column = 0)
Entry(root,textvariable = Namev).grid(row = 1,column = 1)

mark1v = IntVar()
Label(root,text = "Mark1").grid(row = 2,column = 0)
Entry(root,textvariable = mark1v).grid(row = 2,column = 1)
mark1v.set('')

mark2v = IntVar()
Label(root,text = "Mark2").grid(row = 3,column = 0)
Entry(root,textvariable = mark2v).grid(row = 3,column = 1)
mark2v.set('')

mark3v = IntVar()
Label(root,text = "Mark3").grid(row = 4,column = 0)
Entry(root,textvariable = mark3v).grid(row = 4,column = 1)
mark3v.set('')

def genderselection():
    gc = genderv.get()
    if gc == 1:
        return 'Male'
    else:
        return 'Female'

def savetodb():
    a = Rollnov.get()
    b = Namev.get()
    c = mark1v.get()
    d = mark2v.get()
    e = mark3v.get()
    total = c+d+e
    avg = total/3
    if total >= 290:
        g = 'A'
    elif total < 290 and total >= 250:
        g = 'B'
    elif total < 250 and total >= 200:
        g = 'C'
    else:
        g = 'D'
    ge = genderselection()
    dobv = dob.get_date()
    sv = statelistvar.get()
    ph = Phonenov.get()
    ci = []
    if c1.get() == 1:
        ci.append('Python')
    if c2.get() == 1:
        ci.append('SQL')
    if c3.get() == 1:
        ci.append('FullStack')
    if c4.get() == 1:
        ci.append('Java')
    print(ci)
    fci = '-'.join(ci)

    #print(a,b,c,d,e,total,avg,g,ge,dobv,sv,ph,fci)
    sql = f"insert into student values({a},'{b}',{c},{d},{e},'{dobv}',{ph},'{fci}','{sv}',{total},{avg},'{g}','{ge}')"
    connection = mysql.connector.connect(host='localhost', user='root', password='admin', database='training')
    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()
    cur.close()
    root.destroy()
    #print(sql)



genderv = IntVar()
Label(root,text = "Gender").grid(row = 5,column = 0)
Radiobutton(root,text = "Male",value = 1,variable= genderv,command = genderselection).grid(row = 5,column = 1)
Radiobutton(root,text = "Female",value = 2,variable=genderv, command = genderselection).grid(row = 5,column = 2)

dob = DateEntry(root)
Label(root,text = "DOB").grid(row =6,column = 0)
dob.grid(row = 6,column = 1)

Phonenov = IntVar()
Label(root,text = "Phoneno").grid(row = 7,column = 0)
Entry(root,textvariable = Phonenov).grid(row = 7,column = 1)
Phonenov.set('')

Label(root,text = 'State').grid(row= 8, column = 0)
statelist = ['TamilNadu','AP','Kerala','MP']
statelistvar = StringVar(root)
statelistvar.set('Choose your state')
OptionMenu(root,statelistvar,* statelist).grid(row = 8,column = 1)

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
Label(root, text = "Coures intersted").grid(row = 9, column = 0)
Checkbutton(root,text = "Python",onvalue=1,offvalue=0,variable=c1).grid(row = 9,column = 1)
Checkbutton(root,text = "SQL",onvalue=1,offvalue=0,variable=c2).grid(row = 9,column = 2)
Checkbutton(root,text = "FullStack",onvalue=1,offvalue=0,variable=c3).grid(row = 9,column = 3)
Checkbutton(root,text = "Java",onvalue=1,offvalue=0,variable=c4).grid(row = 9,column = 4)

Button(root,text = "Submit to database",command= savetodb).grid(row = 10,column = 1)
root.mainloop()
