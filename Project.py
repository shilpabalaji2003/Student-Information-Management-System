#Student Information Management System

from tkinter import *
from tkinter import messagebox
from project import academic
from project import personal

global root
root=Tk()                       #Main window
root.title("Student Information Management System")
root.geometry("500x500")

sname=Label(root, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10)
sname.pack()

login=Label(root, text="LOGIN", pady=30)
login.pack()

info_frame=LabelFrame(root, text="Info", pady=10)
info_frame.pack(side=BOTTOM, anchor=W)

#Buttons inside the frame in main window
def vision():
    vision=Toplevel()
    vision.geometry("700x300")
    vision.title("Our Vision")

    sname=Label(vision, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).pack()

    v1=Label(vision, text="OUR VISION").pack()
    v2=Label(vision, text='"Striving for excellence, striding towards success and seeking new horizons of personal growth and worth"', pady=10).pack()
    

def rate():
    rate=Toplevel()
    rate.title("Rate Us")
    rate.geometry("300x300")

    sc=Scale(rate, from_=0, to=5, orient=HORIZONTAL)
    sc.pack()

    def scale():
        label=Label(rate, text="Thank you!"+" You have rated us "+str(sc.get())+" stars!").pack()
    
    
    b=Button(rate, text="Rate Us!", command=scale).pack()


def contact_us():
    cont=Toplevel()
    cont.title("Contact Us")
    cont.geometry("300x300")
    contact1=Label(cont, text="Contact us by email: westviewhsc03@gmail.com", pady=10).pack()
    contact2=Label(cont, text="Contact us by landline: 2879056", pady=10).pack()

#Buttons inside main window
btn1=Button(info_frame, text="Our Vision", command=vision).pack(side=LEFT)
btn1=Button(info_frame, text="Rate Us", command=rate).pack(side=LEFT)
btn1=Button(info_frame, text="Contact Us", command=contact_us).pack(side=LEFT)
    

def admin():
    global admin_win
    admin_win=Toplevel()    #New window when admin login is clicked
    admin_win.geometry("463x500")
    
    sname=Label(admin_win, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10)
    sname.grid(row=0, column=0, columnspan=3)

    wel=Label(admin_win, text="Welcome to Admin Login", pady=10)
    wel.grid(row=1, column=0, columnspan=3)

    user_name=Label(admin_win, text="Enter the username: ", pady=10)
    password=Label(admin_win, text="Enter the password: ", pady=10)

    user_name.grid(row=2, column=0)
    password.grid(row=3, column=0)

    global e1
    e1=Entry(admin_win, width=40)
    global e2
    e2=Entry(admin_win, width=40)

    e1.grid(row=2, column=1, sticky=W)
    e2.grid(row=3, column=1, sticky=W)
    C=["NOTE: The password will be considered valid only if it has a"
       " minimum of 5 characters"]

    cond=Label(admin_win, text=C, pady=20)
    cond.grid(row=4, columnspan=3, sticky=S)

    global go
    go=Button(admin_win, text="GO", padx=10, fg="white", bg="green", command=go)
    go.grid(row=5, column=0, columnspan=2)

    close=Button(admin_win, text="EXIT", padx=10, pady=2, command=admin_win.destroy, bg="red").grid(row=5, column=1)

#admins that can login
    
global users
users=[("admin@1","one#1"),
       ("admin@2","two#2"),
       ("admin@3","three#3"),
       ("admin@4","four#4"),
       ("admin@5","five#5")]

#Command for go button in admin login; goes to next window
def go():
    if (str(e1.get()), str(e2.get())) not in users:   #Condition to check the validity of username and password
        messagebox.showerror("Login Error", "Sorry, invalid username or password. Please try again")
    else:                                           #New window to ask for grade/class to be selected
        admin_win.withdraw()
        master=Toplevel()
        master.geometry("420x400")
        master.title("Admin")

        sname=Label(master, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).pack()

        lbl_grade=Label(master, text="Select a grade: ", pady=10).pack()

        global var_grade
        var_grade=StringVar()
        var_grade.set("9")
        
        grades=["9","10","11","12"]
        menu_grade=OptionMenu(master, var_grade, *grades).pack()

        label_division=Label(master, text="Select a division: ", pady=10).pack()

        global var_div
        var_div=StringVar()
        var_div.set("A")
        
        divisions=["A","B","C"]
        menu_division=OptionMenu(master, var_div, *divisions).pack()

        next1=Button(master, text="NEXT", bg="light green", borderwidth=5, command=next_1).pack()

        home=Button(master, text="Back to home page", padx=10.5, bg="yellow", command=root.deiconify).pack(side=BOTTOM, anchor=W)

        close=Button(master, text="EXIT", padx=50, command=master.destroy, bg="red").pack(side=BOTTOM, anchor=W)


