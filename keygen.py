import random
primes = []
totientc = []
decryptc = []
for i in range(int(input("Input starting range of prime : ")),int(input("Input ending point of prime : "))):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        primes.append(i)
p = random.choice(primes)
q = random.choice(primes)
n = p*q
totient = (p-1)*(q-1)
#Key Gen
for i in range(0,totient):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        totientc.append(i)
e = random.choice(totientc)
print "Your public key is : " ,n,",",e
for d in range(0,totient):
    if d*e % totient == 1:
        print "Your private key is : " , n,",",d
