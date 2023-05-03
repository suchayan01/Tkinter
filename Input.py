from tkinter import *
root= Tk()

e= Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"Enter your name")
# print(e)
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
# myButton= Button(root, text= "Click me",state=DISABLED,padx=10,pady=10)
myButton= Button(root, text= "Click me",command=myClick,fg="blue",bg="white")
myButton.pack()


root.mainloop()
