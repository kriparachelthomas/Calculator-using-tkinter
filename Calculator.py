import parser
from tkinter import *
root = Tk()
root.title("CALCULATOR")
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
#getting user input and placing it in the textfield
i=0
def getinput(num):
    global i
    display.insert(i,num)
    i=i+1
def clearall():
    display.delete(0,END)
def undo():
    entire_string=display.get()
    if len(entire_string):
        newstring=entire_string[:-1]
        clearall()
        display.insert(0,newstring)
    else:
        clearall()
        display.insert(0,"Error")
def getoperations(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length
def equal():
    entire_string = display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,"error")

#adding buttons
Button(root,text="1",command=lambda :getinput(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :getinput(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :getinput(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda :getinput(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :getinput(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :getinput(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda :getinput(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :getinput(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :getinput(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda :getinput(0)).grid(row=5,column=0)
Button(root,text="AC",command=lambda :clearall()).grid(row=5,column=1)
Button(root,text="=",command=lambda :equal()).grid(row=5,column=2)
Button(root,text="+",command=lambda :getoperations('+')).grid(row=2,column=3)
Button(root,text="-",command=lambda :getoperations('-')).grid(row=3,column=3)
Button(root,text="*",command=lambda :getoperations('*')).grid(row=4,column=3)
Button(root,text="/",command=lambda :getoperations('/')).grid(row=5,column=3)
Button(root,text="pi",command=lambda :getoperations('*3.14')).grid(row=2,column=4)
Button(root,text="%",command=lambda :getoperations('%')).grid(row=3,column=4)
Button(root,text="(",command=lambda :getoperations('(')).grid(row=4,column=4)
Button(root,text=")",command=lambda :getoperations(')')).grid(row=5,column=4)
Button(root,text="exp",command=lambda :getoperations('**')).grid(row=2,column=5)
Button(root,text="x!").grid(row=3,column=5)
Button(root,text="^2",command=lambda :getoperations('**2')).grid(row=4,column=5)
Button(root,text="->",command=lambda :undo()).grid(row=5,column=5)

root.mainloop()