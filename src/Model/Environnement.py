from Model.Case import Case
import threading
import time
import random


class Environnement :
    
    def thread_env(self , name):
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
                self.env[xD][yD].dirt=True
                print("Dirt placed in",xD,",",yD)
            
            if (jewelProbability <= 1 and numberJewel < jewelLimit):
                #jewel placement
                xJ = random.randrange(5)
                yJ = random.randrange(5)
                self.env[xJ][yJ].jew=True
                print("Jewel placed in",xJ,",",yJ)
                numberJewel += 1
    
    
    def __init__(self ):
        self.env = []
        for i in range(5):
            l = []
            for j in range(5):
                l.append(Case(False,False, False))
            self.env.append(l)
        print("Main    : before creating thread")
        x = threading.Thread(target=self.thread_env, args=(1,))
        print("Main    : before running thread")
        self.print_env()
        self.print_env()
        x.start()
        x.join()
        print("Main    : all done")
    
    
        #Display the env in console
    def print_env(self):
        for row in self.env:
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


    