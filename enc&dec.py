n = int(input("Please enter `n` or the common integer of your key : "))
eod = int(input("Enter 1 to encrypt a number and 2 to decrypt a number : ")) 
if eod==1:
    m = int(input("Please enter a number less than n : " ))
    e = int(input("Please enter your encrypton key : " ))
    print (m**e)%n
if eod==2:
    c = int(input("Please enter your encrypted message : " ))
    d = int(input("Please enter your decrypton key : " ))
    print (c**d)%n
