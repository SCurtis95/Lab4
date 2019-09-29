
x = 65
x1 = 45
y = 57
y1 = 87

def calcDistance(x,x1,y,y1):
    
    import math
    points = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    dist = int(points)
    calc = print("The total distance between points is : ", dist)
    return calc

calcDistance(x,x1,y,y1)

