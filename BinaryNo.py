decimal_number = float(input("Enter a decimal number: "))  
binary_number = ""

while decimal_number > 0:  
    remainder = decimal_number % 2  
    binary_number = str(remainder) + binary_number  
    decimal_number = decimal_number // 2  
if binary_number == "":
    binary_number = "0"
print("Binary:", binary_number)  
