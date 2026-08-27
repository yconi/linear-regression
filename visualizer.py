import matplotlib.pyplot as plt

def plot(points, modelEval):
    x_pred, y_pred = modelEval
    x_points = points[:, 0] # Get the whole first collumn
    y_points = points[:, 1] # Get the whole second collumn

    print(x_points, y_points)

    # Plot the data
    plt.figure(figsize=(8,4))
    plt.plot(x_pred, y_pred, color='blue', label='Trend Line')
    plt.scatter(x_points, y_points, color='black', s=10, zorder=5)

    # Formating
    plt.title('Linear regression')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()