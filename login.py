from tkinter import *
from ToolTip import *
import signup as si
loginWindow = Tk()
loginWindow.geometry('250x200')
loginWindow.title("Login/Sign-up")
loginWindow.iconbitmap('icon/lock.ico')
loginWindow.resizable(0, 0)

# <Functions>

def functions():
    #ifexists()
    si.sign(usernameEntry.get(), passwordEntry.get(), emailEntry.get())

##def ifexists():
##    n = existORnot()
##    if n == True:
##        # msg Label
##        msgLabel = Label(
##            loginWindow, text='Username already exists. Try another one.', fg='red')
##        msgLabel.grid(column=0, row=5, padx=(10, 10), pady=(5, 5), stick='W')
##
##    else:
##        n = 'Account Created!'
##        msgLabel = Label(
##            loginWindow, text=n, fg='red')
##        msgLabel.grid(column=0, row=5, padx=(10, 10), pady=(5, 5))


# </Functions>
textLabel = Label(loginWindow, text='---- Login to continue ----',
                  font=("Helvetica", 15))
textLabel.grid(column=0, row=0, padx=(10, 10), pady=(5, 5))

# Username
usernameLabel = Label(loginWindow, text="Username :", font=("Helvetica", 10))
usernameLabel.grid(column=0, row=1, padx=(5, 5), pady=(5, 5), sticky='W')

usernameEntry = Entry(loginWindow, width=20)
usernameEntry.grid(column=0, row=1, padx=(5, 5), pady=(5, 5), sticky='E')

# password
passwordLabel = Label(loginWindow, text="Password :", font=("Helvetica", 10))
passwordLabel.grid(column=0, row=2, padx=(5, 5), pady=(5, 5), sticky='W')

passwordEntry = Entry(loginWindow, width=20, show='#')
passwordEntry.grid(column=0, row=2, padx=(5, 5), pady=(5, 5), sticky='E')

# Email
emailLabel = Label(loginWindow, text="Email :", font=("Helvetica", 10))
emailLabel.grid(column=0, row=3, padx=(5, 5), pady=(5, 5), sticky='W')

emailEntry = Entry(loginWindow, width=20)
emailEntry.grid(column=0, row=3, padx=(5, 5), pady=(5, 5), sticky='E')

# loginButton
loginButton = Button(loginWindow, text=' Login ')
loginButton.grid(column=0, row=4, sticky='E', padx=(5, 10), pady=(5, 5))

# Signup Button
signupButton = Button(loginWindow, text=' Signup ', command = functions)
signupButton.grid(column=0, row=4, padx=(45, 5), pady=(5, 5))

# INFO Label
info = Label(text=' INFO?')
CreateToolTip(info, '''If you are using the app for the first time\n
then first sign up and after that login to\n
the app to create and manage\n 
strong passwords!!!
''')
info.grid(column=0, row=4, padx=(5, 5), pady=(5, 5), stick='W')


loginWindow.mainloop()
