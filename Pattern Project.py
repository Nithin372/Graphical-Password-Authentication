from tkinter import *
from tkinter import messagebox
import random as r


def show_frame(frame_faces):
    frame_faces.tkraise()


win = Tk()
win.title("ANONYMOUS")
win.geometry("1100x600")
win.state("zoomed")
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)
frame1 = Frame(win)
frame2 = Frame(win)
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky='nsew')
t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0
lt = []
sd = []
tst = []
lite = 0

frame2_label = Label(frame2, text='...** WELCOME **...', font=('Algerian', 50, 'bold'), fg='Blue', bg='pink')
frame2_label.place(x=300, y=200)
frame2_button = Button(frame2, text="LOGOUT", fg='black', bg='white', font=("Baskerville Old Face", 20, "bold"), command=lambda: show_frame(frame1))
frame2_button.place(x=500, y=600)


def ball1():
    global t1, m1, lite
    if lite == 0:
        if t1 == 0:
            t1 = 1
            b1.config(borderwidth=5, bg='grey')
            lt.append('ball-1')
        elif t1 == 1:
            t1 = 0
            b1.config(borderwidth=0, bg='white')
            lt.remove('ball-1')
    elif lite == 1:
        if m1 == 0:
            m1 = 1
            b1.config(borderwidth=5, bg='grey')
            tst.append('ball-1')
        elif m1 == 1:
            m1 = 0
            b1.config(borderwidth=0, bg='white')
            tst.remove('ball-1')


def basketball():
    global t2, m2, lite
    if lite == 0:
        if t2 == 0:
            t2 = 1
            b2.config(borderwidth=5, bg='grey')
            lt.append('basketball-2')
        elif t2 == 1:
            t2 = 0
            b2.config(borderwidth=0, bg='white')
            lt.remove('basketball-2')
    elif lite == 1:
        if m2 == 0:
            m2 = 1
            b2.config(borderwidth=5, bg='grey')
            tst.append('basketball-2')
        elif m2 == 1:
            m2 = 0
            b2.config(borderwidth=0, bg='white')
            tst.remove('basketball-2')


def colorball():
    global t3, m3, lite
    if lite == 0:
        if t3 == 0:
            t3 = 1
            b3.config(borderwidth=5, bg='grey')
            lt.append('colourball-3')
        elif t3 == 1:
            t3 = 0
            b3.config(borderwidth=0, bg='white')
            lt.remove('colourball-3')
    elif lite == 1:
        if m3 == 0:
            m3 = 1
            b3.config(borderwidth=5, bg='grey')
            tst.append('colourball-3')
        elif m3 == 1:
            m3 = 0
            b3.config(borderwidth=0, bg='white')
            tst.remove('colorball-3')


def cricketball():
    global t4, m4, lite
    if lite == 0:
        if t4 == 0:
            t4 = 1
            b4.config(borderwidth=5, bg='grey')
            lt.append('cricketball-4')
        elif t4 == 1:
            t4 = 0
            b4.config(borderwidth=0, bg='white')
            lt.remove('cricketball-4')
    elif lite == 1:
        if m4 == 0:
            m4 = 1
            b4.config(borderwidth=5, bg='grey')
            tst.append('cricketball-4')
        elif m4 == 1:
            m4 = 0
            b4.config(borderwidth=0, bg='white')
            tst.remove('cricketball-4')


def rugbyball():
    global t5, m5, lite
    if lite == 0:
        if t5 == 0:
            t5 = 1
            b5.config(borderwidth=5, bg='grey')
            lt.append('rugbyball-5')
        elif t5 == 1:
            t5 = 0
            b5.config(borderwidth=0, bg='white')
            lt.remove('rugbyball-5')
    elif lite == 1:
        if m5 == 0:
            m5 = 1
            b5.config(borderwidth=5, bg='grey')
            tst.append('rugbyball-5')
        elif m5 == 1:
            m5 = 0
            b5.config(borderwidth=0, bg='white')
            tst.remove('rugbyball-5')


def football():
    global t6, m6, lite
    if lite == 0:
        if t6 == 0:
            t6 = 1
            b6.config(borderwidth=5, bg='grey')
            lt.append('hockey-6')
        elif t6 == 1:
            t6 = 0
            b6.config(borderwidth=0, bg='white')
            lt.remove('hockey-6')
    elif lite == 1:
        if m6 == 0:
            m6 = 1
            b6.config(borderwidth=5, bg='grey')
            tst.append('hockey-6')
        elif m6 == 1:
            m6 = 0
            b6.config(borderwidth=0, bg='white')
            tst.remove('hockey-6')


l1 = Label(frame1, text='Set the Sequence order of Images :', font=('Arial', 15, 'bold'), fg='Brown')
l2 = Label(frame1, text='Enter your Password Sequence', font=('Arial', 15, 'bold'), fg='Brown')
i1 = PhotoImage(file='ball.png')
i2 = PhotoImage(file='basketball.png')
i3 = PhotoImage(file='colorball.png')
i4 = PhotoImage(file='cricketball.png')
i5 = PhotoImage(file='rugbyball.png')
i6 = PhotoImage(file='football.png')

b1 = Button(frame1, image=i1, command=ball1, bg='white', borderwidth=0)
b2 = Button(frame1, image=i2, command=basketball, bg='white', borderwidth=0)
b3 = Button(frame1, image=i3, command=colorball, bg='white', borderwidth=0)
b4 = Button(frame1, image=i4, command=cricketball, bg='white', borderwidth=0)
b5 = Button(frame1, image=i5, command=rugbyball, bg='white', borderwidth=0)
b6 = Button(frame1, image=i6, command=football, bg='white', borderwidth=0)

ls = [b1, b2, b3, b4, b5, b6]


def con():
    global m1, m2, m3, m4, m5, m6
    if lt == tst:
        show_frame(frame2)
    elif lt != tst:
        messagebox.showerror('UNSUCCESSFUL', message='WRONG PATTERN')
    m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0
    tst.clear()
    a, b = 60, 100
    sd.clear()
    while len(sd) != 6:
        d = int(r.random() * 6)
        if d not in sd:
            sd.append(d)
        else:
            continue
        ls[d].place(x=a, y=b)
        a = a + 200
    b1.config(borderwidth=0, bg='white')
    b2.config(borderwidth=0, bg='white')
    b3.config(borderwidth=0, bg='white')
    b4.config(borderwidth=0, bg='white')
    b5.config(borderwidth=0, bg='white')
    b6.config(borderwidth=0, bg='white')


def ent():
    l1.place_forget()
    l2.place(x=70, y=20)
    global lite
    lite = 1
    but.place_forget()
    but2.place(x=650, y=350)
    b1.config(borderwidth=0, bg='white')
    b2.config(borderwidth=0, bg='white')
    b3.config(borderwidth=0, bg='white')
    b4.config(borderwidth=0, bg='white')
    b5.config(borderwidth=0, bg='white')
    b6.config(borderwidth=0, bg='white')


but2 = Button(frame1, text='CONFIRM', font=('algerian', 20), command=con, bg='orange')
but = Button(frame1, text='ENTER', font=('algerian', 20), command=ent, bg='orange')

l1.place(x=70, y=20)
but.place(x=600, y=500)


def main():
    a, b = 50, 100
    sd.clear()
    while len(sd) != 6:
        d = int(r.random() * 6)
        if d not in sd:
            sd.append(d)
        else:
            continue
        ls[d].place(x=a, y=b)
        a = a + 250


main()
show_frame(frame1)
win.mainloop()
