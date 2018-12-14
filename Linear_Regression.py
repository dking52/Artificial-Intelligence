#Calculate linear regression best fit line
#Calculate dependent given independent variable

from statistics import mean
import numpy as my_nump

#Given data points for evaluation
xPts = my_nump.array([1,2,1,4,5,6,4,8,10,10], dtype=my_nump.float64)
yPts = my_nump.array([2,4,6,8,2,12,14,4,18,12], dtype=my_nump.float64)

#Calculate slope and y-intercept from given points
def fitting_Line(xPts,yPts):
    slope = (((mean(xPts) * mean(yPts)) - mean(xPts * yPts)) / ((mean(xPts) * mean(xPts)) - mean(xPts * xPts)))  
    y_Intercept = mean(yPts) - slope*mean(xPts)
    
    return slope, y_Intercept

#Feed points to calculation function and return slope and y-intercept
slope, y_Intercept = fitting_Line(xPts,yPts)

#Print regression equation: y = a + bX
print("Linear Regression: " + "y = " + str(round(slope,3)) + "x + " + str(round(y_Intercept,3)))