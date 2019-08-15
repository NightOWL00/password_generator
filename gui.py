import tkinter as t
from password_gen_v2 import *
import pyperclip as pc

password = password()


def clicked_gen():
    lb2 = t.Label(window, text=str(password), font=("Comic Sans", 20))
    lb2.grid(column=0, row=2, padx=(10, 10), pady=(5, 5))
    copyButton = t.Button(window, text='Copy', command=copyButtonClicked)
    copyButton.grid(column=0, row=8, padx=(10, 10), pady=(5, 5))


def clicked_showStrength():
    lb3 = t.Label(window, text='Password Strength (Between 0 and 1) is '+str(passStrength(password))[:10]+')', bg="springgreen2",
                fg="black")
    lb3.grid(column=0, row=7, padx=(10, 10), pady=(5, 5))


def copyButtonClicked():
    pc.copy(password)


window = t.Tk()
window.geometry('330x270')
window.title("Password Generator and store")


# Title Label
titleLabel = t.Label(window, text="Click Generate to get a password",
                   font=("Comic Sans", 15))
titleLabel.grid(column=0, row=0, padx=(10, 10), pady=(5, 5))

# gen button
GenerateButton = t.Button(window, text='Generate', bg="springgreen2",
                        fg="black", command=clicked_gen)
GenerateButton.grid(column=0, row=1, padx=(10, 10), pady=(5, 5))

# Show Strength Button
showStrengthButton = t.Button(window, text='Show Strength', bg="springgreen2",
                            fg="black", command=clicked_showStrength)
showStrengthButton.grid(column=0, row=6, padx=(10, 10), pady=(5, 5))

# Exit Button
exit_button = t.Button(window, text='EXIT', bg='black',
                     fg='white', command=window.destroy)
exit_button.grid(column=0, row=10, padx=(10, 10), pady=(5, 5))

window.mainloop()
