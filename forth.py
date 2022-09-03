a = int(input("Enter number1= "))  # Question no :- 9
b = int(input("Enter number2= "))
if a > b:
    large = a
else:
    large = b
while True:
    if large % a == 0 and large % b == 0:
        print("LCM is",large)
        break
    large = large+1
print()


        



