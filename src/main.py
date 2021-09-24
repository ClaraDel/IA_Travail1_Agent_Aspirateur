from Model.Environment import Environment
from Model.Robot import Robot
from Model.Capteur import Capteur
from Model.World import World
from tkinter import *
from Interface import Table


def main():
    env = Environment()
    print("Environnement créé \n")
    
    capteur = Capteur(env)
    positionX = 1
    positionY = 1
    robot = Robot(capteur, positionX, positionY)
    print("Robot créé avec capteurs")
    world = World(env, robot)
    print("Monde créé ")
    
    #root.update()
    root = Tk()
    root.title('PythonGuides')
    root.geometry('700x400')
    root.config(bg='#5fffff')
    t = Table(env, root)
    for i in range(10,30000, 5000):
        root.after(i, t.update_draw)
    root.mainloop()
    
if __name__ == "__main__":
    main()
            
    