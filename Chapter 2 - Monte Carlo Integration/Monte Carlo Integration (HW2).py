# Homework 1 - MATH3001
# Writing a program to estimate the integral of cos^2(x) between
# 0 and 2 all divided by 2.

# Let's use Monte Carlo Integration:

# Import Relevant Modules
from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0  # Integral begins at 0
b = 2  # Integral ends at 2
N = 1000  # We will iterate N times for better accuracy
xrand = random.uniform(a, b, N)  # Creates random numbers

# Define our cos^2(x) function:
def function(x):
    return (np.cos(x))**2

# Calculate the Monte Carlo Integration
integral = 0
for i in range(N):
    integral += function(xrand[i])
answer = (b-a)/float(N)*integral  # By definition, this is our answer
print("Integral is:", 0.5*answer)  # Print the given Monte Carlo Integral Estimation
# Multiplying answer by 0.5 because we are asked for half of the integral
# We will get a new value for 'answer' every time you run - something to factor in

# We will do this N times and plot the results:
# This will create a list of N=1000 Monte Carlo Integral estimates
estimations = []
for i in range(N):
    xrand = random.uniform(a,b,N)
    integral = 0
    for i in range(N):
        integral += function(xrand[i])
    answer = (b - a) / float(N) * integral
    estimations.append(0.5*answer)

list1 = []
from statistics import mean
for i in range(N):
    average = mean(estimations[0:i+1])
    list1.append(average)

def montecarlo(f,a,b,N):
    return list1[N-1]

# Actual answer is 0.405399688086509
correct_answer = 0.405399688086509

# plt.figure()
# y = list1
# x = list(range(N))
# plt.ylim(correct_answer - 0.05,correct_answer + 0.05)
# plt.scatter(x,y, s = 0.5, c = "black",label="Average Monte Carlo Estimations")
# y1 = [0.405399688086509]*N
# plt.plot(x,y1,c = "red", label = "Exact Integral")
# plt.title('Monte Carlo Integration for Given Integral')
# plt.xlabel('Number of Samples')
# plt.ylabel('Estimation of Integral')
# plt.legend()
# plt.show()

# We now compare against other methods:

# Define Trapezium Rule:
def trapezoid(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a) / 2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

# Simpsons Rule:
def simps(function,a,b,N):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = function(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S
# print(0.5*simps(function,0,2,N))
# print(0.5*trapezoid(function,0,2,N))
# print(montecarlo(function,0,2,N))

# Setting variables equal to the estimates of the integral which we can plot
trapezium = 0.5*trapezoid(function, 0, 2, N)
simpson = 0.5*simps(function, 0, 2, N)
correct_answer = 0.405399688086509

# Plot Monte Carlo vs Simpsons vs Trapezium Rule
plt.figure()
y = list1
x = list(range(N))
plt.ylim(correct_answer - 0.05,correct_answer + 0.05)
plt.scatter(x,y, s = 0.5, c = "black",label="Average Monte Carlo Estimations (%s samples)"%N)
y1 = [correct_answer]*N
plt.plot(x,y1,c = "red", label = "Exact Integral")
y2 = [trapezium]*N
plt.plot(x,y2,c = "green", label = "Trapezium Integral (%s iterations)"%N)
y3 = [simpson]*N
plt.plot(x,y3,c = "blue", label = "Simpsons Integral (%s iterations)"%N)
plt.title('Monte Carlo Integration for Given Integral')
plt.xlabel('Number of Samples')
plt.ylabel('Estimation of Integral')
plt.legend()
plt.show()
