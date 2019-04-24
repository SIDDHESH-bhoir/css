import math
p=7
q=11
n=p*q
phy=(p-1)*(q-1)
print("Value of n and phy:",n,phy)
a=5
for a in range (5,phy):
    if(math.gcd(a,phy)==1):
        e=a
        break
print("value of e:",e)

for k in range(2,100):
    if(((k*phy)+1)%e==0):
        d=(int)((k*phy+1)/e)
        break
print("Value of d:",d)

msg=int(input("Enter the message: "))
print("Message Encryption")
enc=(msg**e)%n 
dec=(enc**d)%n 
print("Encryption and decryption:",enc,dec)



