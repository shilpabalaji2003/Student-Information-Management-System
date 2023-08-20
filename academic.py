from tkinter import *
import mysql.connector as c


db=c.connect(host='localhost', user='root', passwd='shilpa', database='project')
mc=db.cursor()
    


def display(c,d):           #To display all records of the class
    x=str(c)
    y=str(d)
    a=Toplevel()
    a.title("Academic records")
    mc.execute("use project")
    query="select * from students1 where class='{}' and section='{}'".format(x,y)
    mc.execute(query)
    
    L=[("ADMISSION NUMBER", "NAME", "CLASS", "SECTION", "TERM 1 MARKS", "TERM 2 MARKS", "TERM 3 MARKS")]

    for t in mc:
        L.append(t)

    row=len(L)
    col=len(L[0])

    for i in range(row):
        for j in range(col):
            e=Entry(a, width=20)
            e.insert(0, L[i][j])
            e.grid(row=i, column=j)

def update(grade, section):     #To ask for details to be updated
    global b
    b=Toplevel()
    b.title("Update records")
    b.geometry("450x500")

    sname=Label(b, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).grid(row=0, column=0, columnspan=2)

    select=Label(b, text="Select the admission number of the student to be updated: ", pady=20).grid(row=1, column=0)

    query="select admissionno from students1 where class='{}' and section='{}'".format(grade, section)

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

    optns=["Term1marks",
           "Term2marks",
           "Term3marks"]

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

    p=var_op.get()
    q=entry_field.get()

    r="admissionno"
    s=int(var.get())

   
    query="update students1 set {}='{}' where {}={}".format(p, q, r, s)

    mc.execute(query)
    db.commit()

            
    L=[("ADMISSION NUMBER", "NAME", "CLASS", "SECTION", "TERM 1 MARKS", "TERM 2 MARKS", "TERM 3 MARKS")]

    query3="select * from students1 where admissionno={}".format(s,)
    mc.execute(query3)

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
                    "Term1marks",
                    "Term2marks",
                    "Term3marks"]

    global s_var
    s_var=StringVar()
    s_var.set(search_options[0])

    search_menu=OptionMenu(d, s_var, *search_options)
    search_menu.grid(row=1, column=1, sticky=E)

    go_btn=Button(d, text="NEXT", bg="light green", command=srch_op).grid(row=2, columnspan=2)

def srch_op():
    x=s_var.get()
    sel=Label(d, text="Select the"+" "+s_var.get()+" "+"of the student to be searched", pady=20).grid(row=3, column=0, sticky=W)

    query1="select distinct {} from students1 where class='{}' and section='{}'".format(x, grade, section)

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

    query="select * from students1 where class='{}' and section='{}' and {}='{}'".format(grade, section, x, y)

    mc.execute(query)

    srch_rec=[("ADMISSION NUMBER", "NAME", "CLASS", "SECTION", "TERM 1 MARKS", "TERM 2 MARKS", "TERM 3 MARKS")]

    for i in mc:
        srch_rec.append(i)

    row=len(srch_rec)
    col=len(srch_rec[0])

    for i in range(row):
        for j in range(col):
            data=Entry(e, width=20)
            data.insert(0, srch_rec[i][j])
            data.grid(row=i, column=j)


def add1(g, s):
    global grade, sec
    grade=g
    sec=s
    
    global f
    f=Toplevel()
    f.title("Add Records")
    f.geometry("800x500")

    sname=Label(f, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).grid(row=0, column=0, columnspan=2)

    global e_name, e_t1, e_t2, e_t3, e_fname, e_mname, e_phno, e_address

    name=Label(f, text="Enter the name of the student: ", pady=10).grid(row=1, column=0, sticky=W)

    e_name=Entry(f, width=20)
    e_name.grid(row=1, column=1)

    t1=Label(f, text="Enter the Term 1 marks of the student: ", pady=10).grid(row=2, column=0)

    e_t1=Entry(f, width=20)
    e_t1.grid(row=2, column=1)

    t2=Label(f, text="Enter the Term 2 marks of the student: ", pady=10).grid(row=3, column=0)

    e_t2=Entry(f, width=20)
    e_t2.grid(row=3, column=1)

    t3=Label(f, text="Enter the Term 3 marks of the student: ", pady=10).grid(row=4, column=0)

    e_t3=Entry(f, width=20)
    e_t3.grid(row=4, column=1)

    fname=Label(f, text="Enter the name of the father: ", pady=10).grid(row=5, column=0, sticky=W)

    e_fname=Entry(f, width=20)
    e_fname.grid(row=5, column=1)

    mname=Label(f, text="Enter the name of the mother: ", pady=10).grid(row=6, column=0, sticky=W)

    e_mname=Entry(f, width=20)
    e_mname.grid(row=6, column=1)

    phno=Label(f, text="Enter the phone number of the student: ", pady=10).grid(row=7, column=0, sticky=W)

    e_phno=Entry(f, width=20)
    e_phno.grid(row=7, column=1)

    address=Label(f, text="Enter the address of the student: ", pady=10).grid(row=8, column=0, sticky=W)

    e_address=Entry(f, width=20)
    e_address.grid(row=8, column=1)

    go_btn=Button(f, text="NEXT", bg="light green", command=add2).grid(row=9, columnspan=2)


def add2():
    done=Label(f, text="RECORD HAS BEEN ADDED SUCCESSFULLY!", pady=20, fg="green").grid(row=10, sticky=W, columnspan=2)
    done2=Label(f, text="PLEASE RESTART THE APPLICATION TO VIEW THE CHANGES", fg="green").grid(row=11, sticky=W, columnspan=2)
    
    query0="select max(admissionno) from students1".format(grade, sec)
    mc.execute(query0)
    
    for i in mc:
        for j in i:
            a=j+1
            
    p=e_name.get()
    q=e_t1.get()
    r=e_t2.get()
    s=e_t3.get()
    t=e_fname.get()
    u=e_mname.get()
    v=e_phno.get()
    w=e_address.get()
    
    query1="insert into students1 values( {}, '{}', '{}', '{}', {}, {}, {} )".format(a, p, grade, sec, q, r, s)
    

    query2="insert into personal_information values( {}, '{}', '{}', '{}', '{}', '{}', {}, '{}' )".format(a, p, grade, sec, t, u, v, w)

    mc.execute(query1)
    db.commit()
    
    mc.execute(query2)
    db.commit()


def delete(a, b):
    global g
    g=Toplevel()
    g.title("Delete Records")

    sname=Label(g, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).grid(row=0, column=0, columnspan=2)

    select=Label(g, text="Select the admission number of the student to be deleted: ", pady=20).grid(row=1, column=0)

    query="select admissionno from students1 where class='{}' and section='{}'".format(a, b)

    mc.execute(query)

    admno=[]

    for i in mc:
        for j in i:
            admno.append(j)

    global del_var
    del_var=StringVar()
    del_var.set(admno[0])

    options_admno=OptionMenu(g, del_var, *admno)
    options_admno.grid(row=1, column=1)

    go_btn=Button(g, text="NEXT", bg="light green", command=remove).grid(row=2, columnspan=2)


def remove():
    done1=Label(g, text="The record having Admission Number"+" "+del_var.get()+" has been deleted. Please restart the application to view the changes.", pady=20).grid(row=3, columnspan=2)

    query1="delete from students1 where admissionno={}".format(del_var.get())

    query2="delete from personal_information where admissionno={}".format(del_var.get())

    mc.execute(query1)
    db.commit()

    mc.execute(query2)
    db.commit()
    

    


