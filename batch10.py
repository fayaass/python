# import tkinter

# win=tkinter.Tk()
# win.title("Batch10")
# win.configure(bg="green")
# win.minsize(400,400)
# win.maxsize(500,500)
# def save():
#     # print(e1.get())
#     l3.config(text=e1.get())
    



# l1=tkinter.Label(win,text="Welcome to all",bg='green',fg='blue')
#  # l1.pack()
# l1.place(x=150,y=20)
# # l1.grid(row=0,column=0)

# l2=tkinter.Label(win,text="name")
# l2.place(x=75,y=20)

# e1=tkinter.Entry(win)
# e1.place(x=150,y=50)

# btn1=tkinter.Button(win,text="save",bg="gray",activebackground="black",activeforeground="white",padx=10,pady=8,command=save)
# btn1.place(x=150,y=70)

# l3=tkinter.Label(win)
# l3.place(x=150,y=120)



# l2=tkinter.Label(win,text="Welcome to all",bg='green',fg='red')
# l2.pack()
# l2.place(x=200,y=200)
# l2.grid(row=1,column=1)


# win.mainloop()


#1

import tkinter

win=tkinter.Tk()
win.title("Batch10")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(500,500)
def save():
    print(e1.get())


def reg_form():
    win1=tkinter.Tk()
    l1=tkinter.Label(win,text="Welcome to all",bg='green',fg='blue')
    l1.place(x=150,y=20)

    win1.mainloop()



l1=tkinter.Label(win,text="Welcome to all",bg='green',fg='blue')
l1.place(x=150,y=20)

l2=tkinter.Label(win,text="username")
l2.place(x=75,y=50)



e1=tkinter.Entry(win)
e1.place(x=150,y=50)

btn1=tkinter.Button(win,text="login",bg="gray",activebackground="black",activeforeground="white",padx=10,pady=8,command=save)
btn1.place(x=150,y=70)

btn2=tkinter.Button(win,text="register",bg="gray",activebackground="black",activeforeground="white",padx=10,pady=8,command=reg_form)
btn2.place(x=150,y=70)



win.mainloop()

