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


def password():
    x = genPassword()
    while float((passStrength(x))[0]) < 0.8:
        x = genPassword()
    return x


if __name__ == '__main__':
    genPassword()
    passStrength(genPassword)
    password()
