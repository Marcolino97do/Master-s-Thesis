import numpy as np
import numpy.ma as ma
import random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import math


def graph(pdf,allrichness):
    plt.plot(allrichness, pdf, linestyle='', marker='.', label='dati')
    plt.legend()
    plt.xlabel('wealth')
    plt.ylabel('population')
    #plt.savefig('popol{}kt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
    plt.show()

    #plt.plot(xfitm, exponential(xfitm, *popt), 'r', label='fit: T={:.2f} $\pm$ {:.2f}'.format(-popt[1], np.sqrt(pcov[1][1])))
    plt.semilogy(allrichness, pdf, linestyle='', marker='.',label='datini')
    plt.legend()
    plt.xlabel('wealth')
    plt.ylabel('population')
    #plt.savefig('popol{}klogt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
    plt.show()

def grafit(pdf, allrichness, initmoney, people, mask, mode):
    if(mode==0):#FOR THE EXPONENTIAL FUNCTION
        #MASKING ARRAYS
        maskpdf=ma.masked_where(pdf<mask,pdf)
        #allrichness=ma.masked_less(pdf,mask)

        #DOING THE FIT
        initguess = [initmoney]
        globalize_as_pop(people)
        popt,pcov=curve_fit(exp, allrichness, maskpdf, initguess)
        sigmaT=np.abs(np.sqrt(np.abs(pcov[0][0])))

        #PLOTTING
        plt.plot(allrichness, pdf, linestyle='', marker='.', label='dati')
        plt.plot(allrichness, exp(allrichness, *popt), 'r', label='fit: T={:.2f} $\pm$ {:.2f}'.format(popt[0], sigmaT))
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        # plt.savefig('popol{}kt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
        plt.show()


        plt.semilogy(allrichness, pdf, linestyle='', marker='.', label='datini')
        plt.semilogy(allrichness, exp(allrichness, *popt), 'r', label='fit: T={:.2f} $\pm$ {:.2f}'.format(popt[0], sigmaT))
        plt.legend()
        plt.xlabel('wealth')
        plt.ylabel('population')
        # plt.savefig('popol{}klogt={}.jpeg'.format(people / 1000, graphnumber), dpi=600)
        plt.show()

        return(popt[0],sigmaT)

def fit(pdf, allrichness, initmoney, people, mask, mode):
    if(mode==0):#FOR THE EXPONENTIAL FUNCTION
        #MASKING ARRAYS
        maskpdf=ma.masked_where(pdf<mask,pdf)
        #allrichness=ma.masked_less(pdf,mask)

        #DOING THE FIT
        initguess = [initmoney]
        globalize_as_pop(people)
        popt,pcov=curve_fit(exp, allrichness, maskpdf, initguess)
        sigmaT=np.abs(np.sqrt(np.abs(pcov[0][0])))
        return (popt[0], sigmaT)


def exp(x,T):
    return (np.exp(-x/T))*pop*(1-np.exp(-1/T))

def globalize_as_pop(a):
    global pop
    pop=a


