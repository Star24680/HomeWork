X = int(input("Enter a number: "))

count = 0

if X == 0:
    count = 1
else:
    while X > 0:
        X = X // 10 
        count += 1 

print("Number of digits:", count)
