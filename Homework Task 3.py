# Import Relevant Modules
from scipy import random
import matplotlib.pyplot as plt
from math import pi, sqrt

# Homework 3 - MATH3001
# Writing a program to calculating the area of the unit circle by integrating

# Let's use Monte Carlo Integration:

# Impose our boundary constrants, |x_i| < 1 and |y_i| < 1
a = -1  # Integral begins at -1
b = 1  # Integral ends at 1
N = 2000  # We will iterate N times for better accuracy
xrand = random.uniform(a, b, N)  # Creates random numbers for x_i
yrand = random.uniform(a, b, N)  # Creates random numbers for y_i

# Define our function:
def function(x,y):
    if x**2 + y**2 < 1:
        return 1
    else:
        return 0

# Calculate the Monte Carlo Integration
summation = 0
for i in range(N):
    summation += function(xrand[i], yrand[i])
answer = 4/float(N)*summation  # By definition, this is the integral
print("Integral is:", answer)  # Print the given Monte Carlo Integral Estimation

# Plot the estimates vs the actual integral
# This will create a list of N Monte Carlo Integral estimates
estimations = []
for i in range(N):
    xrand = random.uniform(a, b, N)  # Creates random numbers for x_i
    yrand = random.uniform(a, b, N)  # Creates random numbers for y_i
    summation = 0
    for i in range(N):
        summation += function(xrand[i], yrand[i])
    integral = 4 / float(N) * summation
    estimations.append(integral)
# print(estimations)

list1 = []
from statistics import mean
for i in range(N):
    average = mean(estimations[0:i+1])
    list1.append(average)

nvalues = list(range(1, N+1))
plt.figure()
plt.plot(nvalues, list1, label="Integral Estimations", c="blue")
plt.plot(nvalues, [pi] * len(nvalues), label="Actual Integral", c="red")
plt.title("The Estimated Integral as N increases vs Actual Integral")
plt.xlabel("Sample Size, N")
plt.ylabel("Estimated Integral Value")
plt.legend()
plt.xlim(0)
# plt.show()

# How the error changes with N
# By definition, we have that the standard error when using monte carlo methods is,
# sqrt((<f^2> - <f>^2)/N)
# So let's write some code to compute this standard error

# This will create a list of N Monte Carlo Integral estimate errors
list2 = []
list3 = []
for j in range(1, N+1):
    summation = 0
    summation1 = 0
    xrand = random.uniform(a, b, j)  # Creates random numbers for x_i
    yrand = random.uniform(a, b, j)  # Creates random numbers for y_i
    for i in range(j):
        summation += function(xrand[i], yrand[i])  # Definition of <f>
        summation1 += (function(xrand[i], yrand[i]))**2  # Definition of <f^2>
    f = summation/float(j)
    f_squared = summation1/float(j)
    standard_error = 4*sqrt((f_squared - f**2)/j)
    list2.append(standard_error)
    list3.append((j**-0.5))
# print(list2)

# Calculate the variance
variance = []
for j in range(1, N+1):
    summation = 0
    summation1 = 0
    xrand = random.uniform(a, b, j)  # Creates random numbers for x_i
    yrand = random.uniform(a, b, j)  # Creates random numbers for y_i
    for i in range(j):
        summation += function(xrand[i], yrand[i])  # Definition of <f>
        summation1 += (function(xrand[i], yrand[i]))**2  # Definition of <f^2>
    f = summation/float(j)
    f_squared = summation1/float(j)
    standard_variance = (f_squared - f**2)
    variance.append(standard_variance)

# Plots how the error changes with N
plt.figure()
plt.plot(nvalues, list2, label="Estimation Errors", c="blue")
plt.plot(nvalues, list3, label="N^-0.5", c="orange")
plt.plot(nvalues, [0] * len(nvalues), label="No Error", c="red")
plt.title("How the Error Changes with N")
plt.xlabel("Sample Size, N")
plt.ylabel("Error")
plt.legend()
plt.xlim(10)
plt.ylim(-0.05, list2[10]+0.05)
plt.show()

# Plots the variance versus the error estimator
plt.figure()
plt.plot(nvalues, list2, label="Estimation Errors", c="blue")
plt.plot(nvalues, variance, label="Variance", c="green")
plt.title("How the Error Changes with N")
plt.xlabel("Sample Size, N")
plt.ylabel("Error")
plt.legend()
plt.xlim(10)
plt.show()

# print(mean(variance))