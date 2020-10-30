from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("INVENTORY MANAGEMENT SYSTEM")
Label(root,text="WELCOME ON LOGIN PAGE",font=("Courier",30,"italic","bold"),fg="blue").grid(row=0,column=2)
root.configure(bg='orange')


Label(root,text="username",font=("Courier",20,"bold"),fg="orange").grid(row=2,column=0)
Entry(root,fg="black",font=("Courier",15)).grid(row=2,column=1)
a=Label(root,text="password",font=("Courier",20,"bold"),fg="orange")
a.grid(row=3)
a=Entry(root,fg="black",font=("Courier",15),show='*')# * for security purpose 
a.grid(row=3,column=1)

def reset():
    x=Tk()
    x.title("CHANGE PASSWORD")
    Label(x,text=" Firstname:",fg="blue",font=("Curior",15,"italic")).grid(row=1)
    Entry(x,bg="pink",font=("Courier",15)).grid(row=1,column=1)
    Label(x,text=" Lastname:",fg="blue",font=("Curior",15,"italic")).grid(row=2)
    Entry(x,bg="pink",font=("Courier",15)).grid(row=2,column=1)
    Label(x,text=" Mobile:",fg="blue",font=("Curior",15,"italic")).grid(row=3)
    Entry(x,bg="pink",font=("Courier",15)).grid(row=3,column=1)
    Label(x,text=" DOB:",fg="blue",font=("Curior",15,"italic")).grid(row=4)
    Entry(x,bg="pink",font=("Courier",15)).grid(row=4,column=1)
    Label(x,text=" New password:",fg="blue",font=("Curior",15,"italic")).grid(row=5)
    Entry(x,bg="pink",font=("Courier",15)).grid(row=5,column=1)
    
    
    def fun():
        y=Tk()
        Label(y,text="Your password has been updated").grid()
        y.mainloop()
    Button(x,text="SAVE",bg="red",fg="orange",command=fun).grid(row=9,column=1)
    
    x.mainloop()
def log():
    
    
    y=Tk()
    y.title("Home")
    y.configure(bg="green")
    
    def Items():
            
        A=Tk()
        A.title("Stocked product")
        Label(A,text="All the product available at present",fg="green",font=("Courier",15,"italic","bold")).grid(row=1)
        Label(A,text="   Product name            No of items         Price per item(in Rs)",fg="orange",font=("Courier",15,"italic","bold")).grid(row=2)
        Label(A,text="Bread                   16                  12", fg="blue",font=("Courier",15,"italic","bold")).grid(row=3)
        Label(A,text="Milk                    10                  23",fg="blue",font=("Courier",15,"italic","bold")).grid(row=4)
        Label(A,text="Curd                    20                  35",fg="blue",font=("Courier",15,"italic","bold")).grid(row=5)
        Label(A,text="Sweet                   20                  85",fg="blue",font=("Courier",15,"italic","bold")).grid(row=6)
        Label(A,text="Butter                  11                  15",fg="blue",font=("Courier",15,"italic","bold")).grid(row=7)
        Label(A,text="Cake                    20                  05",fg="blue",font=("Courier",15,"italic","bold")).grid(row=8)
        Button(A,text="OK",bg="green",fg="white",width=15).grid(row=10)

    def OItems():
        B=Tk()
        B.title("Out of stock products")
        Label(B,text="List of unavailable products",fg="green",font=("Courier",15,"italic","bold")).grid(row=1)
        l=Listbox(B,font="arial 18 ",width=20,height=4,selectmode=SINGLE)
        l.insert(1,"Paneer")
        l.insert(2,"Khoya")
        l.insert(3,"Coldrink")
        l.insert(4,"Ice-cream")    
        l.grid(row=2,column=0)

    def show():
        C=Tk()
        Label(C,text="Sorry, no data found. please check another date",fg="red",font=("Courire",12,"italic","bold")).grid(row=1)

    def Pending():
        C=Tk()
        Label(C,text="Wow, Nothing left to deliver",fg="green",font=("Courire",12,"italic","bold")).grid(row=1)
    

        
    Label(y,text="MORGAN'S DAIRY",font=("Courier",30,"bold"),fg="red",bg="yellow").grid(row=0,column=1,pady=25)    
    Button(y,text="Available stock",fg="white",bg="black",font=("Courier",15,"italic"),command=Items).grid(row=1)
    Button(y,text="Out of stock",fg="white",bg="black",font=("Courier",15,"italic"),command=OItems).grid(row=1,column=1)
    Button(y,text="Delivery pending",fg="white",bg="black",font=("Courier",15,"italic"),command=Pending).grid(row=1,column=2)
    Label(y,text="Check all import and export date wise",font=('Verdana',14,),fg='blue').grid(row=2,column=1,pady=35)

    Label(y,text="Date:",fg="black",font=("Courier",10,"italic","bold")).grid(row=3)
    Spinbox(y,from_=1,to=31).grid(row=3,column=1)        
    Label(y,text="Month:",fg="black",font=("Courier",10,"italic","bold")).grid(row=4)
    Spinbox(y,from_=1,to=12).grid(row=4,column=1)
    Label(y,text="Year:",fg="black",font=("Courier",10,"italic","bold")).grid(row=5)
    Spinbox(y,from_=2020,to=2025).grid(row=5,column=1)

    Button(y,text="Search",fg="blue",bg="red",font=("Courier",10,"italic"),command=show).grid(row=4,column=2)
    
    y.mainloop()
Button(root,text="LOGIN",fg="blue",font=("Courier",15,"italic"),command=log).grid(row=5,column=2)
Button(root,text="Forgot password",fg="red",font=("Cuorier",10,"italic"),command=reset).grid(row=6,column=3)


root.mainloop()
