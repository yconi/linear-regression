m = 0
b = 0

def iteration(x):
    return m*x+b

# Generate a very basic function for initial tests 
def firstFunction(points):
    x1, y1 = points[0]
    x2, y2 = points[len(points) - 1]

    if x1 == x2 or y1 == y2:
        print(f"Invalid points")
        return 0
    else:
        global m,b
        m = (y2-y1)/(x2-x1)
        b = y1 - x1*m

# Find how offset the line is from the points
def findError(points):
    error = []
    for point in points:
        x = point[0]
        y = point[1]
        error.append(y - iteration(x))
    return error

def findAvgError(points):
    error = []
    for point in points:
        x = point[0]
        y = point[1]
        error.append(y - iteration(x))
    return sum(error)/len(error)

# Tries to reduce the average error (it does not means that every individual error will decrease even if it tends to happens)

history_error = [] # keep the error during the train for graphs

def fit(data):
    global m, b
    error = findAvgError(data)
    history_error.append(error)
    b += error*0.01
    if error <= 0.05 and error >= - 0.05:
        return 0
    else:
        m+= error*0.1
        fit(data)