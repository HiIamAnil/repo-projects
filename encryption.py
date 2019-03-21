alphabet    ='abcdefghijklmnopqrstuvwxyz'
key         =4
message     =input('enter the input message  : ')
k=""
for i in message:
    index = alphabet.index(i) + 3
    k=k+alphabet[index]

print("encrypted message is "+k)
message=k
k=''

for i in message:
    index = alphabet.index(i) - 3
    k=k+alphabet[index]

print("decrypted message is "+k)

