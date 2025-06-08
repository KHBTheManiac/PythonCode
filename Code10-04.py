from tkinter import *
window = Tk()

photo = PhotoImage(file = r"C:\Users\김학범\Downloads\dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()