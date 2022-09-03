n = int(input("Enter number "))    # Question no :- 1
reverse = 0
while n != 0:
    r = n%10
    reverse = reverse*10+r
    n = n//10
print("reverse of number is",reverse)
print()