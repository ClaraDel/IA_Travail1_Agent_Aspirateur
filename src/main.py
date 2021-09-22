from Model.Environnement import Environnement
from Model.Robot import Robot
from Model.Capteur import Capteur
from tkinter import *

def main():
    
    env = Environnement()
    print("Environnement créé \n")
    capteur = Capteur(env)
    positionInitialeRobot = "00"
    robot = Robot(capteur, positionInitialeRobot)
    print("Robot créé avec capteurs")
    #voir quand faire ça et quoi faire

if __name__ == "__main__":
    main()
            
    