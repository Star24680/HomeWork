def circumference(R):
    pi = 3.14
    circumference = 2 * pi * R
    return circumference

radius = float(input("Enter the radius of the circle: "))

circumference = circumference(radius)
print("Circumference of the circle:", circumference)

# R stands for Radius