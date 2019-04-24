##affine cipher only encryption is asked in the question
## q6,q15

def encrypt(s,k1,k2):
    s1=list(s)
    list1=[]
    for i in s1:
        x=ord(i)
        x-=97
        x=(x*k1+k2)%26
        x+=97
        list1.append(chr(x))
    return ''.join(list1)
        

s=str(input("enter plain text: "))
k1=int(input("enter k1,k2: "))
k2=int(input())
e=encrypt(s,k1,k2)
print("after encryption: ",e)
