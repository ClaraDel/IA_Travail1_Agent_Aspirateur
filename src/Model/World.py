import threading
import random
import time

class World:
	
    def __init__(self, env, robot):
        self.env = env
        self.robot = robot
        #print("Main: before creating thread")
        thread_e = threading.Thread(target=self.thread_env, args=(1,))
        thread_r = threading.Thread(target=self.thread_robot, args=(1,))
        thread_e.start()
        thread_r.start()
        
        #x.join()
        #print("Main    : all done")

    def thread_env(self , name):
        print("thread environment started \n")
        for i in range(5):
            dirtProbability = random.randrange(2)
            if (dirtProbability <= 1):
                # Placement des poussières et incrémentation du nombre de poussières dans l'environnement
                dirt = random.randrange(25)
                #dirt=i+1
                if (not self.env.roomList[dirt].getDirt()):
                    self.env.addDirt(dirt)
                    print("Dirt placed in",self.env.roomList[dirt].getXPos(),",",self.env.roomList[dirt].getYPos())
            
            jewelProbability = random.randrange(3)
            if (jewelProbability <= 1):
                # Placement des bijoux et incrémentation du nombre de bijoux dans l'environnement
                jewel = random.randrange(25)
                if (not self.env.roomList[jewel].getJewel()):
                    self.env.addJewel(jewel)
                    print("Jew placed in",self.env.roomList[jewel].getXPos(),",",self.env.roomList[jewel].getYPos())
            self.env.print_env()
            time.sleep(2)
        print("Thread environment ended")
        
        
    def thread_robot(self , name):
        time.sleep(5)
        print("thread robot started \n")
        for i in range (2):
            print("Tread robot en exécution\n")
            self.robot.ObserveAndUpdate()
            self.robot.ChooseAnAction()
            self.robot.JustDoIt()
               # While (amIAlive()){
               #     ObserveEnvironmentWithAllMySensors()
               #     UpdateMyState()
               #     ChooseAnAction()
               #     justDoIt()
               #    }   
            # beliefEnv = beliefs()
            # explorationBFS = ExplorationGraph(beliefEnv)
            # explorationBFS.bfs(positionRobot)
            time.sleep(5)
        print("Thread robot ended")
        
