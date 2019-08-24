file = 'cry_pass.txt'
f = open(file,'r')

temp = f.read().splitlines()
print(temp)

f.close()
