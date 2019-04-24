##multiplicative cipher
## q2,q13

def inverse(a,z):
    k=1
    while(True):
        if((a*k)%z==1):
            return k
        k+=1
        
def encrypt(s,key):
    list1 = list(s)
    list2 = []
    for i in list1:
        x = ord(i)
        x-=97
        x=(x*key)%26
        x+=97
        y = chr(x)
        list2.append(y)
    return ''.join(list2)

def decrypt(s,key):
    list1 = list(s)
    list2 = []
    kinv = inverse(key,26)
    for i in list1:
        x = ord(i)
        x-=97
        x = (x*kinv)%26
        x+=97
        y = chr(x)
        list2.append(y)
    return ''.join(list2)

plain = str(input("enter string to be encrypted:  "))
key = int(input("enter key"))
e = encrypt(plain,key)
print ("after encryption:  ",e)
d = decrypt(e,key)
print ("after decryption:  ",d)
