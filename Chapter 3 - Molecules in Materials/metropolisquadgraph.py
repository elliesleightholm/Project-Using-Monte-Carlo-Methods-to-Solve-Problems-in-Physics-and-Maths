# this imports the math module, which contains useful maths functions
import math
# this imports the random number generation functions - vital for this project!
import random
import matplotlib.pyplot as plt

# any variables defined here will be "global"
#(i.e. can be accessed or changed in a function)
SPRINGCONST = 1
KT=1.0
XSTEP = 1

NTIMES = 10000

# set up binning for generating a graph
BINMAX = 5.0
BINMIN = -5.0
NBINS = 100

BINSTEP = (BINMAX - BINMIN) / NBINS
BINMID= []
BINLEFT=[]
for i in range(NBINS):
    BINMID.append(BINMIN + (i + 0.5) * BINSTEP)
    BINLEFT.append(BINMIN + i * BINSTEP)

    # set up bins: this creates a "list" with NBINS entries, each being zero
COUNT = [0 for j in range(NBINS)]

# this is the main program
positions_of_particle = []
def main():
    # initial position and energy of the particle
    x=0.0
    enold=u_pot(x)
    ennew=enold

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
        # work out which "bin" current position is in and add to bin
        positions_of_particle.append(x)
        ibin = int((x - BINMIN)/BINSTEP)
        if ibin>=0 and ibin<NBINS:
            COUNT[ibin] += 1

    # open a file for output
    fout = open ('results.txt','w')
    
    # normalise bins and output
    for ibin in range(NBINS):
        COUNT[ibin] = COUNT[ibin]/BINSTEP/NTIMES
        fout.write(str(BINMID[ibin])+' '+str(COUNT[ibin])+'\n')
 #       print(str(BINMID[ibin]-0.5*BINSTEP)+' to ' 
 #             +str(BINMID[ibin]+0.5*BINSTEP)+'      '+str(COUNT[ibin]))
    fout.close

    
# here we define additional functions which we might use in the program

# this function defines a simple quadratic potential
def u_pot(x):
  pot = SPRINGCONST* (x**2) / 2.0
  return pot


def cplot():
    #plot the sampled distribution as a histogram
    plt.bar(BINLEFT, COUNT, width=BINSTEP, color='b')
    plt.xlabel('x',fontsize=18)
    plt.ylabel('Probability',fontsize=18)
    plt.suptitle('Metropolis Monte Carlo sampling, quadratic potential',fontsize=18)
    plt.title('N = %s and Step %s'%(NTIMES,XSTEP))
    # plot the expected distribution as a line
    ydat=[]
    norm=math.sqrt(2*math.pi/SPRINGCONST)
    for i in range(NBINS):
        ydat.append(math.exp(-u_pot(BINMID[i]))/norm)
    plt.plot(BINMID,ydat,'-',color='black',linewidth=3)
    
    plt.show()


# here we run the main function
main()
cplot()
print(positions_of_particle)
