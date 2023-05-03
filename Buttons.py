from tkinter import *
root= Tk()

def myClick():
    myLabel = Label(root, text="Click happened")
    myLabel.pack()
# myButton= Button(root, text= "Click me",state=DISABLED,padx=10,pady=10)
myButton= Button(root, text= "Click me",command=myClick,fg="blue",bg="white")
myButton.pack()


root.mainloop()
