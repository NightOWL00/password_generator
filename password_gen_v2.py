import passwordmeter
import random
import string


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


store_firstPassword = genPassword()


for i in range(10):
    x = genPassword()
    t = (x, passStrength(x))


print(store_firstPassword, passStrength(store_firstPassword))


# if float((passStrength(store_firstPassword))[0]) < 0.8:
#     new_Password = genPassword()
#     print(new_Password, passStrength(new_Password))
