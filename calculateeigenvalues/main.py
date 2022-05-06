import numpy as np
from matplotlib import pyplot as plt


lenvec=500
parameter=0.1
lambdapoints=1000

Pzero=0.5 #depends on the temperature

lambdas=np.linspace(-3,-2.88,lambdapoints)
alpha=np.zeros(lenvec)
alpha[lenvec-1]=parameter


kappas=0.5*(lambdas+2-Pzero-np.sqrt((lambdas+2-Pzero)**2-4*(1-Pzero)))
print(kappas)

sum=np.zeros(len(lambdas))

numbers=np.arange(0,lenvec-2)

for index,k in enumerate(kappas):
    alpha[lenvec - 1] = parameter
    alpha[lenvec - 2] =alpha[lenvec-1]/k
    for n in numbers[::-1]:
        alpha[n]=((Pzero-2-lambdas[index])*alpha[n+1]+alpha[n+2])/(Pzero-1)
    print(alpha)


    rescalefactor=1/alpha[0]
    sum[index]=rescalefactor*np.sum(alpha)
    alpha = np.zeros(lenvec)


plt.plot(lambdas,sum)
plt.xlabel("$\lambda$")
plt.ylabel("$\sum \delta(m)$")
#plt.axvline(-1.5-np.sqrt(2),color='red',ls='--')
#plt.ylim=(-2,2)
plt.minorticks_on()
plt.show()