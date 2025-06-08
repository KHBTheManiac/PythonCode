from tkinter import *
import random


fnameList = ["square.gif", "circle.gif", "sponge.gif", "squid.gif", "frog.gif",
             "bird.gif", "squirrel.gif", "dog.gif", "cat.gif"]


random.shuffle(fnameList)


btnList = []
photoList = []


window = Tk()
window.geometry("210x210")
window.title("랜덤 이미지 버튼")


for fname in fnameList:
    photo = PhotoImage(file=fname)
    photoList.append(photo)
    btn = Button(window, image=photo)
    btnList.append(btn)

num = 0
for i in range(3):
    for k in range(3):
        btnList[num].place(x=k * 70, y=i * 70)
        num += 1

window.mainloop()