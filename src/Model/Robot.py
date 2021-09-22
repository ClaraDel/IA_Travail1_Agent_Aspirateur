# -*- coding: utf-8 -*-
import threading
import time
from Model.ExplorationGraph import ExplorationGraph

class Robot:
    # Capteur
    # Effecteur
    # beliefEnv
    
    def thread_robot(self , name):
        print("Thread started \n")
        for i in range (5):
            print("Tread robot en exécution\n")
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
        print("Thread ended")
    
    def __init__(self, capteur, positionRobot):
        self.capteur = capteur
        self.positionRobot = positionRobot
        thread_robot = threading.Thread(target=self.thread_robot, args=(1,))
        print("Main    : robot thread created")
        thread_robot.start()
        

        
        
        
        
        
        
        
        
        
    # "son état interne devrait contenir un état mental sous la forme BDI :"
    def beliefs():
       beliefEnv = capteur.scan()
       return beliefEnv
       # for i in range(5):
       #     for j in range(5):
       #         if(env[i][j].jew=True) :
   
    def Desires():
       return
       #série d’états que l’agent souhaite atteindre ou description partielle d’un état  à atteindre.
       #peuvent être implantés lors de la création du robot ou en cours de route
       
    def intentions():
       return
       #actions que le robor compte effectuer dans le futur afin d’atteindre son/ses objectifs
