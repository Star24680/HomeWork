def filter (start, end):
    print("Even squares:", end=" ")
    for num in range(start, end + 1):
        square = num ** 2
        if square % 2 == 0:
            print(square, end=" ")
    
    print("\n Odd squares:", end=" ")
    for num in range(start, end + 1):
        square = num ** 2
        if square % 2 != 0:
            print(square, end=" ")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

filter(start, end)
print (filter)