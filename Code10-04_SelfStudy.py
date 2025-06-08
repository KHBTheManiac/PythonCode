from tkinter import *
window = Tk()

photo = PhotoImage(file="dog.gif")
label1 = Label(window, image = photo)

photo2 = PhotoImage(file="cat.gif")
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()