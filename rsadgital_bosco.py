## rsa for digital signature
## q8

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def inv(a,n):
    for i in range(n+1):
        if (a*i)%n==1:
            return i

m=int(input("enter message: "))
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
print "public key of sender = (",e,",",n,")"
ct=(m**d)%n
print "sender encrypts using sender's private key...\ncipher text: ",ct
print "receiver decrypts using sender's public key..."
pt=(ct**e)%n
print "after decryption: ",pt
