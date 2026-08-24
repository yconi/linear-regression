import data
import model

linear_data = data.negative_linear_data

model.firstFunction(linear_data)
avgError = model.findAvgError(linear_data)
print(avgError)

model.fit(linear_data)

error = model.findError(linear_data)
avgError = model.findAvgError(linear_data)
print(avgError)