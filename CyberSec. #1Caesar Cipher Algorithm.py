def encryption(en_st):
    new_st = ''
    for k in en_st:
        if n<=ord('z') - ord(k)<=26:
            new_st+=chr(ord(k)+n)
        elif 0<=ord('z')-ord(k)<n:
            a = ord('z') - ord(k)
            new_st += chr((n-a)+96)
        else:
            new_st+=k
    return new_st

def decryption(de_st):
    new_st = ''
    for k in de_st:
        if 96+n< ord(k) <= ord('z'):
            new_st+=chr(ord(k)-n)
        elif 96<ord(k)<=96+n:
            a = ord(k) - ord('a')
            new_st+=chr(123-(n-a))
        else:
            new_st+=k
    return new_st

n = int(input("Enter the shifting value: "))
st = input("Enter the message: ").lower()
print("\n1. Encryption\n2. Decryption")
ch = int(input("Enter your choice: "))

if ch==1:
    print(encryption(st))

elif ch==2:
    print(decryption(st))

else:
    print("Incorrect Input")
