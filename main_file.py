from tkinter import *
import passwordmeter
import random
import string
import pyperclip as pc


def genPassword():
    CharList = '@'+'_'+'-'+'+'+' '+'.'+'?'+'$' + \
        '`' + string.ascii_letters+string.digits
    firstPassword = ''
    for i in range(16):
        firstPassword += CharList[random.randint(0, len(CharList)-1)]
    return firstPassword


def passStrength(store_firstPassword):
    Strength = passwordmeter.test(store_firstPassword)
    return Strength


def password():
    x = genPassword()
    while float((passStrength(x))[0]) < 0.8:
        x = genPassword()
    return x


window = Tk()
window.title('Password generator')

window.geometry('300x100')
window.resizable(0, 0)


def magic():
    window.geometry('300x200')
    # code for copy
    pwd = password()
    btn1['text'] = 'Generate another'
    lbl1['text'] = str(pwd)
    lbl1['font'] = "Helvetica 16 bold"
    lbl1['bg'] = "seagreen"
    pc.copy(pwd)
    pwdStrength = passStrength(pwd)

    lbl3 = Label(window, text='Strength of password: ' +
                 str(pwdStrength[0])[0:5], bg="black", fg="springgreen2")
    lbl3.grid(column=0, row=3, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2), columnspan=2)

    lbl2 = Label(window, text='Save password for: ',
                 bg="black", fg="springgreen2")
    lbl2.grid(column=0, row=4, padx=(10, 0), pady=(5, 5), ipadx=(5), ipady=(2))

    ent1 = Entry(window, width=20)
    ent1.grid(column=1, row=4, padx=(10, 0), pady=(5, 5), ipadx=(5), ipady=(2))

    btn2 = Button(window, text='    Save    ', bg="black", fg="springgreen2")
    btn2.grid(column=0, row=5, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2), columnspan=2)


btn1 = Button(window, text='Generate and copy',
              bg="black", fg="springgreen2", command=magic)
btn1.grid(column=0, row=0, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), columnspan=2)

lbl1 = Label(window, text=' ')
lbl1.grid(column=0, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), columnspan=2)

window.mainloop()
