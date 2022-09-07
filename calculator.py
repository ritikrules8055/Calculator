from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Syntax Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x820")
root.title("Calculator")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=20, padx=20)

f=Frame(root,bg="grey")
n=9
for i in range(3):
    b = Button(f, text=str(n), padx=28, pady=8, font="lucida 35 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)
    n-=1
f.pack()

f=Frame(root,bg="grey")
n=6
for i in range(3):
    b = Button(f, text=str(n), padx=28, pady=8, font="lucida 35 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)
    n-=1
f.pack()

f=Frame(root,bg="grey")
n=3
for i in range(3):
    b = Button(f, text=str(n), padx=28, pady=8, font="lucida 35 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)
    n-=1
f.pack()

f=Frame(root,bg="grey")
b = Button(f, text='0', padx=28, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='00', padx=15, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='C', padx=24, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root,bg="grey")
b = Button(f, text='+', padx=28, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='-', padx=33, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='*', padx=32, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root,bg="grey")
b = Button(f, text='/', padx=34, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='.', padx=34, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text='=', padx=28, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()