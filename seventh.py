n = int(input("Enter number ")) # Question no :- 8
a = 0
b = 1
count = 2
print(a,b,sep = "  ",end = "  ")
i = 1
while i<=30*n:
    if count == n:
        break
    elif count <= n:
        c = a+b
        print(c,end = "  ")
        count += 1
        d = a      # Swaping
        a = b
        b = c
    i += 1
print()
        
