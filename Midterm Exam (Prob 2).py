from tkinter import *

def ChangeToYellow(): btn.configure(bg="yellow", fg="black")

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")


btn = Button(window, text = "Click to Change Color", command=ChangeToYellow)
btn.place(relx= .5, rely= .5, anchor= "center")


window.mainloop()