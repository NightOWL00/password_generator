import os
import tkinter as t
import password_gen_v2 as pg
import pyperclip as pc

password = pg.password()


def saveFunction():
    passfile = open('passwords.txt', '+a')
    passfile.write('The password is for ' + txt.get() + ': ' + password)
    passfile.close()


def clicked_gen():
    # passwordStr
    passwordStr = t.Label(window, text=str(password), font=("Helvetica", 20))
    passwordStr.grid(column=0, row=1, padx=(20, 25), pady=(5, 5), sticky='E')

    # copy Button
    copyButton = t.Button(window, text='Copy', command=copyButtonClicked, bg="springgreen2",
                          fg="black",)
    copyButton.grid(column=0, row=4, padx=(10, 10), pady=(
        20, 10), ipadx=(5), ipady=(2), sticky='W')

    # Password Strength
    passwordStrength = t.Label(window, text='Password Strength (Between 0 and 1) is '+str(pg.passStrength(password))[:7]+')', bg="springgreen2",
                               fg="black")
    passwordStrength.grid(column=0, row=3, padx=(10, 30),
                          pady=(5, 5), sticky='E')

    # save
    saveButton = t.Button(window, text='Save Password',
                          bg="springgreen2", fg="black", command=saveFunction)
    saveButton.grid(column=0, row=5, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2), sticky='W')


def copyButtonClicked():
    pc.copy(password)


window = t.Tk()
window.geometry('400x300')
window.title("Password Generator and store")
window.resizable(0, 0)

# Title Label
titleLabel = t.Label(window, text="Click Generate to get a password",
                     font=("Helvetica", 15))
titleLabel.grid(column=0, row=0, padx=(45, 45), pady=(5, 5))

# generate button
GenerateButton = t.Button(window, text='Generate', bg="springgreen2",
                          fg="black", command=clicked_gen)
GenerateButton.grid(column=0, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), sticky='W')

# view passwords
viewButton = t.Button(window, text='View saved passwords',
                      bg="springgreen2", fg="black")
viewButton.grid(column=0, row=5, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), sticky='E')

# Exit Button
exit_button = t.Button(window, text='EXIT', bg='black',
                       fg='white', command=window.destroy)
exit_button.grid(column=0, row=4, padx=(10, 10),
                 pady=(20, 10), ipadx=(5), ipady=(2), sticky='E')

txt = t.Entry(window, width=10)
txt.grid(column=0, row=9)

window.mainloop()
