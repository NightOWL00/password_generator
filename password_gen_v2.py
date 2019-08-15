import passwordmeter
import random
import string


def password():
    CharList = '@'+'_'+'-'+'+'+' '+'.'+'?'+'$' + \
        '`' + string.ascii_letters+string.digits
    temp, x = [], ''
    for i in range(16):
        temp.append(random.randint(0, len(CharList)-1))
    for num in temp:
        x += CharList[num]
    return x


def passStrength(x):
    Strength = passwordmeter.test(x)
    return Strength


if __name__ == "__main__":
    password()
    passStrength(password())
