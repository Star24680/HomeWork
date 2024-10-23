try:
    age = int(input("Enter age: "))
    if age%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
except ValueError:
    print("Error: Not an integer.")
