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
                    return "noplz error: Text variable over 26! Maybe you forgot to reset the variable?"
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
                    return "noplz error: Text variable is negative!"
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
                    return "noplz error: Text variable over 26! Maybe you forgot to reset the variable?"
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

# you can delete everything below, it's the UI

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

# small documentation
# c : creates (makes it look like it created it) an empty variable (resets it to 0 or " " (if text mode) if already created)
# + : adds 1 to the variable (or moves one letter further if string mode enabled)
# - : removes 1 to the variable (or moves one letter back if string mode enabled)
# t : turns the variable to string (text) mode (disabled by default)
# p : prints the current variable
# s : prints the source code
# * : adds current variable to the mix variable
# ! : prints the mix variable
# % : multiplies the variable by 2
# a : ascii text mode (disabled by default too and does nothing (yet))

# examples:
# print all numbers from 1 to 9: c+*+*+*+*+*+*+*+*+*!
