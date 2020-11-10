# Homework 1 - MATH3001
# Writing a program to estimate the integral of cos^2(x) between
# 0 and 2 all divided by 2.

# Let's use Monte Carlo Integration:

# Import Relevant Modules
from scipy import random
from math import cos
import numpy as np
import matplotlib.pyplot as plt

a = 0 # Integral begins at 0
b = 2 # Integral ends at 2
N = 1000 # We will iterate 1000 times for better accuracy
xrand = random.uniform(a,b,N) # Creates random numbers

# Define our cos^2(x) function:
def function(x):
    return (cos(x))**2

# Calculate the Monte Carlo Integration
integral = 0
for i in range(N):
    integral += function(xrand[i]) # Adds up each random number in xrand
answer = (b-a)/float(N)*integral # By definition, this is our answer
print("Integral is:", 0.5*answer) # Print the given Monte Carlo Integral Estimation
# Will get a new value for 'answer' every time you run

# We will do this N times and plot the results:
areas = []
for i in range(N):
    xrand = random.uniform(a,b,N)
    integral = 0
    for i in range(N):
        integral += function(xrand[i])
    answer = (b - a) / float(N) * integral
    areas.append(0.5*answer)

# Actual answer is 0.405399688086509
correct_answer = 0.405399688086509

plt.figure()
y = areas
x = list(range(N))
plt.ylim(correct_answer - 0.05,correct_answer + 0.05)
plt.scatter(x,y, s = 0.5, c = "black",label="Monte Carlo Estimations")
y1 = [0.405399688086509]*N
plt.plot(x,y1,c = "red", label = "Exact Integral")
plt.title('Monte Carlo Integration for Given Integral')
plt.xlabel('Number of Samples')
plt.ylabel('Estimation of Integral')
plt.legend()
plt.show()

# We now compare against methods like the Trapezium Rule:

# Define Trapezium Rule:
def trapezoid(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

# Print for our given function, limits and number of iterations
print(0.5*trapezoid(function, 0, 2, 1000))
# This produces 0.40539981422029153

# Calculating the mean value of 1000 estimates of Monte Carlo
from statistics import mean
print(mean(areas))
