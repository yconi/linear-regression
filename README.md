
# Linear Regression
The linear regression is a model that estimates the relashionship between a  independent variable and a dependent variable.
## Main objective
Understanding the basic of regression models. In this moment, the objective is not to build the best model ever, but to learn more about basic statistics models.

## model.py
At this moment, the model receives an array with some ordered pair as the data for training.
``` py
exampleData = [0, 4.3], [1, 7.4], [2, 8.3], [3, 10.7], [4, 13.1]
```
After choosing the desired array, the model finds the slope $m$ and the intersection $b$ to create the first basic function.

$$
m=\frac{ΔY}{ΔX}
$$

$$
b=y1[n] -mx[n]
$$

Or:

``` py
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

```
