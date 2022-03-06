from graphics.circle import *
import graphics.rectangle
import graphics..sphere
from graphics.cuboid import *

l =int(input("Enter the length: "))
b =int(input("Enter the breadth: "))
h =int(input("Enter the height: "))
r= int(input("Enter the Radius: "))

Arec=graphics.rectangle.getArea(l,b)
Prec=graphics.rectangle.getPerimeter(l,b)

Asph=graphics.sphere.getArea(r)
Psph=graphics.sphere.getPerimeter(r)

Acub=cuboid.getArea(l,b,h)
Pcub=cuboid.getPerimeter(l,b,h)

Acir=getArea(r)
Pcir=getArea(r)

print("\nArea of Rectangle : ",Arec)
print("Area of Sphere : ",Asph)
print("Area of Cuboid : ",Acub)
print("Area of Circle : ",Acir)

print("\nPerimeter of Rectangle : ",Prec)
print("Perimeter of Sphere : ",Psph)
print("Perimeter of Cuboid : ",Pcub)
print("Perimeter of Circle : ",Pcir)