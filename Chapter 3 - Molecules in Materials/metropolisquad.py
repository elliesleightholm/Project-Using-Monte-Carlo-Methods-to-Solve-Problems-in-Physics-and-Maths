# this imports the math module, which contains useful maths functions
import math
# this imports the random number generation functions - vital for this project!
import random
from math import sqrt
import matplotlib.pyplot as plt

# any variables defined here will be "global"
#(i.e. can be accessed or changed in a function)
SPRINGCONST = 10000000
KT = 1
XSTEP = 0.00001

NTIMES = 10000

# set up binning for generating a graph
BINMAX = 5.0
BINMIN = -5.0
NBINS = 20

BINSTEP = (BINMAX - BINMIN) / NBINS
BINMID= []
for i in range(NBINS):
    BINMID.append(BINMIN + (i + 0.5) * BINSTEP)

# Create an empty list to add position of particles in
positions_of_particle = []
positions_of_particle_squared = []
# this is the main program
def main():
    # initial position and energy of the particle
    x=4.1
    enold=u_pot(x)
    ennew=enold

    # set up bins
    count = [0 for j in range(NBINS)]

    # main loop
    for i in range(NTIMES):
        # randomly choose a new position and calculate energy change
        xnew = x + XSTEP * random.uniform(-1.0,1.0)
        ennew = u_pot(xnew)
        edif = ennew - enold
        # apply the metropolis criterion
        if edif < 0:
            # energy decreased, accept new position
            x = xnew
            enold = ennew
        else:
            # energy increased, accept new position conditionally
            prob = math.exp(-edif/KT)
            rnum = random.random()
            if rnum < prob:
                x = xnew
                enold = ennew
        # Append all x values to a list
        positions_of_particle.append(x)
        positions_of_particle_squared.append(x**2)
        # work out which "bin" current position is in and add to bin
        ibin = int((x - BINMIN)/BINSTEP)
        if ibin>=0 and ibin<NBINS:
            count[ibin] += 1

    # open a file for output
    fout = open ('results.txt','w')
    
    # normalise bins and output
    for ibin in range(NBINS):
        count[ibin] = count[ibin]/BINSTEP/NTIMES
        fout.write(str(BINMID[ibin])+' '+str(count[ibin])+'\n')
        print(str(BINMID[ibin]-0.5*BINSTEP)+' to ' 
              +str(BINMID[ibin]+0.5*BINSTEP)+'      '+str(count[ibin]))

    print ('done')
    fout.close



# here we define additional functions which we might use in the program

# this function defines a simple quadratic potential
def u_pot(x):
  pot = SPRINGCONST* x**2 / 2.0
  return pot

# here we run the main function
main()

#print(positions_of_particle)

# Average particle position
average_position_of_particle = (sum(positions_of_particle)/NTIMES)
print(average_position_of_particle)
print(positions_of_particle)

# Variance
#variance = (sum(positions_of_particle_squared)/NTIMES) - ((sum(positions_of_particle)/NTIMES))**2
#print(sqrt(variance))

plt.figure()
plt.plot(list(range(1, NTIMES + 1)), positions_of_particle, label="Particle Positions", c="blue", linewidth=1)
#plt.plot(list(range(1, NTIMES + 1)), [average_position_of_particle]*NTIMES, label="Average Particle Position", c="orange")
plt.title("Particle Positions for Different N (N = %s, Step = %s)" %(NTIMES,float(XSTEP)))
plt.xlabel("Number of Steps")
plt.ylabel("Position")
plt.legend()
plt.ylim(0,10)
plt.show()

# Setting up the code to calculate the average particle position and variance
# for increasing N.

# Main code
#
# x = 4.1
# enold = u_pot(x)
# ennew = enold
# average_position = []
# variance = []
# for j in range(1, NTIMES+1):
#     for i in range(1, NTIMES+1):
#         # randomly choose a new position and calculate energy change
#         xnew = x + XSTEP * random.uniform(-1.0, 1.0)
#         ennew = u_pot(xnew)
#         edif = ennew - enold
#         # apply the metropolis criterion
#         if edif < 0:
#             # energy decreased, accept new position
#             x = xnew
#             enold = ennew
#         else:
#             # energy increased, accept new position conditionally
#             prob = math.exp(-edif / KT)
#             rnum = random.random()
#             if rnum < prob:
#                 x = xnew
#                 enold = ennew
#         # Append all x values to a list
#         positions_of_particle.append(x)
#         positions_of_particle_squared.append(x**2)
#     average_position.append((sum(positions_of_particle)/j))
#     variance.append((sum(positions_of_particle_squared)/j) - ((sum(positions_of_particle))/j)**2)
#
# print(average_position)

# plt.figure()
# plt.plot(list(range(1, NTIMES + 1)), average_position, label=" Average Particle Positions", c="blue", linewidth=0.5)
# #plt.plot(list(range(1, NTIMES + 1)), variance, label="Average Variance", c="purple", linewidth=0.5)
# plt.title("Average Particle Positions for Increasing N (N = %s, Step = %s)" %(NTIMES,float(XSTEP)))
# plt.xlabel("Number of Steps")
# plt.ylabel("Average Position")
# plt.legend()
# #plt.xlim(20)
# #plt.ylim(-10)
# #plt.show()