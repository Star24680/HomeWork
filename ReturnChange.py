def calculate_change(Bill, Paid):
    change = Paid - Bill
    return change

bill = 2.50
paid = 4.00

change = calculate_change(bill, paid)
print("Change:", change)
