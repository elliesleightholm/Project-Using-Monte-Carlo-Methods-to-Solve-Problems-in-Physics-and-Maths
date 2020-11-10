# this imports the math module, which contains useful maths functions but isn't required for this code
# import math
# this imports the random number generation functions - vital for this project!
import random
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import time
start = time.time()

# any variables defined here will be "global"
# (i.e. can be accessed or changed in a function)

NTIMES = 10000

# Define our lambda
lambda_value = 1

# Define percentage error
p = 0.015  # percent error

# set up binning for generating a graph
BINMAX = 10.0
BINMIN = -10.0
NBINS = 100

BINSTEP = (BINMAX - BINMIN) / NBINS
BINMID = []
BINLEFT = []
for i in range(NBINS):
    BINMID.append(BINMIN + (i + 0.5) * BINSTEP)
    BINLEFT.append(BINMIN + i * BINSTEP)

# set up bins: this creates a "list" with NBINS entries, each being zero
COUNT = [0 for j in range(NBINS)]


# this is the main program
def main():
    # for iloop in range(50):
    # initialisation of variables for calculating mean and variance
    sumx = 0.0
    sumxsq = 0.0

    # main loop
    for i in range(NTIMES):  # this will loop NTIMES
        # obtain a random number from one of the built-in functions
        # you could try different distributions here!
        x = random.expovariate(lambda_value)
        # add number, and number squared to the sums
        sumx += x
        sumxsq += x ** 2
        # work out which "bin" the random number is in and add to bin
        ibin = int((x - BINMIN) / BINSTEP)
        # check that the bin number is in the right range
        if ibin >= 0 and ibin < NBINS:
            COUNT[ibin] += 1

    # calculate mean and variance of the sample
    mean = sumx / NTIMES
    variance = sumxsq / NTIMES - mean ** 2

    # write out mean and variance
    # print('We sampled ' + str(NTIMES) + ' random numbers')
    # print('The mean was ' + str(mean))
    # print('The variance was ' + str(variance))
    # print('A binned distribution is found in binresults.txt')
    # print('The standard error of the mean is', sqrt(variance / NTIMES))

    # open a file for output
    fout = open('binresults.txt', 'w')

    # normalise bins and output
    for ibin in range(NBINS):
        COUNT[ibin] = COUNT[ibin] / BINSTEP / NTIMES
        fout.write(str(BINMID[ibin]) + ' ' + str(COUNT[ibin]) + '\n')

    # fout.close


# here we define additional functions which we might use in the program

def cplot():
    plt.bar(BINLEFT, COUNT, width=BINSTEP, color='g')
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Sampling from a uniform distribution')

    plt.show()

# here we run the main function
main()

# EXPONENTIAL DISTRIBUTION
list1 = []
list2 = []
nvalues = list(range(1, NTIMES+1))
for NTIMES in nvalues:
    sumx = 0.0
    sumxsq = 0.0

    # main loop
    for i in range(NTIMES):  # this will loop NTIMES
        # obtain a random number from one of the built-in functions
        # you could try different distributions here!
        x = random.expovariate(lambda_value)
        # add number, and number squared to the sums
        sumx += x
        sumxsq += x ** 2
        # work out which "bin" the random number is in and add to bin
        ibin = int((x - BINMIN) / BINSTEP)
        # check that the bin number is in the right range
        if ibin >= 0 and ibin < NBINS:
            COUNT[ibin] += 1

    # calculate mean and variance of the sample
    mean = sumx / NTIMES
    variance = sumxsq / NTIMES - mean ** 2

    # Create a list of the standard error of the mean for each N
    list1.append(sqrt(variance / NTIMES))

    # Create a list of the calculated means for each N
    list2.append(mean)

