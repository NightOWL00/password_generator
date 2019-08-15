import random
CharList=['@','_','-','+','%','.','?','$','`','1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CharList.sort(reverse = True)
temp=[]
for passLength in range(16):
    temp.append(random.randint(0,len(CharList)-1))
x=''
for num in temp:
    x+=CharList[num]
print('The Password: ',x)
#Saving password
