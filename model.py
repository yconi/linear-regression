# 2d array for the points on the cartesian plane
basicLinear = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]] #basic linear function first test

a = 0
b = 0
x = 0

def iteration(x):
    return a*x+b

# Generate a very basic function for initial tests 
def firstFunction(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 or y1 == y2:
        print(f"Invalid points")
        return 0
    else:
        global a, b
        a = (y2-y1)/(x2-x1)
        b = y1 - x1*a 

def findError(points):
    error = []
    for point in points:
        x = point[0]
        y = point[1]
        error.append(y - iteration(x))
    return error

firstFunction(basicLinear[0], basicLinear[7])
error = findError(basicLinear)
print(error)
