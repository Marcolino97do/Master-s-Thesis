import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math

def calculate(richaxis, initmoney=20, graph=0,show=0):
    if(graph==0):
        people=len(richaxis)
        cumrich = np.zeros(people)
        totmoney = np.sum(richaxis)
        for i in range(len(richaxis)):
            cumrich[i] = cumrich[i - 1] + richaxis[i]
        normcumrich = (cumrich+0.5) / totmoney
        print(normcumrich)
        gini = 1 - 2*np.sum(normcumrich) / people
        return gini


    if(graph==1 and show==0):
        people = len(richaxis)
        cumrich = np.zeros(people)
        totmoney = np.sum(richaxis)
        for i in range(len(richaxis)):
            cumrich[i] = cumrich[i - 1] + richaxis[i]
        normcumrich = (cumrich + 0.5) / totmoney
        print(normcumrich)
        gini = 1 - 2 * np.sum(normcumrich) / people
        return gini

        ginicurve = np.zeros(len(richaxis))
        ginicurve[0] = normcumrich[0]
        for i in range(1, len(richaxis)):
            ginicurve[i] = normcumrich[i] + ginicurve[i - 1]

        print('GINI----------')
        print(gini)
        x = np.arange(len(richaxis))
        plt.plot(x / people, normcumrich, label='no debt')
        plt.plot(x / people, x / people)
        plt.xlabel('cumulative share of people')
        plt.ylabel('cumulative wealth')
        plt.legend()
        plt.show()
        # plt.plot(richaxis,ginicurve)

    if(graph==1 and show==1):

        people = len(richaxis)
        cumrich = np.zeros(people)
        totmoney = np.sum(richaxis)
        for i in range(len(richaxis)):
            cumrich[i] = cumrich[i - 1] + richaxis[i]
        normcumrich = (cumrich + 0.5) / totmoney
        print(normcumrich)
        gini = 1 - 2 * np.sum(normcumrich) / people
        return gini
        ginicurve = np.zeros(len(richaxis))
        ginicurve[0] = normcumrich[0]
        for i in range(1, len(richaxis)):
            ginicurve[i] = normcumrich[i] + ginicurve[i - 1]

        print('GINI----------')
        print(gini)
        x = np.arange(len(richaxis))
        plt.plot(x / people, normcumrich, label='no debt')
        plt.plot(x / people, x / people)
        plt.xlabel('cumulative share of people')
        plt.ylabel('cumulative wealth')
        plt.legend()
        # plt.plot(richaxis,ginicurve)
        plt.show()








