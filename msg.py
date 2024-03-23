from tkinter import *
from tkinter import messagebox
root = Tk()
def callback():
    messagebox.showinfo("well done great !")
    print("you clicked delete")
button1 = Button(root,text="Delete",command = callback)
button1.grid(row=0,column=0,padx=90,pady=50)
root.geometry('350x250')
root.title("pythonLobby")
root.mainloop()