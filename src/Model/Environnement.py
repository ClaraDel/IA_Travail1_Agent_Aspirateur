from Model.Case import Case
import threading
import time
import random
from abc import ABC, abstractmethod

class Environnement(ABC) :
    
    @abstractmethod 
    def thread_env(env, name):
        print("Thread start")
        jewelLimit = 5
        numberJewel = 0
        while (True):

            #probability that dirt and jewel will be generated into the manor
            dirtProbability = random.randrange(100)
            jewelProbability = random.randrange(100)

            if (dirtProbability <= 1):
                #Dirt placement
                xD = random.randrange(5)
                yD = random.randrange(5)
                env[xD][yD].dirt=True
                print("Dirt placed in",xD,",",yD)
            
            if (jewelProbability <= 1 and numberJewel < jewelLimit):
                #jewel placement
                xJ = random.randrange(5)
                yJ = random.randrange(5)
                env[xJ][yJ].jew=True
                print("Jewel placed in",xJ,",",yJ)
                numberJewel += 1
    
    @abstractmethod 
    def init_env():
        env = []
        for i in range(5):
            l = []
            for j in range(5):
                l.append(Case(False,False, False))
            env.append(l)
        print("Main    : before creating thread")
        print_env()
        x = threading.Thread(env, args=(1,))
        print("Main    : before running thread")
        print_env()
        x.start()
        x.join()
        print("Main    : all done")
    
    
    #Display the env in console
    @abstractmethod 
    def print_env():
        for row in env:
            for col in row:
                if col.jew:
                    print("J",end='')
                if col.dirt:
                    print("D",end='')
                if col.aspi:
                    print("A",end='')
                if (not(col.dirt) and not(col.jew) and not(col.aspi)):
                    print("X",end='')
                print("  ",end='')
            print('')
        print("----------")


    