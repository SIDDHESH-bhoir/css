## rail fence cipher with key=2
## q5,q14

def encrypt(s,key):
    s1=list(s)
    l0=[]
    l1=[]
    for i in range(len(s1)):
        if(i%2==0):
            l0.append(s1[i])
        else:
            l1.append(s1[i])
    a=''.join(l0)
    b=''.join(l1)
    return a+b

def decrypt(s,key):
    s1=[]
    if len(s)%2==1:
        for i in range(len(s)/key+1):
            s1.append(s[i])
            if i+len(s)/key+1<len(s):
                s1.append(s[i+len(s)/key+1])
    else:
        for i in range(len(s)/key):
            s1.append(s[i])
            s1.append(s[i+len(s)/key])
    return ''.join(s1)
s=str(input("enter string  "))
key = int(input("enter key  "))
e = encrypt(s,key)
print ("after encryption:  ",e)
d = decrypt(e,key)
print ("after decryption:  ",d)
