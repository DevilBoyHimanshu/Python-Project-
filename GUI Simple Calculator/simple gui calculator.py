# Simple gui calculator

import tkinter as t
def main():
    w=t.Tk()
    w.geometry('500x300')
    l1=t.Label(w,text='Number 1',font=('Arial',15))
    l2=t.Label(w,text='Number 2',font=('Arial',15))
    l3=t.Label(w,text='Result',font=('Arial',15))
    e1=t.Entry(w,width=10,font=('Arial',15))
    e2=t.Entry(w,width=10,font=('Arial',15))
    e3=t.Entry(w,width=10,font=('Arial',15))

    def add():      # Addition
        n1=int(e1.get())
        n2=int(e2.get())
        n3=n1+n2
        e3.delete(0,t.END)
        e3.insert(0,str(n3))

    def sub():      # Subtraction
        n1=int(e1.get())
        n2=int(e2.get())
        n3=n1-n2
        e3.delete(0,t.END)
        e3.insert(0,str(n3))

    def multiply():     # Multiplication
        n1=int(e1.get())
        n2=int(e2.get())
        n3=n1*n2
        e3.delete(0,t.END)
        e3.insert(0,str(n3))

    def div():          # Division
        n1=int(e1.get())
        n2=int(e2.get())
        n3=n1/n2
        e3.delete(0,t.END)
        e3.insert(0,str(n3))

    b1=t.Button(w,text='Add',font=('Arial',14),width=10,command=add)
    b2=t.Button(w,text='Sub',font=('Arial',14),width=10,command=sub)
    b3=t.Button(w,text='Multiply',font=('Arial',14),width=10,command=multiply)
    b4=t.Button(w,text='Div',font=('Arial',14),width=10,command=div)
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    b1.grid(row=4,column=1)
    b2.grid(row=4,column=2)
    b3.grid(row=5,column=1)
    b4.grid(row=5,column=2)

main()
