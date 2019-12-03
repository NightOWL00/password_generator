import base64
from tkinter import *
import passwordmeter
import random
import string
import pyperclip as pc
import os
os.mkdir('DATA_FILES')
os.system("attrib +h DATA_FILES")
if os.path.exists('DATA_FILES/data_pgs.dtap'):
    os.rename('DATA_FILES/data_pgs.dtap',
              'DATA_FILES/Good_File_DO_NOT_DELETE_Contains_password.txt')
else:
    print('file_not_found'.upper())


def encrypt(plain_data):
    plain_data = plain_data.encode()
    encoded_data = base64.b64encode(plain_data)
    return encoded_data


def decrypt(encrypted_data):
    decoded_data = base64.b64decode(encrypted_data)
    return decoded_data


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
    lbl1['bg'] = "#C0C0C0"
    pc.copy(pwd)
    pwdStrength = passStrength(pwd)

    lbl3 = Label(window, text='Strength of password: ' +
                 str(pwdStrength[0])[0:5], bg="black", fg="springgreen2")
    lbl3.grid(column=0, row=3, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2), columnspan=2)

    lbl2 = Label(window, text='Save this password for: ',
                 bg="black", fg="springgreen2")
    lbl2.grid(column=0, row=4, padx=(10, 0), pady=(5, 5), ipadx=(5), ipady=(2))

    def save_it():
        file = 'DATA_FILES/Good_File_DO_NOT_DELETE_Contains_password.txt'
        f = open(file, 'a')
        data = f'Password for \'{ent1.get()}\' is \'{pwd}\' \n'
        f.write('\n' + encrypt(data).decode() + '\n')
        f.close()

    def view_passwords():
        file = 'DATA_FILES\Temp_file_DELETE_AFTER_USE.txt'  # windows file system
        Message = 'Delete this file after use to avoid password leakage'
        f = open(file, 'w')
        f.write(Message+'\n')
        with open("DATA_FILES/Good_File_DO_NOT_DELETE_Contains_password.txt") as password_file:
            for line in password_file.readlines():
                f.write(decrypt(line).decode() + '\n')
        f.close()
        os.popen(file)

    ent1 = Entry(window, width=20)
    ent1.grid(column=1, row=4, padx=(10, 0), pady=(5, 5), ipadx=(5), ipady=(2))

    btn2 = Button(window, text='    Save    ', bg="black",
                  fg="springgreen2", command=save_it)
    btn2.grid(column=0, row=5, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2))
    btn3 = Button(window, text='    View Passwords    ', bg="black",
                  fg="springgreen2", command=view_passwords)
    btn3.grid(column=1, row=5, padx=(10, 0), pady=(
        5, 5), ipadx=(5), ipady=(2))


btn1 = Button(window, text='Generate and copy',
              bg="black", fg="springgreen2", command=magic)
btn1.grid(column=0, row=0, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), columnspan=2)

lbl1 = Label(window, text=' ')
lbl1.grid(column=0, row=1, padx=(10, 0), pady=(
    5, 5), ipadx=(5), ipady=(2), columnspan=2)

window.mainloop()

# On exit delete decrypted file
if os.path.exists("DATA_FILES/Temp_file_DELETE_AFTER_USE.txt"):
    os.remove("DATA_FILES/Temp_file_DELETE_AFTER_USE.txt")
else:
    sys.exit
os.rename('DATA_FILES/Good_File_DO_NOT_DELETE_Contains_password.txt',
          'DATA_FILES/data_pgs.dtap')
