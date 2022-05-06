import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math

#DEFINE THE FIT FUNCTION
def powerexp(x,a,b,T):
    return a*(x**(b))*np.exp(-x/T)
def exp (x,a,T):
    return a*np.exp(-x/T)
def gaussian (x,a,b,T):
    return a*np.exp(-((x-b)**2)/T**2)
def squareroot (x,a):
    return a*np.abs(np.sqrt(x))



time = 300000
people = 5000
initmoney = 20
accounts = initmoney * np.ones(people)
counter=-1
points=30


sigma=np.zeros(points)
Dsigma=np.zeros(points)
for t in range(time+1):

    a = random.randint(0, people - 1)
    b = random.randint(0, people - 1)
    if (True):
        exchange=1
        #exchange=math.floor(gamma*accounts[a]+(gamma/capratio)*initmoney)
        #exchange=random.randint(0, math.floor(gamma*accounts[a]))
        #exchange = random.randint(0, math.floor(gamma * accounts[a]))+ alpha
        #exchange=math.floor(gamma*accounts[a])
        accounts[b] += exchange
        accounts[a] -= exchange

    if (t%(time/points)==0 and t>1):
        counter=counter+1
        idx = np.argsort(accounts)
        richaxis = accounts[idx]


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
        #Calculating Entropy
        entropy=0
        if(t>1 and t%100==0):
            for i in temp:
                if(i!=0):
                    entropy-=(i/people)*np.log(i/people)


        #FITTING
        print('fitting \n')
        initguess=[30,initmoney,initmoney]
        popt, pcov = curve_fit(gaussian,allrichness, temp, initguess)
        print(*popt,pcov)
        sigma[counter]=np.abs(popt[2])
        Dsigma[counter]=np.abs(np.sqrt(pcov[2][2]))
        """
        # PLOTTING
        plt.plot(allrichness, temp,linestyle='',marker='.' ,label='accounts,t={}M, S={:.3f}'.format(t/1000000,entropy))
        plt.plot(allrichness,gaussian(allrichness,*popt),linestyle='-',marker='' , label='$\sigma$={:.2f}$\pm${:.2f}'.format(np.abs(popt[2]),np.abs(np.sqrt(pcov[2,2]))))
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        plt.savefig('popol{}kt={}.jpeg'.format(people/1000,graphnumber),dpi=600)
        #plt.show()


        plt.semilogy(allrichness, temp,linestyle='',marker='.' ,label='accounts,t={}M, S={:.3f}'.format(t/1000000,entropy))
        plt.plot(allrichness, gaussian(allrichness, *popt), linestyle='-', marker='', label='fit')
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        plt.savefig('popol{}klogt={}.jpeg'.format(people/1000,graphnumber), dpi=600)
        plt.show() 
        graphnumber+=1
        """
x=np.linspace(0,points,100)
n=np.arange(0,points)
plt.errorbar(n,sigma,Dsigma,ls='none',marker='.',label="fitted sigma")
#fitting sigma
initguess=[2]
popt, pcov = curve_fit(squareroot,x, sigma, initguess)
y=popt[0]*np.abs(np.sqrt(x))
plt.plot(x,y,label='Theoretical prediction')
plt.xlabel("interactions[10k]")
plt.ylabel("sigma")
plt.legend()
plt.show()





