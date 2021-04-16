from tkinter import *
from tkinter import ttk
import pymysql

root=Tk()
def register():
    name=e.get()
    fname=e1.get()
    dob=e2.get()
    email=e3.get()
    phone=e4.get()
    v=var.get()
    gen=""
    if v==1:
        gen="Male"
    else:
        gen="Female"
    state=var1.get()
    if chvar1.get() and chvar.get() and chvar2.get():
        print("All are checked")
    elif chvar.get() and chvar1.get():
        print("Hindi and English are checked")
    elif chvar1.get() and chvar2.get():
        print("English and French are checked")
    elif chvar.get() and chvar2.get():
        print("Hindi and French are checked")
    elif chvar.get():
        print("Hindi is checked")
    elif chvar1.get():
        print("English  is checked")
    elif chvar2.get():
        print("French is checked")
    print(name,"\n",fname,"\n",dob,"\n",email,"\n",phone,"\n",state,"\n",gen)
root.geometry("600x600")
root.title("Registration form")
root.maxsize(width=600,height=600)
root.minsize(width=600,height=600)
label=Label(text="Registration form", font=("Arial",20,"bold"),width=20)
label.place(x=100,y=50)
name=Label(text="Full Name:",font=("Arial",16))
name.place(x=80,y=120)
e=Entry(font=("Arial",16))
e.place(x=260,y=120)
fname=Label(text="Father's Name:",font=("Arial",16))
fname.place(x=77,y=160)
e1=Entry(font=("Arial",16))
e1.place(x=260,y=160)
dob=Label(text="Date of Birth:",font=("Arial",16))
dob.place(x=77,y=200)
e2=Entry(font=("Arial",16))
e2.place(x=260,y=200)
email=Label(text="Email:",font=("Arial",16))
email.place(x=77,y=240)
e3=Entry(font=("Arial",16))
e3.place(x=260,y=240)
ph=Label(text="Phone Number:",font=("Arial",16))
ph.place(x=77,y=280)
e4=Entry(font=("Arial",16))
e4.place(x=260,y=280)
gender=Label(text="Gender:",font=("Arial",16))
gender.place(x=77,y=320)
var=IntVar()
male=Radiobutton(root,text="Male",value="1",variable=var)
male.place(x=260,y=320)
female=Radiobutton(root,text="Female",value="2",variable=var)
female.place(x=380,y=320)
languages=Label(text="Languages:",font=("Arial",16))
languages.place(x=77,y=360)
chvar=IntVar()
chvar1=IntVar()
chvar2=IntVar()
hindi=Checkbutton(root,text="Hindi",variable=chvar,onvalue=1,offvalue=0)
hindi.place(x=260,y=360)
english=Checkbutton(root,text="English",variable=chvar1,onvalue=1,offvalue=0)
english.place(x=380,y=360)
french=Checkbutton(root,text="French",variable=chvar2,onvalue=1,offvalue=0)
french.place(x=500,y=360)
var1=StringVar()
state=Label(text="State:",font=("Arial",16))
state.place(x=77,y=400)
dropDownList=ttk.Combobox(root,textvariable=var1,width=15)
dropDownList['values']=["UP","RAJ","HR","UK","MP","TN","WB","PU"]
dropDownList.place(x=260,y=400)
b=Button(root,text="Submit",bg="purple",fg="white",command=register,width=10).place(x=220,y=460)
root.mainloop()