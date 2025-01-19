msg = input("enter the message to be encoded: ")
diff = int(input("enter the amount of characters to skip: "))
newMsg = ""

for char in range(0,len(msg)):
    if((ord(msg[char])+diff)<=90):
        newMsg += chr(ord(msg[char]) + diff)
    else:
        newMsg +=  chr(((ord(msg[char])+diff) - ord('Z')) + 64)

print("\n the encrypted message is:",newMsg)



code = input("enter the encrypted code: ")
skip = int(input("enter the amount of characters skipped: "))
ogMsg = ""

for char in code:
    if((ord(char)-skip)>=65):
        ogMsg += chr(ord(char)-skip)
    else:
        print((91-(ord(char)-64)))
        ogMsg += chr((90-abs(((ord(char)-skip)-64))))

print("\n the decrypted message is:",ogMsg)