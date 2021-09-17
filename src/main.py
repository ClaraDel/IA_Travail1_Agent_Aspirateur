import threading
import time
import random
from dataclasses import dataclass
#import tkinter
#import interface

@dataclass
class Case:
    jew : bool
    dirt : bool
    aspi : bool
    


def thread_env(name,env):
    print("Thread start")
    for i in range (5):
        #Dirt placement
        xD = random.randrange(5)
        yD = random.randrange(5)
        env[xD][yD].dirt=True
        print("Dirt placed in",xD,",",yD)
        
        #jew placement
        xJ = random.randrange(5)
        yJ = random.randrange(5)
        env[xJ][yJ].jew=True
        print("Jew placed in",xJ,",",yJ)
        print_env(env)
        time.sleep(5)
    print("Thread end")
    
    


env = []
for i in range(5):
    l = []
    for j in range(5):
        l.append(Case(False,False, False))
    env.append(l)
    
def place_aspi(env,x,y):
    env[x][y].aspi=True
    
    
#Display the env in console
def print_env(env):
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
    

        

if __name__ == "__main__":
    print("Main    : before creating thread")
    x = threading.Thread(target=thread_env, args=(1,env))
    print("Main    : before running thread")
    print_env(env)
    place_aspi(env, 2, 2)
    print_env(env)
    x.start()
    x.join()
    print("Main    : all done")
    
