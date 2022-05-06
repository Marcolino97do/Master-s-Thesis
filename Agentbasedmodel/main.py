import numpy as np
import subprocess


import command
import plottemp
import plotter
import debt

debt.graph()

time=1000000
people=1000

maxinitmoney=10
runs=10
mask=50


#CYCLE ON INITMONEY
initmoney=1
for initmoney in range(1,maxinitmoney+1):
    #WRITE PARAMETERS ON FILE
    command.write_params(time,people,initmoney,runs)

    #EVOLUTE THE SYSTEM

    if(initmoney==1):
        print('GETTING THE SYSTEM TO RIGHT TEMPERATURE...')
        subprocess.call(["gcc","provino.c"])
        subprocess.call("./a.out")
        print('DONE\n')
    else:
        proc = subprocess.Popen(['python3.8', r"caller.py", str(500000 + i)])
        # proc=subprocess.Popen(["gcc","random.c"])
        # subprocess.call("./a.out")


        #LOAD DATA
        accounts=np.loadtxt('results.txt',unpack=True,dtype=int)

        #FIND THE PDF
        pdf=command.pdf(accounts)
        allrichness=np.arange(np.min(accounts),np.max(accounts)+1)

        #DOING THE FIT & PLOT RESULTS
        mode=0
        if(i==1):
            T,sigmaT=plotter.fit(pdf,allrichness,initmoney,people,mask,mode)
        else:
            T, sigmaT = plotter.fit(pdf, allrichness, initmoney, people, mask, mode)
        print('T and SigmaT=--------')
        print(T,sigmaT)
        if(i==1):
            command.write_avgtemp(T)
        else:
            command.append_avgtemp(T)
    #CALCULATE THE AVERAGE TEMPERATURE AND THE ERROR
    T,sigmaT=command.calctemp()
    if(initmoney==1):
        command.write_temperature(T,sigmaT)
    else:
        command.append_temperature(T,sigmaT)

#AFTER THE FOR
plottemp.graph()





