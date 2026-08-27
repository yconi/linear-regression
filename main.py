import numpy as np
import data
import model
import visualizer

# Data selection, choose one of negative_linear_data, linear_data or quadratic_data
linear_data = data.generator(15)

# Initial function
model.firstFunction(linear_data)

# Model fit for reducing the error
model.fit(linear_data)

error = model.findError(linear_data)
avgError = model.findAvgError(linear_data)

# Model evalution for graph

x = np.arange(50)
y = [model.iteration(i) for i in x]

visualizer.plot(np.array(linear_data), [x, y])