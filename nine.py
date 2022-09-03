a = int(input("Enter 1st number "))  # Question no :- 7
b = int(input("Enter 2nd number "))
if a > b:
    small = b
else:
    small = a
while True:
    if a % small == 0 and b % small == 0:
        if small == 1:
            print(a,"and",b,"are co-prime numbers")
            break
        else:
            print(a,"and",b,"are not co-prime numbers")
            break
    small = small-1
print()