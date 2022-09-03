n = int(input("Enter number "))          # Question no:- 6
i = 1  
count = 0                
while i<=10*n:
    if count == n:
        break
    if i == 1:
        print("",end = "")
    elif i == 2:
        print(i,end= " ")
        count += 1
    elif i == 3:
        print(i,end = " ")
        count += 1
    elif i == 5:
        print(i,end = " ")
        count += 1
    elif i == 7:
        print(i,end= " ")
        count += 1
    elif i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    print(i, end = " ")
                    count += 1
    i += 1
print()
print()
