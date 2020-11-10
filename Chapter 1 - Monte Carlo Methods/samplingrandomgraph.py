# this imports the math module, which contains useful maths functions but isn't required for this code
# import math
# this imports the random number generation functions - vital for this project!
import random
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

# any variables defined here will be "global"
# (i.e. can be accessed or changed in a function)

NTIMES = 10000

# set up binning for generating a graph
BINMAX = 10.0
BINMIN = -10.0
NBINS = 100

BINSTEP = (BINMAX - BINMIN) / NBINS
BINMID= []
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
    sumx=0.0
    sumxsq=0.0


    # main loop
    for i in range(NTIMES):  #this will loop NTIMES
        # obtain a random number from one of the built-in functions
        # you could try different distributions here!
        x = random.normalvariate(1,4)
        # add number, and number squared to the sums
        sumx += x
        sumxsq += x**2
        # work out which "bin" the random number is in and add to bin
        ibin = int((x - BINMIN)/BINSTEP)
        #check that the bin number is in the right range
        if ibin>=0 and ibin<NBINS:  
            COUNT[ibin] += 1

    # calculate mean and variance of the sample
    mean = sumx/NTIMES
    variance = sumxsq/NTIMES - mean**2

    # write out mean and variance
    print('We sampled '+str(NTIMES)+' random numbers')
    print('The mean was '+str(mean))
    print('The variance was '+str(variance))
    print('A binned distribution is found in binresults.txt')
    print('The standard error of the mean is', sqrt(variance/NTIMES))
            
    # open a file for output
    fout = open ('binresults.txt','w')
    
    # normalise bins and output
    for ibin in range(NBINS):
        COUNT[ibin] = COUNT[ibin]/BINSTEP/NTIMES
        fout.write(str(BINMID[ibin])+' '+str(COUNT[ibin])+'\n')

    #fout.close

    
# here we define additional functions which we might use in the program

def cplot():
    plt.bar(BINLEFT, COUNT, width=BINSTEP, color='g')
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Sampling from a uniform distribution')
    
    plt.show()

# here we run the main function
main()
# generate a plot of the results
# cplot()

# NORMAL DISTRIBUTION
list1 = []
list2 = []
nvalues = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for NTIMES in nvalues:
        sumx = 0.0
        sumxsq = 0.0

        # main loop
        for i in range(NTIMES):  # this will loop NTIMES
            # obtain a random number from one of the built-in functions
            # you could try different distributions here!
            x = random.normalvariate(1, 4)
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
print(list1)

# UNIFORM
list3 = []
list4 = []
for NTIMES in nvalues:
        sumx = 0.0
        sumxsq = 0.0

        # main loop
        for i in range(NTIMES):  # this will loop NTIMES
            # obtain a random number from one of the built-in functions
            # you could try different distributions here!
            x = random.uniform(1, 4)
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
        list3.append(sqrt(variance/NTIMES))

        # Create a list of the calculated means for each N
        list4.append(mean)
# print(list3)

# TRIANGULAR
list5 = []
list6 = []
for NTIMES in nvalues:
        sumx = 0.0
        sumxsq = 0.0

        # main loop
        for i in range(NTIMES):  # this will loop NTIMES
            # obtain a random number from one of the built-in functions
            # you could try different distributions here!
            x = random.triangular(1, 4)
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
        list5.append(sqrt(variance / NTIMES))

        # Create a list of the calculated means for each N
        list6.append(mean)
# print(list5)

# EXPONENTIAL
list7 = []
list8 = []
for NTIMES in nvalues:
        sumx = 0.0
        sumxsq = 0.0

        # main loop
        for i in range(NTIMES):  # this will loop NTIMES
            # obtain a random number from one of the built-in functions
            # you could try different distributions here!
            x = random.expovariate(1)
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
        list7.append(sqrt(variance/NTIMES))

        # Create a list of the calculated means for each N
        list8.append(mean)
# print(list7)

# Plotting the standard error of the mean vs N
plt.figure()
plt.plot(nvalues, list1, label="Normal Distribution")
plt.plot(nvalues, list3, label="Uniform Distribution")
plt.plot(nvalues, list5, label = "Triangular Distribution")
plt.plot(nvalues, list7, label = "Exponential Distribution")
plt.xticks(nvalues)
plt.title("The Standard Error of the Mean vs Sample Size ($N$) for Different Distributions")
plt.xlabel("Sample Size, N")
plt.ylabel("Standard Error of the Mean")
plt.legend()
plt.show()

# Plot Normal vs Exponential for Estimated Mean
plt.figure(figsize=(6,4))
plt.plot(nvalues, list2, label="Normal Distribution", c="blue")
plt.plot(nvalues, list8, label="Exponential Distribution", c="orange")
plt.plot(nvalues, [1]*len(nvalues), label="Actual Mean", c="green")
plt.plot(nvalues, [1*1.05]*len(nvalues), label="Upper Limit for 5% Error Estimation", c="red")
plt.plot(nvalues, [1*0.95]*len(nvalues), label="Lower Limit for 5% Error Estimation", c="red")
plt.xticks(nvalues)
plt.title("The Estimated Mean as N increases vs Actual Mean")
plt.xlabel("Sample Size, N")
plt.ylabel("Estimated Mean Value")
plt.legend()
plt.show()

# NORMAL DISTRIBUTION
list1 = []
list2 = []
nvalues = list(range(1,101))
for NTIMES in nvalues:
        sumx = 0.0
        sumxsq = 0.0

        # main loop
        for i in range(NTIMES):  # this will loop NTIMES
            # obtain a random number from one of the built-in functions
            # you could try different distributions here!
            x = random.normalvariate(1, 4)
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
plt.figure(figsize=(6,4))
plt.plot(nvalues, list2, label="Normal Distribution", c="blue")
# plt.plot(nvalues, list8, label="Exponential Distribution", c="orange")
plt.plot(nvalues, [1]*len(nvalues), label="Actual Mean", c="green")
plt.plot(nvalues, [1*1.05]*len(nvalues), label="Upper Limit for 5% Error Estimation", c="red")
plt.plot(nvalues, [1*0.95]*len(nvalues), label="Lower Limit for 5% Error Estimation", c="red")
plt.title("The Estimated Mean as N increases vs Actual Mean")
plt.xlabel("Sample Size, N")
plt.ylabel("Estimated Mean Value")
plt.legend()
plt.show()
