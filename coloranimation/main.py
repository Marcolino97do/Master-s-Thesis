import numpy as np
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import matplotlib
from matplotlib import cm


#DEFINE THE FIT FUNCTION
def powerexp(x,a,b,T):
    return a*(x**(b))*np.exp(-x/T)
def exp (x,a,T):
    return a*np.exp(-x/T)
def gaussian (x,a,b,T):
    return a*np.exp(-((x-b)**2)/T**2)



graphnumber=0

time = 80000000
people = 200000
initmoney = 20
accounts = initmoney * np.ones(people)
grafics=[time/50,time/20,time/10,time/4,time]
colors = matplotlib.cm.gnuplot(np.linspace(0.1,0.9,len(grafics)))
for t in range(time + 1):
    # EVOLUTE THE SYSTEM
    a = random.randint(0, people - 1)
    b = random.randint(0, people - 1)
    if(accounts[a]>0):
        exchange = 1
        accounts[b] += exchange
        accounts[a] -= exchange
    if(t in grafics):
        print(graphnumber)
        idx = np.argsort(accounts)
        richaxis = accounts[idx]
        print("\n ------")

        # CUMULANT DISTRIBUTION

        allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
        temp = np.ones(len(allrichness))
        for i in range(len(allrichness)):
            temp[i] = allrichness[i]
        h = 0
        for i in allrichness:
            count = 0
            for j in richaxis:
                # print(i,j,count)
                if (j == i):
                    count += 1
            temp[h] = count
            h += 1
        # Calculating Entropy
        entropy = 0
        if (t > 1 and t % 100 == 0):
            for i in temp:
                if (i != 0):
                    entropy -= (i / people) * np.log(i / people)

        print('fitting')
        initguess = [3000, initmoney, initmoney]
        initguess2=[1/initmoney,initmoney]
        popt, pcov = curve_fit(exp, allrichness, temp, initguess2)
        print(*popt, pcov)
        # PLOTTING
        plt.plot(allrichness, temp, linestyle='-', marker='',
                 label='accounts,t={}M, S={:.3f}'.format(t / 1000000, entropy),color=colors[graphnumber])
        #plt.plot(allrichness, exp(allrichness, *popt), linestyle='-', marker='',
                 #label='$\sigma$={:.2f}$\pm${:.2f}'.format(np.abs(popt[1]), np.abs(np.sqrt(pcov[1, 1]))))
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        plt.savefig('popol{}kt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
        # plt.show()

        """plt.semilogy(allrichness, temp,linestyle='',marker='.' ,label='accounts,t={}M, S={:.3f}'.format(t/1000000,entropy))
        plt.plot(allrichness, gaussian(allrichness, *popt), linestyle='-', marker='', label='fit')
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        plt.savefig('popol{}klogt={}.jpeg'.format(people/1000,graphnumber), dpi=600)
        plt.show() """
        graphnumber += 1
plt.xlim((0,80))
plt.show()