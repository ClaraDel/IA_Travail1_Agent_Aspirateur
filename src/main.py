from Model.Environnement import Environnement
from Model.Robot import Robot
from Model.Capteur import Capteur
from tkinter import *
from Interface import Table
import time


def main():
    env = Environnement()
    
    root = Tk()
    root.title('PythonGuides')
    root.geometry('500x400')
    root.config(bg='#5fffff')
    t = Table(env, root)
    
    root.update()
    env.lauch_thread()
    print("Environnement créé \n")
    
    #root.after(0, t.update_draw())
    #root.mainloop()
    
    capteur = Capteur(env)
    positionInitialeRobot = "00"
    robot = Robot(capteur, positionInitialeRobot)
    print("Robot créé avec capteurs")
    #voir quand faire ça et quoi faire

if __name__ == "__main__":
    main()
            
    