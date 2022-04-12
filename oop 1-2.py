from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Hello Python World")
window.geometry("500x400+20+10")

# Insert button widget


lbl = Label (window, text = "Student Semestral Grade", font =("Verdana", 14))
lbl.place(relx =.5, y=70, anchor = "center")
btn = Button(window, text = "I am Button", fg ="Orange")
btn.place(x= 50, y= 100)


lbl1 = Label(window, text = "Prelim Grade")
lbl2 = Label(window, text = "Midterm Grade")
lbl3 = Label(window, text = "Final Grade")
lbl1.place(x=50, y=150)
lbl2.place(x=50, y=200)
lbl3.place(x=50, y=250)


txtfld = Entry(window, bd = 4)
txtfld2 = Entry(window, bd = 4)
txtfld3 = Entry(window, bd = 4)

txtfld.place(x=150, y=150)
txtfld2.place(x=150, y=200)
txtfld3.place(x=150, y=250)


#add selection widget
var = IntVar()
var.set(1)

r1 = Radiobutton(window, text = "Prelim",variable=var, value=1)
r2 = Radiobutton(window, text = "Midterm",variable=var, value=2)
r3 = Radiobutton(window, text = "Final",variable=var, value=3)

r1.place(x=250, y=150)
r2.place(x=250, y=200)
r3.place(x=250, y=250)


c1 = Checkbutton(window, text = "view term Grade")
c2 = Checkbutton(window, text = "view Sem Grade")
c1.place(x=50, y=350)
c2.place(x=200, y=350)

data1 = "English"
data2 = "Filipino"
data3 = "OOP"

lb = Listbox(window, height=5, selectmode="multiple")
lb.insert(END, data1, data2, data3)
lb.place(y=150, x=350)

var1 = StringVar()
var1.set("English")
data = "English", "Filipino", "OOP"
cb = ttk.Combobox(window, values = data)
cb.place(x=350, y=300)

window.mainloop()
