#START

num=int(input("Enter a two-digit number:"))
if 10<=num<=99:
    tens=num//10
    ones=num%10
    if tens == ones:
        print("tens equals ones")
    else:
        print("tens not equals ones")
else:
    print("number should be between 10-99")

#STOP
