import numpy as np
import numpy.ma as ma
import random
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


#DEFINE THE FIT FUNCTION
def exponential(x,a,b,c):
    return b-a*np.exp(-x/c)

def powerlaw(x,a,b,c,d):
    return b-(((x+d)/a)**c)

def invlog(x,a,b,c):
    return b-a*(1/c+np.log(x))


time=100000
people=4000
initmoney=10

points=1000

accounts=initmoney*np.ones(people)
quarters=int(time/points)
entropy=np.zeros(quarters)
scounter=0
entropy[0]=0
for t in range(time):
    a = random.randint(0, people - 1)
    b = random.randint(0, people - 1)
    if (accounts[a] >= -initmoney/3):
        accounts[a] -= 1
        accounts[b] += 1
    #Calculate Entropy

    if (t%points==0 and t>1):
        scounter+=1
        idx = np.argsort(accounts)
        richaxis = accounts[idx]
        allrichness = np.arange(np.min(richaxis), np.max(richaxis))
        pop=np.ones(len(allrichness))


        h=0
        for i in allrichness:
            count=0
            for j in richaxis:
                if(j==i):
                    count+=1
            pop[h]=count
            h+=1
        print(scounter)
        for i in range (1,len(pop)):
            if(pop[i]!=0):
                entropy[scounter]-=((pop[i]/people)*np.log(pop[i]/people))

#plotting the entropy
x=np.arange(0,quarters)

mx = ma.masked_outside(x,20,20)
initguess=[3,3,20]
initguess2=[1,3,-2,0.3]
initguess3=[1,3,0]
#FITS
popt,pcov=curve_fit(exponential,mx,entropy,initguess)
#popt2,pcov2=curve_fit(powerlaw,mx,entropy,initguess2)
#popt3,pcov3=curve_fit(invlog,x,entropy,initguess3)
#print(*popt)
#print(*popt2)
#print(*popt3)
plt.plot(x,entropy,linestyle='', marker='.',label='data')
#plt.plot(x, exponential(x, *popt), 'r', label='exp')
#plt.plot(x, powerlaw(x, *popt2), 'y', label='pow: exp={:.1f}'.format(popt2[2]))

#plt.plot(x, invlog(x, *popt3), 'g', label='invlog')


#plt.title('entropy vs time')
plt.xlabel('time')
plt.ylabel('entropy')
plt.legend()
#plt.xlim(3,)
#plt.ylim(2.5,)
plt.show()

res=entropy-powerlaw(x, *popt)
res[0]=0
plt.plot(x,res)
plt.xlabel('time')
plt.ylabel('res')
#plt.show()

plt.semilogy(x,-entropy+np.ones(len(entropy))*popt[1])
#plt.show()
plt.loglog(x,-entropy+np.ones(len(entropy))*popt[1])
#plt.show()
print(mx)




