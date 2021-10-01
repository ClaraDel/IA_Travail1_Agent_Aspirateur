from Model.Environment import Environment
from Model.Effecteur import Effecteur
from Model.Robot import Robot
from Model.Capteur import Capteur
from Model.World import World
from tkinter import Tk, PhotoImage
from Interface import Table, PopUp
import time


def main():
    # Création du manoir
    env = Environment()
    
    # Création de l'agent 
    effecteur = Effecteur(env)
    capteur = Capteur(env)
    positionX = 1
    positionY = 1
    
    rootPopup = Tk()
    rootPopup.geometry('420x180')
    rootPopup.title("Choix d'exploration")
    rootPopup.iconphoto(False, PhotoImage(file='Images/robot.png'))
    popUp = PopUp(rootPopup)
    popUp.lancer()
    rootPopup.mainloop()
    
    if (popUp.choix == "continuer"):
        print("Exploration ", popUp.explorationType.get(), "e choisie.") 
        robot = Robot(capteur, effecteur, positionX, positionY, popUp.explorationType.get())
        
        # Ajout des deux éléments dans notre monde (lancement des threads)
        world = World(env, robot)
        
        # Gestion de l'interface
        #root.update()
        root = Tk()
        root.title('Manoir et robot intelligent')
        root.iconphoto(False, PhotoImage(file='Images/robot.png'))
        root.geometry('550x600')
        root.config(bg='#30449F')
        t = Table(env, root, robot, world)
        
        
        #for i in range(200):
        while(world.gameIsRunning):
            root.update()
            t.update_draw()
            time.sleep(0.05)
            
    elif (popUp.choix == "quitter"):
        print("Simulation non lancée.")
        
if __name__ == "__main__":  
    main()