n = int(input("Enter number "))        # Question no :- 5
i = n+1
while i <= (10*n+10):
    if i == 1:
        print("",end = "")
    elif i == 2:
        print("next prime number of",n,"is",i)
        break
    elif i == 3:
        print("next prime number of",n,"is",i) 
        break
    elif i == 5:
        print("next prime number of",n,"is",i)
        break
    elif i == 7:
        print("next prime number of",n,"is",i)
        break
    elif i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    print("next prime number of",n,"is",i)
                    break
    i += 1
print()
print()
