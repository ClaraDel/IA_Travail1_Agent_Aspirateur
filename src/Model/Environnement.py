from Model.Salle import Salle
import threading
import time
import random


class Environnement :

    
    
    def thread_env(self , name):
        print("Thread start")
        for i in range (5):
            #Dirt placement
            xD = random.randrange(5)
            yD = random.randrange(5)
            self.env[xD][yD].dirt=True
            print("Dirt placed in",xD,",",yD)
            
            #jew placement
            xJ = random.randrange(5)
            yJ = random.randrange(5)
            self.env[xJ][yJ].jew=True
            print("Jew placed in",xJ,",",yJ)
            #self.print_env()
            time.sleep(5)
        print("Thread end")
    
    
    def __init__(self):

        self.listeSalle = []
        self.nbPoussiere = 0
        self.nbBijou = 0

        for i in range(5):
            for j in range(5):
                listeSalle.append(Salle(i,j))

        print("Main    : before creating thread")
        x = threading.Thread(target=self.thread_env, args=(1,))
        print("Main    : before running thread")
        #self.print_env()
        x.start()
        #x.join()
        #print("Main    : all done")
    
    
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
        

    


    