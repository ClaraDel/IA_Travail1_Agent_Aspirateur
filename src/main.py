from Model.Environment import Environment
from Model.Effecteur import Effecteur
from Model.Robot import Robot
from Model.Capteur import Capteur
from Model.World import World
from tkinter import Tk
from Interface import Table
import time


def main():
    # Création du manoir
    env = Environment()
    print("Environnement créé \n")
    
    # Création de l'agent 
    effecteur = Effecteur(env)
    capteur = Capteur(env)
    positionX = 1  # RANDOM ? A mettre dans world?
    positionY = 1
    robot = Robot(capteur, effecteur, positionX, positionY)
    print("Robot créé avec capteurs et effecteurs")
    
    # Ajout des deux éléments dans notre monde (lancement des threads)
    world = World(env, robot)
    print("Monde créé ")
    
    # Gestion de l'interface
    #root.update()
    root = Tk()
    root.title('PythonGuides')
    root.geometry('550x550')
    root.config(bg='#30449F')
    t = Table(env, root, robot)
    
    while(True):
        root.update()
        t.update_draw()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
            
    