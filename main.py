import data
import model
import visualizer

linear_data = data.quadratic_data

model.firstFunction(linear_data)

model.fit(linear_data)

visualizer.plot(
    linear_data,
    model.history_m,
    model.history_b,
    model.history_error
)