import turtle
turtle.Screen().bgcolor("Lavender")
turtle.Screen().setup(1000,1000)
Polygon=turtle.Turtle()
Sides=800
L=100
Angle=360/Sides
for r in range(Sides):
   Polygon.forward(L)
   Polygon.right(Angle)