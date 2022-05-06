import numpy as np

#FIND THE PROBABILITY DISTRIBUTION FUNCTION FOR THE ARRAY OF THE ACCOUNTS
def pdf(richaxis):
    allrichness = np.arange(np.min(richaxis), np.max(richaxis) + 1)
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
    return(temp)

#FIND THE SHANNON ENTROPY OF DISTRIBUTION
def entropy(temp):
    people=np.sum(temp)
    print(people)
    s = 0
    for i in temp:
        if (i != 0):
            s -= (i / people) * np.log(i / people)
    return(s)

#WRITE DATA ON FILE
def write_params(time,people,initmoney,runs):
    f = open('param.txt', 'w')
    f.write('{} {} {} {}'.format(time, people, initmoney,runs))
    f.close()

def write_temperature(T,sigmaT):
    f = open('temperature.txt', 'w')
    f.write('{} {}\n'.format(T,sigmaT))
    f.close()

def append_temperature(T,sigmaT):
    f = open('temperature.txt', 'a')
    f.write('{} {}\n'.format(T, sigmaT))
    f.close()

def write_avgtemp(T):
    f = open('avgtemp.txt', 'w')
    f.write('{}\n'.format(T))
    f.close()

def append_avgtemp(T):
    f = open('avgtemp.txt', 'a')
    f.write('{}\n'.format(T))
    f.close()

def calctemp():
    T=np.loadtxt('avgtemp.txt',unpack=True)
    avgT=np.mean(T)
    sigmaT=np.sqrt((np.sum((T-avgT)**2))/(len(T)-1))
    print('--GET READY--')
    print(avgT,sigmaT)
    return(avgT,sigmaT)