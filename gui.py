import tkinter as t
import password_gen_v2 as pg
import pyperclip as pc

password = pg.password()


def clicked_gen():
    # passwordStr
    passwordStr = t.Label(window1, text=str(password), font=("Comic Sans", 20))
    passwordStr.grid(column=0, row=1, padx=(20, 25), pady=(5, 5), sticky='E')

    # copy Button
    copyButton = t.Button(window1, text='Copy', command=copyButtonClicked, bg="springgreen2",
                          fg="black",)
    copyButton.grid(column=0, row=4, padx=(10, 10), pady=(
        20, 10), ipadx=(5), ipady=(2), sticky='W')
    # Password Strength
    passwordStrength = t.Label(window1, text='Password Strength (Between 0 and 1) is '+str(pg.passStrength(password))[:7]+')', bg="springgreen2",
                               fg="black")
    passwordStrength.grid(column=0, row=3, padx=(10, 30),
                          pady=(5, 5), sticky='E')

    # save
    saveButton = t.Button(window1, text='Save Password',
                          bg="springgreen2", fg="black")
    saveButton.grid(column=0, row=5, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2), sticky='W')


def copyButtonClicked():
    pc.copy(password)

def createwindow():

    #Window of UserID
    window2 = t.Tk()
##    window1.geometry('400x300')
##    window1.title('UserID')
    canvas1 = t.Canvas(window2, width = 400, height = 300)
    canvas1.pack()

    entry1 = t.Entry()
    canvas1.create_window(200, 140, window=entry1)
    

window1 = t.Tk()
window1.geometry('400x300')
window1.title("Password Generator and store")
window1.resizable(0, 0)

# Title Label
titleLabel = t.Label(window1, text="Click Generate to get a password",
                     font=("Comic Sans", 15))
titleLabel.grid(column=0, row=0, padx=(45, 45), pady=(5, 5))

# gen button
GenerateButton = t.Button(window1, text='Generate', bg="springgreen2",
                          fg="black", command=clicked_gen)
GenerateButton.grid(column=0, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), sticky='W')

# view passwords
viewButton = t.Button(window1, text='View saved passwords',
                      bg="springgreen2", fg="black",command=createwindow)
viewButton.grid(column=0, row=5, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), sticky='E')

# Exit Button
exit_button = t.Button(window1, text='EXIT', bg='black',
                       fg='white', command=window1.destroy)
exit_button.grid(column=0, row=4, padx=(10, 10),
                 pady=(20, 10), ipadx=(5), ipady=(2), sticky='E')


window1.mainloop()
