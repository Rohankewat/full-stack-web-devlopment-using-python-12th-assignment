i = 2       # Question no :- 3
while i<100:
    if i == 2:
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

