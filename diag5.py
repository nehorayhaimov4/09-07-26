#START

num=int(input("Enter a two-digit number:"))
if 10<=num<=99:
    #YES
    tens=num//10
    ones=num%10
else:
    #NO
    print("number should be between 10-99")

if tens==ones:
    #YES
    print("tens equals ones")
else:
    #NO
    print("tens not equals ones")

#STOP