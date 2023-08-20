from tkinter import *
import mysql.connector as c

db=c.connect(host='localhost', user='root', passwd='shilpa', database='project')
mc=db.cursor()


def display(c,d):
    a=Toplevel()
    a.title("Personal Records")

    query="select * from personal_information where class='{}' and section='{}'".format(c,d)

    mc.execute(query)

    L=[("ADMISSIONNO", "NAME", "CLASS", "SECTION", "FATHERSNAME", "MOTHERSNAME", "PHONENUMBER", "ADDRESS")]

    for t in mc:
        L.append(t)

    row=len(L)
    col=len(L[0])

    for i in range (row):
        for j in range(col):
            e=Entry(a, width=20)
            e.insert(0, L[i][j])
            e.grid(row=i, column=j)

def update(grade, section):     #To ask for details to be updated
    global b
    b=Toplevel()
    b.title("Personal records")
    b.geometry("450x500")

    sname=Label(b, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).grid(row=0, column=0, columnspan=2)

    select=Label(b, text="Select the admission number of the student to be updated: ", pady=20).grid(row=1, column=0)

    query="select admissionno from personal_information where class='{}' and section='{}'".format(grade, section)

    mc.execute(query)

    admno=[]

    for i in mc:
        for j in i:
            admno.append(j)

    global var
    var=StringVar()
    var.set(admno[0])

    options_admno=OptionMenu(b, var, *admno)
    options_admno.grid(row=1, column=1)

    go_btn=Button(b, text="NEXT", bg="light green", command=options_update).grid(row=2, columnspan=2)


def options_update():       #To ask for field name to be updated
    lbl=Label(b, text="Select a field to be updated: ", pady=20).grid(row=3, column=0, sticky=W)

    optns=["Name",
           "Class",
           "Section",
           "Fathersname",
           "Mothersname",
           "Phonenumber",
           "Address"]

    global var_op
    var_op=StringVar()
    var_op.set(optns[0])

    options_field=OptionMenu(b, var_op, *optns)
    options_field.grid(row=3, column=1)

    go_btn=Button(b, text="NEXT", bg="light green", command=updated).grid(row=4, columnspan=2)

    

def updated():      #To enter the new value
    lbl1=Label(b, text="Enter the new"+" "+var_op.get(), pady=20).grid(row=5, column=0, sticky=W)

    global entry_field
    entry_field=Entry(b, width=20)
    entry_field.grid(row=5, column=1)

    go_btn=Button(b, text="NEXT", bg="light green", command=upd_disp).grid(row=6, columnspan=2)

    

def upd_disp():     #To display that record after updation
    c=Toplevel()
    c.title("Update")

    success=Label(c, text="Record has been successfully updated!", pady=20, fg="green").grid(row=2, columnspan=7)

    p=var_op.get()          #What the user selected to update
    q=entry_field.get()     #New record entered by the user

    r="admissionno"
    s=int(var.get())    #Admission number selected by the user
    

    query1="update personal_information set {}='{}' where {}={}".format(p, q, r, s)

    mc.execute(query1)

    db.commit()

    L=[("ADMISSION NUMBER", "NAME", "CLASS", "SECTION", "FATHERSNAME", "MOTHERSNAME", "PHONENUMBER", "ADDRESS")]

    query2="select * from personal_information where admissionno={}".format(s,)
    mc.execute(query2)

    for x in mc:
        L.append(x)

    row=len(L)
    col=len(L[0])

    for i in range(row):
        for j in range(col):
            data=Entry(c, width=20)
            data.insert(0, L[i][j])
            data.grid(row=i, column=j)


def search(g,s):
    global grade
    global section
    grade=g
    section=s
    
    global d
    d=Toplevel()
    d.geometry("500x500")
    d.title("Search Records")

    sname=Label(d, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).grid(row=0, column=0, columnspan=2)

    search_by=Label(d, text="Search by: ", pady=20).grid(row=1, column=0, sticky=W)

    search_options=["Admissionno",
                    "Name",
                    "Fathersname",
                    "Mothersname",
                    "Phonenumber",
                    "Address"]

    global s_var
    s_var=StringVar()
    s_var.set(search_options[0])

    search_menu=OptionMenu(d, s_var, *search_options)
    search_menu.grid(row=1, column=1, sticky=E)

    go_btn=Button(d, text="NEXT", bg="light green", command=srch_op).grid(row=2, columnspan=2)

def srch_op():
    x=s_var.get()
    sel=Label(d, text="Select the"+" "+s_var.get()+" "+"of the student to be searched", pady=20).grid(row=3, column=0, sticky=W)

    query1="select distinct {} from personal_information where class='{}' and section='{}'".format(x, grade, section)

    mc.execute(query1)

    val=[]

    for i in mc:
        for j in i:
            val.append(j)
            
    global select_var
    select_var=StringVar()
    select_var.set(val[0])

    value_menu=OptionMenu(d, select_var, *val)
    value_menu.grid(row=3, column=1, sticky=E)

    go_btn=Button(d, text="NEXT", bg="light green", command=srch_disp).grid(row=4, columnspan=2)


def srch_disp():
    x=s_var.get()
    y=select_var.get()
    
    e=Toplevel()
    e.title("Search Records")

    query="select * from personal_information where class='{}' and section='{}' and {}='{}'".format(grade, section, x, y)

    mc.execute(query)

    srch_rec=[("ADMISSION NUMBER", "NAME", "CLASS", "SECTION", "FATHERSNAME", "MOTHERSNAME", "PHONENUMBER", "ADDRESS")]

    for i in mc:
        srch_rec.append(i)

    row=len(srch_rec)
    col=len(srch_rec[0])

    for i in range(row):
        for j in range(col):
            data=Entry(e, width=20)
            data.insert(0, srch_rec[i][j])
            data.grid(row=i, column=j)





    
