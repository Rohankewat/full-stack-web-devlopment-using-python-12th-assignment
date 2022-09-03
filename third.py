a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
i = a                      # Question no :- 4
while i<=b:
    if i == 1:
        print("",end = "")
    elif i == 2:
        print(i,end= " ")
    elif i == 3:
        print(i,end = " ")
    elif i == 5:
        print(i,end = " ")
    elif i == 7:
        print(i,end= " ")
    elif i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    print(i, end = " ")
    i += 1
print()
print()

