from tkinter import *
from ToolTip import *
from functions import existORnot, signup

# <Functions>


def login():
    root2 = Tk()
    root2.geometry('270x100')
    root2.title("Login")
    root2.resizable(0, 0)
    usernameLabel = Label(root2, text='USERNAME: ')
    usernameLabel.grid(column=0, row=1, padx=(10, 10), pady=(5, 5))
    usernameEntry = Entry(root2, width=25)
    usernameEntry.grid(column=1, row=1, padx=(10, 10), pady=(5, 5))
    passwordLabel = Label(root2, text='PASSWORD: ')
    passwordLabel.grid(column=0, row=2, padx=(10, 10), pady=(5, 5))
    passwordEntry = Entry(root2, width=25)
    passwordEntry.grid(column=1, row=2, padx=(10, 10), pady=(5, 5))
    testButton = Button(root2, text='Login', padx=10,
                        pady=7, command=root.destroy)
    testButton.grid(column=1, row=3, padx=10, pady=7)
    root2.mainloop()


def register():

    def check():
        msgLabel = Label(registerWindow, text='', fg='red')
        msgLabel.grid(column=0, row=7, padx=(
            10, 10), pady=(5, 5), columnspan=2)
        msgLabel['text'] = ' '
        if existORnot(usernameEntry.get()) == True:
            txt = 'Username already exists. Try another one.'
            msgLabel['text'] = txt
        else:
            txt = 'Account Created'
            msgLabel['text'] = txt

    registerWindow = Tk()
    registerWindow.geometry('300x270')
    registerWindow.title("Register")
    registerWindow.iconbitmap('img/lock.ico')
    # registerWindow.resizable(0, 0)

    textLabel = Label(registerWindow, text=' Register here ',
                      font=("Helvetica", 15))
    textLabel.grid(column=0, row=0, padx=(10, 10), pady=(5, 5), columnspan=2)

    # Username
    usernameLabel = Label(registerWindow, text="Username :",
                          font=("Helvetica", 10))
    usernameLabel.grid(column=0, row=1, padx=(5, 5), pady=(5, 5), sticky='W')

    usernameEntry = Entry(registerWindow, width=25)
    usernameEntry.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))

    # password
    passwordLabel = Label(registerWindow, text="Password :",
                          font=("Helvetica", 10))
    passwordLabel.grid(column=0, row=2, padx=(5, 5), pady=(5, 5), sticky='W')

    passwordEntry = Entry(registerWindow, width=25)
    passwordEntry.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))

    # confirm password
    con_passwordLabel = Label(registerWindow, text="Confirm Password :",
                              font=("Helvetica", 10))
    con_passwordLabel.grid(column=0, row=3, padx=(5, 5),
                           pady=(5, 5), sticky='W')

    con_passwordEntry = Entry(registerWindow, width=25, show='*')
    con_passwordEntry.grid(column=1, row=3, padx=(5, 5), pady=(5, 5))

    # Email
    emailLabel = Label(registerWindow, text="Email :", font=("Helvetica", 10))
    emailLabel.grid(column=0, row=4, padx=(5, 5), pady=(5, 5), sticky='W')

    emailEntry = Entry(registerWindow, width=25)
    emailEntry.grid(column=1, row=4, padx=(5, 5), pady=(5, 5))

    # Confirm Email
    con_emailLabel = Label(
        registerWindow, text="Confirm Email :", font=("Helvetica", 10))
    con_emailLabel.grid(column=0, row=5, padx=(5, 5), pady=(5, 5), sticky='W')

    con_emailEntry = Entry(registerWindow, width=25, show='#')
    con_emailEntry.grid(column=1, row=5, padx=(5, 5), pady=(5, 5))

    # Signup Button
    signupButton = Button(registerWindow, text=' Signup ',
                          command=check)
    signupButton.grid(column=1, row=6, padx=(5, 5),
                      pady=(5, 5))
    registerWindow.mainloop()


# </Functions>

root = Tk()
root.geometry('250x70')
root.title("Login/Register")
root.resizable(0, 0)

# INFO Label
info = Label(text=' INFO?')
CreateToolTip(info, '''If you are using the app for the first time\n
then first sign up and after that login to\n
the app to create and manage\n 
strong passwords!!!
''')
info.grid(column=2, row=0)
loginButton = Button(root, text='LOGIN', command=login)
loginButton.grid(column=0, row=0, padx=10, pady=10)
registerButton = Button(root, text='REGISTER', command=register)
registerButton.grid(column=1, row=0, padx=10, pady=10)

root.mainloop()
