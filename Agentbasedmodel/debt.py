import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math

import command
import gini

def exp (x,a,T):
    return a*np.exp(-x/T)



def graph():
    graphnumber=0
    debt=5
    time = 600000
    people = 1000
    initmoney = 5
    accounts = initmoney * np.ones(people)
    counter=0
    for t in range(time+1):

        a = random.randint(0, people - 1)
        b = random.randint(0, people - 1)
        if (accounts[a]>0):
            exchange=1
            #exchange=math.floor(gamma*accounts[a]+(gamma/capratio)*initmoney)
            #exchange=random.randint(0, math.floor(gamma*accounts[a]))
            #exchange = random.randint(0, math.floor(gamma * accounts[a]))+ alpha
            #exchange=math.floor(gamma*accounts[a])
            accounts[b] += exchange
            accounts[a] -= exchange

        if (t%(time)==0 and t>1):
            idx = np.argsort(accounts)
            richaxis = accounts[idx]
            print("\n ------")
            allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
            # Find the pdf
            temp = command.pdf(richaxis)


            #Calculating Entropy
            entropy=command.entropy(temp)

            # CALCULATING GINI
            Gininodebt=gini.calculate(richaxis, initmoney, graph=1, show=0)

            #FITTING
            print('fitting')
            initguess=[3000,initmoney]
            popt, pcov = curve_fit(exp,allrichness, temp, initguess)
            print(*popt,pcov)
            """
            # PLOTTING
            plt.plot(allrichness, temp,linestyle='',marker='.' ,label='accounts,t={}M, S={:.3f}, gini={:.3f}'.format(t/1000000,entropy,Gininodebt))
            plt.plot(allrichness,exp(allrichness,*popt),linestyle='-',marker='' , label='fit T={:.2f} $\pm$ {:.2f}'.format(popt[1], np.sqrt(pcov[1][1])))
            plt.legend()
            plt.xlabel('wealth')
            plt.ylabel('population')
            plt.savefig('popol{}kt={}.jpeg'.format(people/1000,graphnumber),dpi=600)
            #plt.show()
            """

            """plt.semilogy(allrichness, temp,linestyle='',marker='.' ,label='accounts,t={}M, S={:.3f}'.format(t/1000000,entropy))
            plt.plot(allrichness, gaussian(allrichness, *popt), linestyle='-', marker='', label='fit')
            plt.legend()
            plt.xlabel('wealth')
            plt.ylabel('population')
            plt.savefig('popol{}klogt={}.jpeg'.format(people/1000,graphnumber), dpi=600)
            plt.show() """
            graphnumber+=1

    accounts = initmoney * np.ones(people)
    counter=0
    for t in range(time+1):

        a = random.randint(0, people - 1)
        b = random.randint(0, people - 1)
        if (accounts[a]>(-debt)):
            exchange=1
            #exchange=math.floor(gamma*accounts[a]+(gamma/capratio)*initmoney)
            #exchange=random.randint(0, math.floor(gamma*accounts[a]))
            #exchange = random.randint(0, math.floor(gamma * accounts[a]))+ alpha
            #exchange=math.floor(gamma*accounts[a])
            accounts[b] += exchange
            accounts[a] -= exchange

        if (t%(time)==0 and t>1):
            idx = np.argsort(accounts)
            richaxis = accounts[idx]
            allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
            print("\n ------")

            # Find the pdf
            temp = command.pdf(richaxis)

            # Calculating Entropy
            entropy = command.entropy(temp)

            # CALCULATING GINI
            Ginidebt = gini.calculate(richaxis, initmoney, graph=1, show=1)
            """
            # FITTING
            print('fitting')
            initguess = [3000, initmoney]
            popt, pcov = curve_fit(exp, allrichness, temp, initguess)
            print(*popt, pcov)

            # PLOTTING
            plt.plot(allrichness, temp, linestyle='', marker='.',
                     label='accounts,t={}M, S={:.3f}, gini={:.3f}'.format(t / 1000000, entropy, Ginidebt))
            plt.plot(allrichness, exp(allrichness, *popt), linestyle='-', marker='',
                     label='fit T={:.2f} $\pm$ {:.2f}'.format(popt[1], np.sqrt(pcov[1][1])))
            plt.legend()
            plt.xlabel('wealth')
            plt.ylabel('population')
            plt.savefig('popol{}kt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
            # plt.show()

    plt.axvline(x=0,color='grey')
    print('-----------Gini')
    print(Gininodebt,Ginidebt)
    plt.show()
    """





