n = int(input("Enter the shifting value: "))
st = input("Enter the message: ").lower()
n_st = ''
print("\n1. Encryption\n2. Decryption")
ch = int(input("Enter your choice: "))
if ch==1:
    for k in st:
        if n<=ord('z') - ord(k)<=26:
            n_st+=chr(ord(k)+n)
        elif 0<=ord('z')-ord(k)<n:
            a = ord('z') - ord(k)
            n_st += chr((n-a)+96)
        else:
            n_st+=k
    print(n_st)
elif ch==2:
    for k in st:
        if 96+n< ord(k) <= ord('z'):
            n_st+=chr(ord(k)-n)
        elif 96<ord(k)<=96+n:
            a = ord(k) - ord('a')
            n_st+=chr(123-(n-a))
        else:
            n_st+=k
    print(n_st)
else:
    print("Incorrect Input")
