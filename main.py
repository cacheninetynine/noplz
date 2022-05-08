import string
from tkinter import *
num2alpha = dict(zip(range(1, 27), string.ascii_lowercase))


def noplz(esotericcode):
    esocodebackup = esotericcode
    esotericlen = len(esotericcode)
    vsmode = False
    asciimode = False
    ei = 0
    v = 0
    mv = ""
    vs = ""
    while ei < esotericlen:
        if esotericcode[ei] == "c":
            v = 0
            vs = " "
        if esotericcode[ei] == "+":
            if vsmode:
                v = v + 1
                if v > 26 and vsmode:
                    v = 26
                    vs = num2alpha[v]
                else:
                    if v == 0:
                        vs = " "
                    else:
                        vs = num2alpha[v]
            else:
                v = v + 1
        if esotericcode[ei] == "-":
            if vsmode:
                v = v - 1
                if v < 0 and vsmode:
                    v = 0
                    vs = num2alpha[v]
                else:
                    if v == 0:
                        vs = " "
                    else:
                        vs = num2alpha[v]
            else:
                v = v - 1
        if esotericcode[ei] == "t":
            vsmode = True
            mv = ""
        if esotericcode[ei] == "s":
            return esocodebackup
        if esotericcode[ei] == "p":
            if vsmode:
                return vs
            else:
                return v
        if esotericcode[ei] == "*":
            if vsmode:
                mv = mv + vs
            else:
                mv = mv + str(v)
        if esotericcode[ei] == "!":
            return mv
        if esotericcode[ei] == "%":
            if vsmode:
                v = v * 2
                if v > 26 and vsmode:
                    v = 26
                    vs = num2alpha[v]
                else:
                    if v == 0:
                        vs = " "
                    else:
                        vs = num2alpha[v]
            else:
                v = v * 2
        if esotericcode[ei] == "a":
            asciimode = True
        ei = ei + 1


# you can delete everything below, its the ui


def clicked():
    txt2.config(text = noplz(txt.get()))


window = Tk()
window.resizable(width=False, height=False)
window.title("noplz")
window.geometry('630x100')
lbl = Label(window, text="Enter noplz code here:")
lbl.grid(column=0, row=0)
txt2 = Label(window, text="Result go here")
txt2.place(relx=0.5, rely=0.6, anchor=CENTER)
txt = Entry(window, width=70)
txt.grid(column=1, row=0)
btn = Button(window, text="Run the code", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
