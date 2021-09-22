from Model.Case  import Case
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
            if (random.randrange(2)):
                xJ = random.randrange(5)
                yJ = random.randrange(5)
                self.env[xJ][yJ].jew=True
                print("Jew placed in",xJ,",",yJ)
            else : print("No jew placed this time")
            
            self.print_env()
            time.sleep(5)
        print("Thread end")
    
    
    def __init__(self ):
        self.env = []
        for i in range(5):
            l = []
            for j in range(5):
                l.append(Case(False,False, False))
            self.env.append(l)
        print("Main    : before creating thread")
        x = threading.Thread(target=self.thread_env, args=(1,)) #génère une poussière et un bijoux
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
        

    


    