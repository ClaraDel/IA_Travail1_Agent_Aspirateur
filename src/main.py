from Model.Environment import Environment
from Model.Effecteur import Effecteur
from Model.Robot import Robot
from Model.Capteur import Capteur
from Model.World import World
from tkinter import *
from Interface import Table


def main():
    env = Environment()
    print("Environnement créé \n")
    effecteur = Effecteur()
    capteur = Capteur(env)
    positionX = 1
    positionY = 1
    robot = Robot(capteur, effecteur, positionX, positionY)
    print("Robot créé avec capteurs")
    world = World(env, robot)
    print("Monde créé ")
    
    #root.update()
    root = Tk()
    root.title('PythonGuides')
    root.geometry('550x550')
    root.config(bg='#30449F')
    t = Table(env, root)
    for i in range(10,30000, 5000):
        root.after(i, t.update_draw)

    root.mainloop()
    
if __name__ == "__main__":
    main()
            
    