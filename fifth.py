a = int(input("Enter 1st number "))  # Question no :- 10
b = int(input("Enter 2nd number "))
if a > b:
    small = b
else:
    small = a
while True:
    if a % small == 0 and b % small == 0:
        print("HCF of",a,"and",b,"is",small)
        break
    small = small-1
print()
    
