from tkinter import *
from functions import *
import pyperclip as pc

window = Tk()
window.geometry('290x130')
window.title("Password Generator and store")
#window.resizable(0, 0)

password = password()


def genandcopy():
    window.geometry('450x200')
    # passwordStr
    passwordStr = Label(window, text=str(password), font=("Helvetica", 20))
    passwordStr.grid(column=1, row=0, padx=(20, 25), pady=(5, 5), sticky='S')
    pc.copy(password)

    # Password Strength
    passwordStrength = Label(window, text='Password Strength (Between 0 and 1) is '+str(passStrength(password))[:7]+')', bg="springgreen2",
                             fg="black")
    passwordStrength.grid(column=1, row=1, padx=(10, 30),
                          pady=(5, 5), sticky='NE')
    # Save Entry
    txt = Entry(window, width=30)
    txt.grid(column=1, row=2, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2))

    def saveFunction():
        passfile = open('passwords.txt', '+a')
        passfile.write('\nThe password is for "' +
                       txt.get() + '": ' + password+'\n')
        passfile.close()

    # save
    saveButton = Button(window, text='Save Password for',
                        bg="springgreen2", fg="black", command=saveFunction)
    saveButton.grid(column=0, row=2, padx=(10, 0),
                    pady=(5, 5), ipadx=(5), ipady=(2))


generate_and_copyButton = Button(window, text='Generate and Copy', bg="springgreen2",
                                 fg="black", command=genandcopy)
generate_and_copyButton.grid(column=0, row=0, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))

# view passwords
viewButton = Button(window, text='View saved passwords',
                    bg="springgreen2", fg="black")
viewButton.grid(column=0, row=3, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2))

# logged in as
lb1 = Label(window, text='LOGGED IN AS', fg='#B332FF')
lb1.grid(column=0, row=4, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), stick='S')

# username
lb2 = Label(window, text='<< USERNAME >>', fg='#B332FF')
lb2.grid(column=1, row=4, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), sticky='S')

window.mainloop()