# Plot Normal vs Exponential for Estimated Mean
plt.figure(figsize=(6, 4))
plt.plot(nvalues, list2, label="Exponential Distribution", c="blue")
plt.plot(nvalues, [1] * len(nvalues), label="Actual Mean", c="green")
plt.plot(nvalues, [1 * 1.05] * len(nvalues), label="Upper Limit for 5% Error Estimation", c="red")
plt.plot(nvalues, [1 * 0.95] * len(nvalues), label="Lower Limit for 5% Error Estimation", c="red")
plt.title("The Estimated Mean as N increases vs Actual Mean")
plt.xlabel("Sample Size, N")
plt.ylabel("Estimated Mean Value")
plt.legend()

# Time how long it takes
print('It took', time.time()-start, 'seconds.')

# plt.show()

# Finding out which values are within the percentage error
list2 = np.array(list2)
result = np.where((list2 >= lambda_value*(1-p)) & (list2 <= lambda_value*(1+p)))

# Now we create a list of all the N values for which the estimate is within the
# percentage error
arr = result[0]
arr = arr.tolist()
# print(arr)

minimum_n = []
mylist = list(range(1,10))
for element in arr:
    if element + 1 in arr\
            and element + 2 in arr\
            and element + 3 in arr\
            and element + 4 in arr\
            and element + 5 in arr\
            and element + 6 in arr\
            and element + 7 in arr\
            and element + 8 in arr\
            and element + 9 in arr\
            and element + 10 in arr\
            and element + 11 in arr\
            and element + 12 in arr\
            and element + 13 in arr\
            and element + 14 in arr\
            and element + 15 in arr\
            and element + 16 in arr\
            and element + 17 in arr\
            and element + 18 in arr\
            and element + 19 in arr\
            and element + 20 in arr\
            and element + 21 in arr\
            and element + 22 in arr\
            and element + 23 in arr\
            and element + 24 in arr\
            and element + 25 in arr\
            and element + 26 in arr\
            and element + 27 in arr\
            and element + 28 in arr\
            and element + 29 in arr\
            and element + 30 in arr\
            and element + 31 in arr\
            and element + 32 in arr\
            and element + 33 in arr\
            and element + 34 in arr\
            and element + 35 in arr\
            and element + 36 in arr\
            and element + 37 in arr\
            and element + 38 in arr\
            and element + 39 in arr\
            and element + 40 in arr\
            and element + 41 in arr\
            and element + 42 in arr\
            and element + 43 in arr\
            and element + 44 in arr\
            and element + 45 in arr\
            and element + 46 in arr\
            and element + 47 in arr\
            and element + 48 in arr\
            and element + 49 in arr \
            and element + 50 in arr:
            # and element + 51 in arr \
            # and element + 52 in arr \
            # and element + 53 in arr \
            # and element + 54 in arr \
            # and element + 55 in arr \
            # and element + 56 in arr \
            # and element + 57 in arr \
            # and element + 58 in arr \
            # and element + 59 in arr \
            # and element + 60 in arr \
            # and element + 61 in arr \
            # and element + 62 in arr \
            # and element + 63 in arr \
            # and element + 64 in arr \
            # and element + 65 in arr \
            # and element + 66 in arr \
            # and element + 67 in arr \
            # and element + 68 in arr \
            # and element + 69 in arr \
            # and element + 70 in arr \
            # and element + 71 in arr \
            # and element + 72 in arr \
            # and element + 73 in arr \
            # and element + 74 in arr \
            # and element + 75 in arr\
            # and element + 76 in arr \
            # and element + 77 in arr \
            # and element + 78 in arr \
            # and element + 79 in arr \
            # and element + 80 in arr \
            # and element + 81 in arr \
            # and element + 82 in arr \
            # and element + 83 in arr \
            # and element + 84 in arr \
            # and element + 85 in arr \
            # and element + 86 in arr \
            # and element + 87 in arr \
            # and element + 88 in arr \
            # and element + 89 in arr \
            # and element + 90 in arr \
            # and element + 91 in arr \
            # and element + 92 in arr \
            # and element + 93 in arr \
            # and element + 94 in arr \
            # and element + 95 in arr \
            # and element + 96 in arr \
            # and element + 97 in arr \
            # and element + 98 in arr \
            # and element + 99 in arr \
            # and element + 100 in arr:
        minimum_n.append(element)
print(min(minimum_n))
