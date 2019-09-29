def calculateMPG(){
    import math

    radius = input("Please enter a radius: ")

    radiusInt = int(radius)

    areaOfCircle = (math.pi * radiusInt ** 2)

    aoC = str(areaOfCircle)

print("The area of the circle is " + aoC)
}
