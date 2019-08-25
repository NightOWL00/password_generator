def existORnot(userinput):
    file = 'username.txt'
    f = open(file,'r')
    temp = f.read().splitlines()
    for i in range(len(temp)):
        if temp[i] == userinput:
            return True
    return False
    f.close()
