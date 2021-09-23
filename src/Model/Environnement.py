from Model.Case  import Case
import threading
import time
import random
from tkinter import *
from Interface import Table


class Environnement :
    
    def thread_env(self , name): 
        print("Thread started \n")
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
            
            #Affuchage
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
        
        #thread_env.join()
        #print("Main    : all done")
        
    def lauch_thread(self) :
        thread_env = threading.Thread(target=self.thread_env, args=(1,)) #génère une poussière et un bijoux
        print("Main    : environement thread created")
        thread_env.start()
    
    
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
    #self.update_env()


    


    