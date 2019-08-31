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

def encrypt(n):
    d = {'a':'on','b':'fu','c':'.@','d':'xn','e':'na','f':'af','g':'_f','h':'_g','i':'_m','j':'@0','k':'@9','l':'fn','m':'le','n':'ec','o':'nj','p':'vj','q':'kg','r':'ap','s':'ps','t':'hs','u':'ao','v':'pk','w':'vg','x':'lr','y':'us','z':'gl','A':'xf','B':'sn','C':'al','D':'nl','E':'cn','F':'bu','G':'da','H':'dx','I':'fs','J':'@a','K':'la','L':'ac','M':'~n','N':'_e','O':'-a','P':'no','Q':'?n','R':'$m','S':'tk','T':'x@','U':'?e','V':'@?','W':'bx','X':'f~','Y':'jn','Z':'@~','@':'zp','_':'pc','-':'2n','+':'8c',' ':'x6','.':'5h','?':'9u','$':'yo','~':'oj','1':'ye','2':'ya','3':'am','4':'pm','5':'8b','6':'0m','7':'_-','8':'^*','9':'&y'}
    a = list(d.keys())
    b = list(d.values())
    l1 = []
    for i in range(len(n)):
        for j in range(len(a)):
            if n[i]==a[j]:
                l1.append(b[j])
                break
    l2 = '&'.join(l1)
    return l2

def decrypt(a):
    a = a.split('&')
    d1 = {'a':'on','b':'fu','c':'.@','d':'xn','e':'na','f':'af','g':'_f','h':'_g','i':'_m','j':'@0','k':'@9','l':'fn','m':'le','n':'ec','o':'nj','p':'vj','q':'kg','r':'ap','s':'ps','t':'hs','u':'ao','v':'pk','w':'vg','x':'lr','y':'us','z':'gl','A':'xf','B':'sn','C':'al','D':'nl','E':'cn','F':'bu','G':'da','H':'dx','I':'fs','J':'@a','K':'la','L':'ac','M':'~n','N':'_e','O':'-a','P':'no','Q':'?n','R':'$m','S':'tk','T':'x@','U':'?e','V':'@?','W':'bx','X':'f~','Y':'jn','Z':'@~','@':'zp','_':'pc','-':'2n','+':'8c',' ':'x6','.':'5h','?':'9u','$':'yo','~':'oj','1':'ye','2':'ya','3':'am','4':'pm','5':'8b','6':'0m','7':'_-','8':'^*','9':'&y'}
    a1 = list(d1.keys())
    b1 = list(d1.values())
    l1 = []
    for i in range(len(a)):
        for j in range(len(b1)):
            if a[i]==b1[j]:
                l1.append(a1[j])
                break
    return ''.join(l1)

def existORnot(userinput):
    file = 'KEYDATA.txt'
    f = open(file,'r')
    temp = f.read().splitlines()
    for i in range(len(temp)):
        if temp[i] == userinput:
            return True
    f.close()
    return False

def signup(username, password, email):
    userdict = {}
    userdict[username] = password, email
    userkeys = userdict.keys()
    userkeys = list(userkeys)
    file = open("DATABASE.txt", "a+")
    file.write(str(userdict))
    file.write('\n')
    file.close()
    file1 = open("KEYDATA.txt", "a+")
    file1.write(userkeys.pop())
    file1.write('\n')
    file1.close()
