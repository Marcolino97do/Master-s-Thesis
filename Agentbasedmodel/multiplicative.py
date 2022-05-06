import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math

import gini
#import evolution.c

def run(time=1000000, people=100000, initmoney=20):

    debt=10
    accounts = initmoney * np.ones(people)
    counter=0
    for t in range(time+1):

        a = random.randint(0, people - 1)
        b = random.randint(0, people - 1)
        if (accounts[a] >= 0):
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

            # CUMULANT DISTRIBUTION

            allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
            print(allrichness)
            temp = np.zeros(len(allrichness))
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

            # CALCULATING GINI
            cumrich=np.zeros(len(richaxis))
            for i in range(len(richaxis)):
                cumrich[i]=cumrich[i-1]+richaxis[i]
            normcumrich=cumrich/(initmoney*people)
            print(normcumrich)
            ginicurve=np.zeros(len(richaxis))
            ginicurve[0]=normcumrich[0]
            for i in range(1,len(richaxis)):
                ginicurve[i]=normcumrich[i]+ginicurve[i-1]
            Gini=0.5-np.sum(normcumrich)/people
            print('GINI----------')
            print(Gini)

            Gini=gini.calculate(richaxis, initmoney)
            print(Gini)




            """cumrich = np.zeros(len(allrichness))
            print(cumrich[-1])
            for i in range(len(allrichness)):
                cumrich[i] = cumrich[i - 1] + allrichness[i] * temp[i]
            normalcumrich = cumrich / (initmoney * people)
            print(normalcumrich)
            ginicurve=np.zeros(len(normalcumrich))
            for i in range(len(temp)):
                ginicurve[i]=ginicurve[i-1]+normalcumrich[i]
            gini = 0.5 - np.sum(normalcumrich) / len(allrichness)
            print(len(allrichness))
            print('GINI---------------')
            print(gini)"""

            # PLOTTING
            x=np.arange(len(richaxis))
            plt.plot(x/people,normcumrich,label='no debt')
            plt.plot(x/people,x/people)
            plt.xlabel('cumulative share of people')
            plt.ylabel('cumulative wealth')
            plt.legend()
            #plt.plot(richaxis,ginicurve)

    accounts = initmoney * np.ones(people)
    counter = 0
    for t in range(time + 1):

        a = random.randint(0, people - 1)
        b = random.randint(0, people - 1)
        if (accounts[a] >= -debt):
            exchange = 1
            # exchange=math.floor(gamma*accounts[a]+(gamma/capratio)*initmoney)
            # exchange=random.randint(0, math.floor(gamma*accounts[a]))
            # exchange = random.randint(0, math.floor(gamma * accounts[a]))+ alpha
            # exchange=math.floor(gamma*accounts[a])
            accounts[b] += exchange
            accounts[a] -= exchange

        if (t % (time) == 0 and t > 1):
            idx = np.argsort(accounts)
            richaxis = accounts[idx]
            print("\n ------")

            # CUMULANT DISTRIBUTION

            allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
            print(allrichness)
            temp = np.zeros(len(allrichness))
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

            # CALCULATING GINI
            cumrich = np.zeros(len(richaxis))
            for i in range(len(richaxis)):
                cumrich[i] = cumrich[i - 1] + richaxis[i]
            normcumrich = cumrich / (initmoney * people)
            print(normcumrich)
            ginicurve = np.zeros(len(richaxis))
            ginicurve[0] = normcumrich[0]
            for i in range(1, len(richaxis)):
                ginicurve[i] = normcumrich[i] + ginicurve[i - 1]
            Gini = 0.5 - np.sum(normcumrich) / people
            print('GINI----------')
            print(Gini)

            Gini = gini.calculate(richaxis, initmoney)
            print(Gini)

            """cumrich = np.zeros(len(allrichness))
            print(cumrich[-1])
            for i in range(len(allrichness)):
                cumrich[i] = cumrich[i - 1] + allrichness[i] * temp[i]
            normalcumrich = cumrich / (initmoney * people)
            print(normalcumrich)
            ginicurve=np.zeros(len(normalcumrich))
            for i in range(len(temp)):
                ginicurve[i]=ginicurve[i-1]+normalcumrich[i]
            gini = 0.5 - np.sum(normalcumrich) / len(allrichness)
            print(len(allrichness))
            print('GINI---------------')
            print(gini)"""

            # PLOTTING
            x = np.arange(len(richaxis))
            plt.plot(x / people, normcumrich, label='no debt')
            plt.plot(x / people, x / people)
            plt.xlabel('cumulative share of people')
            plt.ylabel('cumulative wealth')
            plt.legend()
            # plt.plot(richaxis,ginicurve)


    plt.show()






