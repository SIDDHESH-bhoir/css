## rsa for cryptosystem
## q7

def inv(a,n):
    for i in range(1,n+1):
        if (a*i)%n==1:
            return i

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

m=int(input("enter messager: "))
p=211
q=227
n=p*q
phi=(p-1)*(q-1)
e=0
for i in range(2,phi):
    if gcd(i,phi)==1:
        e=i
        break
d=inv(e,phi)
print "public key of receiver = (",e,",",n,")"
ct=(m**e)%n
print "sender encrypts using receiver's public key... \ncipher text: ",ct
print "receiver decrypts using receiver's private key..."
pt=(ct**d)%n
print "after decryption: ",pt
