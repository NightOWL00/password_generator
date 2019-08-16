import passwordmeter
import random
import string


def password():
    CharList = '@'+'_'+'-'+'+'+' '+'.'+'?'+'$' + \
        '`' + string.ascii_letters+string.digits
    temp, x = [], ''
    for i in range(16):
        x += CharList[random.randint(0, len(CharList)-1)]
    return x


def passStrength(x):
    Strength = passwordmeter.test(x)
    return Strength


if __name__ == '__main__':
    password()
    passStrength(password())
