import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math


def graph():
    #IMPORT DATA
    T,sigmaT = np.loadtxt('temperature.txt', unpack=True)
    maxis=np.arange(1,len(T)+1)
    diff=T-maxis
    plt.errorbar(maxis,diff,sigmaT,fmt='o',ecolor='lightgray',capsize=1, elinewidth=1,linestyle='',label='Fitted T')
    #plt.plot(maxis,diff, linestyle='', marker='.', label='dati')
    x = np.linspace(1, len(maxis), 100)
    prediction=np.ones(len(x))
    prediction=1/(np.log(1+1/x))-x

    plt.plot(x,prediction, linestyle='-', marker='', label='$\\frac{1}{\ln(1+1/m_0)}-m_0$')
    asintote=np.ones(len(maxis))*0.5
    plt.plot(maxis,asintote)
    plt.legend()
    plt.xlabel('$m_0$')
    plt.ylabel('T-$m_0$')
    #plt.savefig('popol{}kt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
    plt.show()