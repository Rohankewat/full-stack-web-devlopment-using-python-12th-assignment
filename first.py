n = int(input("Enter number ")) # Question no :- 2
a = True
i = 2
while i<=int(n/2):
    if n % i == 0:
        a = False
        break
    i += 1
if a:
    if n == 1:
        print("neither prime nor composite")
    else:
        print("number is prime")
else:
    print("not a prime number")
print()      