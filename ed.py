def encrypt(l):
    d = {'a':'on','b':'fu','c':'.@','d':'xn','e':'na','f':'af','g':'_f','h':'_g','i':'_m','j':'@0','k':'@9','l':'fn','m':'le','n':'ec','o':'nj','p':'vj','q':'kg','r':'ap','s':'ps','t':'hs','u':'ao','v':'pk','w':'vg','x':'lr','y':'us','z':'gl','A':'xf','B':'sn','C':'al','D':'nl','E':'cn','F':'bu','G':'da','H':'dx','I':'fs','J':'@a','K':'la','L':'ac','M':'~n','N':'_e','O':'-a','P':'no','Q':'?n','R':'$m','S':'tk','T':'x@','U':'?e','V':'@?','W':'bx','X':'f~','Y':'jn','Z':'@~','@':'zp','_':'pc','-':'2n','+':'8c',' ':'x6','.':'5h','?':'9u','$':'yo','~':'oj','1':'ye','2':'ya','3':'am','4':'pm','5':'8b','6':'0m','7':'_-','8':'^*','9':'&y'}
    a = list(d.keys())
    b = list(d.values())
    l1 = []
    for i in range(len(l)):
        for j in range(len(a)):
            if l[i]==a[j]:
                l1.append(b[j])
                break
    return l1

def decrypt(a):    
    d1 = {'a':'on','b':'fu','c':'.@','d':'xn','e':'na','f':'af','g':'_f','h':'_g','i':'_m','j':'@0','k':'@9','l':'fn','m':'le','n':'ec','o':'nj','p':'vj','q':'kg','r':'ap','s':'ps','t':'hs','u':'ao','v':'pk','w':'vg','x':'lr','y':'us','z':'gl','A':'xf','B':'sn','C':'al','D':'nl','E':'cn','F':'bu','G':'da','H':'dx','I':'fs','J':'@a','K':'la','L':'ac','M':'~n','N':'_e','O':'-a','P':'no','Q':'?n','R':'$m','S':'tk','T':'x@','U':'?e','V':'@?','W':'bx','X':'f~','Y':'jn','Z':'@~','@':'zp','_':'pc','-':'2n','+':'8c',' ':'x6','.':'5h','?':'9u','$':'yo','~':'oj','1':'ye','2':'ya','3':'am','4':'pm','5':'8b','6':'0m','7':'_-','8':'^*','9':'&y'}
    a1 = list(d1.keys())
    b1 = list(d1.values())
    l1 = []
    for i in range(len(a)):
        for j in range(len(b1)):
            if a[i]==b1[j]:
                l1.append(a1[j])
                break
    return l1

l='kabjobfoib39niq3 tw39hgibiwo'
print(encrypt(l))
print(decrypt(l))