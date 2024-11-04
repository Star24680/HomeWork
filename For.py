def count(number):
    count = 0
    for digit in str(number):
        count += 1
    return count

number = int(input("Enter a number: "))

Result = count(number)
print("Number of digits:", Result)