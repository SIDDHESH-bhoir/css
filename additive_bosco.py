##Additive/ceasar/shift cipher (ceasar cipher is additive where key=3)
## q1,q3,q4


def encrypt(s,key):
    list1 = list(s)
    list2 = []
    for i in list1:
        x = ord(i)
        x-=97
        x=(x+key)%26
        x+=97
        y = chr(x)
        list2.append(y)
    return ''.join(list2)

def decrypt(s,key):
    list1 = list(s)
    list2 = []
    for i in list1:
        x = ord(i)
        x-=97
        x-=key
        if(x<0):
            x+=26
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