def next_1():       #If next button is clicked from grades window(master), this window pops up to show admin functionalities
    records=Toplevel()
    records.title("Admin")
    records.geometry("463x500")

    sname=Label(records, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=10).pack()

    welcome=Label(records, text="Welcome to "+" "+var_grade.get()+" "+var_div.get(), pady=10, fg="green").pack()

    funcn=Label(records, text="Select a functionality", pady=10).pack()

    display=Button(records, text="Display Records", padx=49, borderwidth=5, command=disp_option).pack()
    update=Button(records, text="Update Student Records", padx=27, borderwidth=5, command=upd_option).pack()
    search=Button(records, text="Search Records", padx=50, borderwidth=5, command=search_option).pack()
    add=Button(records, text="Add New Records", padx=43, borderwidth=5, command=add_rec).pack()
    delete=Button(records, text="Delete Records", padx=50, borderwidth=5, command=del_rec).pack()

    close=Button(records, text="EXIT", pady=5, command=records.destroy, bg="red").pack(side=BOTTOM, anchor=E)


def disp_option():         #To ask whether to display academic or personal details
    option_disp=Toplevel()
    option_disp.geometry("500x500")
    
    sname=Label(option_disp, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=50).pack()
    
    btn1=Button(option_disp, text="Display Academic Records", command=disp_aca).pack(anchor=CENTER)
    btn2=Button(option_disp, text="Display Personal Records", command=disp_per).pack(anchor=CENTER)

    close=Button(option_disp, text="EXIT", pady=5, command=option_disp.destroy, bg="red").pack(side=BOTTOM, anchor=E)
    
def disp_aca():             #To display records of students
    g=var_grade.get()
    s=var_div.get()

    academic.display(g,s)

def disp_per():
    g=var_grade.get()
    s=var_div.get()

    personal.display(g,s)
    

def upd_option():               #To ask whether to update academic or personal details
    option_upd=Toplevel()
    option_upd.geometry("500x500")

    sname=Label(option_upd, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=50).pack()
    
    btn1=Button(option_upd, text="Update Academic Records", command=upd_aca).pack(anchor=CENTER)
    btn2=Button(option_upd, text="Update Personal Records", command=upd_per).pack(anchor=CENTER)

    close=Button(option_upd, text="EXIT", pady=5, command=option_upd.destroy, bg="red").pack(side=BOTTOM, anchor=E)

def upd_aca():      #To update academic records
    g=var_grade.get()
    s=var_div.get()
    
    academic.update(g,s)

def upd_per():      #To update personal records
    g=var_grade.get()
    s=var_div.get()
    
    personal.update(g,s)

def search_option():
    option_srch=Toplevel()
    option_srch.geometry("500x500")

    sname=Label(option_srch, text="WESTVIEW HIGHER SECONDARY SCHOOL", fg="blue", pady=50).pack()
    
    btn1=Button(option_srch, text="Search Academic Records", command=srch_aca).pack(anchor=CENTER)
    btn2=Button(option_srch, text="Search Personal Records", command=srch_per).pack(anchor=CENTER)

    close=Button(option_srch, text="EXIT", pady=5, command=option_srch.destroy, bg="red").pack(side=BOTTOM, anchor=E)

def srch_aca():
    g=var_grade.get()
    s=var_div.get()
    
    academic.search(g,s)

def srch_per():
    g=var_grade.get()
    s=var_div.get()
    
    personal.search(g,s)

def add_rec():
    g=var_grade.get()
    s=var_div.get()
    
    academic.add1(g, s)

def del_rec():
    g=var_grade.get()
    s=var_div.get()
    
    academic.delete(g, s)
    
    
    
admin=Button(root, text="Admin Login", padx=50, pady=10, fg="white", bg="red", command=admin)
close=Button(root, text="EXIT", padx=73, pady=10, command=root.destroy, bg="light blue")

admin.pack()
close.pack()

root.mainloop()
