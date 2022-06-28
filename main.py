def square(a):
    return a**2


def rectangle(a, b):
    return a * b


def triangle(a, b):
    return (a * b) / 2


def circle(a):
    import math
    return math.pi * (a ** 2)


def ext():
    return exit()


print("**********************")
print("MENU")
print("**********************")

print("[1] - Area of square")
print("[2] - Area of rectangle")
print("[3] - Area of triangle")
print("[4] - Area of circle")
print("[5] - Exit")

print("----------------------")
choice = int(input("Enter your choice: "))
print("----------------------")

if choice == 1:
    print("AREA OF SQUARE")
    print("----------------------")
    a = int(input("Enter the side of the square: "))
    print()
    print("The area is", square(a), "sq. units")
elif choice == 2:
    print("AREA OF RECTANGLE")
    print("----------------------")
    a = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the width of the rectangle: "))
    print()
    print("The area is", rectangle(a, b), "sq. units")
elif choice == 3:
    print("AREA OF TRIANGLE")
    print("----------------------")
    a = int(input("Enter the base of the triangle: "))
    b = int(input("Enter the width of the height of the triangle: "))
    print()
    print("The area is", triangle(a, b), "sq. units")
elif choice == 4:
    print("AREA OF CIRCLE")
    print("----------------------")
    a = int(input("Enter the radius of the circle: "))
    print()
    print("The area is", circle(a), "sq. units")
elif choice == 5:
    print("Thank you!")
    quit()
else:
    print("INPUT NOT INCLUDED!")
