import threading
import time
import random
from Model.Environnement import Environnement
    

def thread_env(name,env):
    print("Thread start")
    for i in range (5):
        #Dirt placement
        xD = random.randrange(5)
        yD = random.randrange(5)
        env.env[xD][yD].dirt=True
        print("Dirt placed in",xD,",",yD)
        
        #jew placement
        xJ = random.randrange(5)
        yJ = random.randrange(5)
        env.env[xJ][yJ].jew=True
        print("Jew placed in",xJ,",",yJ)
        env.print_env()
        time.sleep(5)
    print("Thread end")
    
    


def place_aspi(env,x,y):
    env.env[x][y].aspi=True    

        

if __name__ == "__main__":
    
    env = Environnement()
    print("Main    : before creating thread")
    x = threading.Thread(target=thread_env, args=(1,env))
    print("Main    : before running thread")
    env.print_env()
    place_aspi(env, 2, 2)
    env.print_env()
    x.start()
    x.join()
    print("Main    : all done")
    
