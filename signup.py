def sign(username,password,email):
    userdict = {}
    userdict[username] = password, email
    userkeys = userdict.keys()
    userkeys = list(userkeys)
    file = open("DATABASE.txt","a+")
    file.write(str(userdict))
    file.write('\n')
    file.close()
    file1 = open("KEYDATA.txt","a+")
    file1.write(userkeys.pop())
    file1.write('\n')
    file1.close()

if  __name__ == "__main__" :
    sign()
