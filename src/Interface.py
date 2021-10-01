from tkinter import Label, PhotoImage, Button, Radiobutton, StringVar
import time
  
class Table(): 
      
    def __init__(self, env, root, robot, world): 
        self.root = root
        self.env = env
        self.robot = robot
        self.world = world
        self.imgRobot = PhotoImage(file='Images/robot.png')
        self.imgDirt = PhotoImage(file='Images/dirt.png')
        self.imgJewel = PhotoImage(file='Images/jewel.png')
        self.imgDirtAndJewel = PhotoImage(file='Images/DirtAndJewel.png')
        self.imgDirtAndRobot = PhotoImage(file='Images/DirtAndRobot.png')
        self.imgJewelAndRobot = PhotoImage(file='Images/jewelAndRobot.png')
        self.imgNothing = PhotoImage(file='Images/nothing.png')
        self.imgDirtAndJewelAndRobot = PhotoImage(file='Images/DirtAndJewelAndRobot.png')
        
        Button(self.root, text = "Quitter", command = self.stop, activebackground  = '#F5F5F5').grid(row=5,column=4, pady = 10, ipadx = 6, ipady = 3)
        
        for room in self.env.roomList:
            Label(self.root, image=self.imgNothing).grid(row=room.getXPos(), column=room.getYPos(), padx=4, pady=4)

    def update_draw(self):
        for room in self.env.roomList:
            panel = Label(self.root, image=self.imgNothing)
            #if (not(room.getDirt() and room.getJewel(), and self.robot.x == room.xPos and self.robot.y == room.yPos)):
            if (room.getDirt()):
                panel =  Label(self.root, image=self.imgDirt)
                if (room.getJewel()):
                    panel =  Label(self.root, image=self.imgDirtAndJewel)
                    if (self.robot.x == room.xPos and  self.robot.y == room.yPos):
                        panel =  Label(self.root, image=self.imgDirtAndJewelAndRobot)
                elif (room.getDirt() and self.robot.x == room.xPos and self.robot.y == room.yPos):
                    panel = Label(self.root, image=self.imgDirtAndRobot)
            elif (room.getJewel()):
                panel =  Label(self.root, image=self.imgJewel)
                if (self.robot.x == room.xPos and  self.robot.y == room.yPos):
                    panel = Label(self.root, image=self.imgJewelAndRobot)
            elif (self.robot.x == room.xPos and  self.robot.y == room.yPos):
                panel =  Label(self.root, image=self.imgRobot)
            panel.grid(row=room.getXPos(), column=room.getYPos(), padx=4, pady=4)
        
    def stop(self):
        self.world.gameIsRunning = False
        time.sleep(1)
        self.root.destroy()
        
class PopUp(): 
    
    def __init__(self, rootPopup):
        self.rootPopup = rootPopup
        self.explorationType = StringVar()
        self.explorationType.set("Informé")
        self.choix = ""
        
    def lancer(self) :
        
        Label(self.rootPopup, 
                text="Bienvenue sur cette simulation d'un agent aspirateur dans un manoir !",
                 padx = 20, pady = 10, anchor  ='center').grid(row=1,column=1, sticky='w')
                
        Label(self.rootPopup, 
                text="Quel type d'exploration voulez-vous utiliser ?",
                padx = 20, pady = 5, justify ="left").grid(row=2,column=1, sticky='w')
        
        Radiobutton(self.rootPopup, 
                       text="Informé",
                       padx = 20, pady = 5, 
                       variable=self.explorationType,
                       value="Informé").grid(row=3,column=1, sticky='w')
        
        Radiobutton(self.rootPopup, 
                       text="Non informé",
                       padx = 20, 
                       variable=self.explorationType, 
                       value="Non informé").grid(row=4,column=1, sticky='w')
        
        Button(self.rootPopup, text = "Valider", command = self.valider, padx = 10, activebackground  = '#F5F5F5').grid(row=5,column=1, sticky='se', pady = 10, padx = 60)
        Button(self.rootPopup, text = "Quitter", command = self.quitter, activebackground  = '#F5F5F5').grid(row=5,column=1, pady = 10, sticky='se')
        
    def valider(self):
        self.choix = "continuer"
        self.rootPopup.destroy()
        
    def quitter(self):
        self.choix = "quitter"
        self.rootPopup.destroy()
        
            
        

                          