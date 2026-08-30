import math

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

# Standard Error Function: Find the difference (error) between the predicted Y value and the actual Y value.

def findStdError(points):
    error = []
    for point in points:
        x = point[0]
        y = point[1]
        error.append((y - iteration(x)) ** 2)
    return (sum(error)/(len(error)-2)) ** 0.5

# Fit function: Tries to reduce the standard error (it does not means that every individual error will decrease even if it tends to happens)

history_error = [] # keep the error during the train for graphs
history_m = []
history_b = []

def fit(data, learning_rate=0.01, epochs=100):
    global m, b

    history_m.clear()
    history_b.clear()
    history_error.clear()

    for _ in range(epochs):

        dm = 0
        db = 0

        for x, y in data:

            prediction = iteration(x)
            error = prediction - y

            dm += error * x
            db += error

        dm /= len(data)
        db /= len(data)

        m -= learning_rate * dm
        b -= learning_rate * db

        history_m.append(m)
        history_b.append(b)

        history_error.append(findStdError(data))