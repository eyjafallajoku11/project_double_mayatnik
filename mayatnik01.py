from tkinter import Tk, Canvas, Button, Entry
from math import sin, cos, pi


def stop():
    global go
    go = 0
    StartButton.config(text="старт", command=start)


def drawgraf():
    global angle0
    holst.create_line(1100 + angle0[0] / pi * 400, 650 + angle0[1] / pi * 400,
                      1100 + angle[0] / pi * 400, 650 + angle[1] / pi * 400, fill="lime", tag="graf")
    angle0[0], angle0[1] = angle[0], angle[1]


def start():
    global angle, w, go, j
    go = 1
    StartButton.config(text="стоп", command=stop)
    while go:
        if j == 100: j = 0
        # drawgraf()
        znam = (l / 2) * (2 * m1 + m2 - m2 * cos(2 * angle[0] - 2 * angle[1]))
        e1 = (-g * (2 * m1 + m2) * sin(angle[0]) - m2 * g * sin(angle[0] - 2*angle[1]) -
              2 * sin(angle[0] - angle[1]) * m2 *
              (w[1] ** 2 * (l / 2) + w[0] ** 2 * (l / 2) * cos(angle[0] - angle[1]))) / znam
        e2 = (2 * sin(angle[0] - angle[1]) * (w[0] ** 2 * (l / 2) * (m1 + m2) + g * (m1 + m2) * cos(angle[0])
                                              + w[1] ** 2 * (l / 2) * m2 * cos(angle[0] - angle[1]))) / znam
        w[0] += e1 / 50
        w[1] += e2 / 50
        angle[0] += w[0]
        angle[1] += w[1]
        y1 = 100 + l / 2 * cos(angle[0])
        x1 = 450 + l / 2 * sin(angle[0])
        y2 = y1 + l / 2 * cos(angle[1])
        x2 = x1 + l / 2 * sin(angle[1])
        holst.coords(may1, 450, 100, x1, y1)
        holst.coords(may2, x1, y1, x2, y2)
        holst.coords(nak1, x1 - 5, y1 - 5, x1 + 5, y1 + 5)
        holst.coords(nak2, x2 - 5, y2 - 5, x2 + 5, y2 + 5)
        j += 1
        if j%5==0:
            coord = tuple(holst.coords(line) + [x2, y2])
            holst.coords(line, coord)
        holst.update()


def checkpole():
    t = Pole.get()
    if not t.isdigit():
        Pole.delete(0, 100)
        for k in range(len(t)):
            if t[k].isdigit() or (t[k] == "." and Pole.get().count(".") == 0) or (t[k] == "-" and len(Pole.get()) == 0):
                Pole.insert(k, t[k])


def changeangle(n=0):
    global angle, w
    checkpole()
    t = Pole.get()
    if t != "":
        holst.delete("graf")
        stop()
        angle[n] = ((float(t) + 180) % 360 - 180) / 180 * pi
        angle0[n] = angle[n]
        w = [0, 0]
        y1 = 100 + l / 2 * cos(angle[0])
        x1 = 450 + l / 2 * sin(angle[0])
        y2 = y1 + l / 2 * cos(angle[1])
        x2 = x1 + l / 2 * sin(angle[1])
        holst.coords(may1, 450, 100, x1, y1)
        holst.coords(may2, x1, y1, x2, y2)
        holst.coords(nak1, x1 - 5, y1 - 5, x1 + 5, y1 + 5)
        holst.coords(nak2, x2 - 5, y2 - 5, x2 + 5, y2 + 5)
        holst.coords(line, x2, y2, x2, y2)


okno = Tk()
okno.geometry('1300x900')
holst = Canvas(okno, width=1300, height=900, bg='white')
holst.create_line(900, 0, 900, 900, width=5)
holst.create_rectangle(900, 450, 1300, 850)
holst.pack()

j = 0
l = 700
g = 9.82
angle0 = [0, 0]
angle = [0, 0]
w = [0, 0]
y1 = 100 + l / 2 * cos(angle[0])
x1 = 450 + l / 2 * sin(angle[0])
y2 = y1 + l / 2 * cos(angle[1])
x2 = x1 + l / 2 * sin(angle[1])
may1 = holst.create_line(450, 100, x1, y1, width=3, fill="orange")
may2 = holst.create_line(x1, y1, x2, y2, width=3, fill="orange")
nak1 = holst.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill="red")
nak2 = holst.create_oval(x2 - 5, y2 - 5, x2 + 5, y2 + 5, fill="red")
line = holst.create_line(x2, y2, x2, y2, width=2, fill="lime")
go = 0
m1 = 10
m2 = 10
StartButton = Button(text="старт", command=start, height=3, width=15)
StartButton.place(x=1100, y=350, anchor="s")
PoleButton1 = Button(text="выставить угол 1", command=changeangle, height=3, width=15)
PoleButton1.place(x=1000, y=270, anchor="s")
PoleButton2 = Button(text="выставить угол 2", command=lambda: changeangle(1), height=3, width=15)
PoleButton2.place(x=1200, y=270, anchor="s")
input = str()
Pole = Entry(textvariable=input)
Pole.place(x=1100, y=200, anchor="s")
okno.mainloop()
