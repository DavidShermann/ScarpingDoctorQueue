

from tkinter import *



def submit():
    prof = prof_var.get()
    print(prof)
    root.destroy()


root = Tk()
prof_var = StringVar()
# specify size of window.
root.geometry("350x100")

root.eval('tk::PlaceWindow . center')

# Create text widget and specify size
T = Entry(root,font = ("Ariel",14),textvariable=prof_var)
 
# Create label
l = Label(root, text = "Insert keyword for finding a doctor")
l.config(font =("Ariel", 14))
 
# Create an Exit button.
b2 = Button(root, text = "OK",command = submit,font =("Ariel", 14))


l.pack()
T.pack()
b2.pack()
 


mainloop()











