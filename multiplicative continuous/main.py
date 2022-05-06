import math

import numpy as np
import random
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def exp(x,a,T):
    return a*np.exp(-x/T)


time = 5000
#people = 3000
initmoney = 10
gamma=0.1

alpha=0.05
maxrich=250
growth=0.02
graphs=5


#Initializing accounts
#accounts=initmoney*np.ones(people)
pop=np.zeros(maxrich)
newpop=np.zeros(maxrich)
pop[initmoney]=1
print(pop)

for t in range(time+1):
    for i in range(maxrich-1):
        if(i!=0 and i<math.floor(gamma*maxrich)):
            #newpop[i]=pop[i]+alpha*(pop[i+1]+pop[i-1]-2*pop[i])+alpha*pop[0]*(pop[i]-pop[i-1])+
            li=0
            for j in range (i):
                li+= pop[i]*pop[math.floor((i-j)/gamma)]
            ri=pop[math.floor(i/(1-gamma))]
            newpop[i]=pop[i]+alpha*(-2*pop[i]+ri+li)
        else:
            if(i==0):
                newpop[i] = pop[i] + alpha * (- pop[i] + pop[1] )
            else:
                li = 0
                for j in range(i):
                    li += pop[i] * pop[math.floor((i - j) / gamma)]
                newpop[i] = pop[i] + alpha * (-2 * pop[i]  + li)
    for i in range(maxrich):
        pop[i]=newpop[i]





    if((graphs*t)%time==0):
        # FITTING
        initguess = [0.1, 10]
        x = np.arange(0, maxrich)

        popt, pcov = curve_fit(exp, x, pop, initguess)
        print(popt)
        print(pcov)
        #print(pop)
        print(np.sum(pop))

        # PRINTING RESULTS
        plt.subplot(1, 2, 1)
        plt.plot(x, pop)
        plt.plot(x,exp(x,*popt))


        plt.subplot(1,2,2)
        plt.semilogy(x, pop)
        plt.semilogy(x, exp(x, *popt))

        plt.show()









    #idx = np.argsort(accounts)
    #richaxis = accounts[idx]
    #print(np.unique(richaxis))




