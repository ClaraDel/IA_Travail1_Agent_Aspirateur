from tkinter import *
from PIL import ImageTk,Image  
import time
  
class Table(): 
      
    def __init__(self, env, root, robot): 
        self.root = root
        self.env = env
        self.robot = robot
        self.imgRobot = PhotoImage(file='Images/robot.png')
        self.imgDirt = PhotoImage(file='Images/dirt.png')
        self.imgJewel = PhotoImage(file='Images/jewel.png')
        self.imgDustAndJewel = PhotoImage(file='Images/DustAndJewel.png')
        self.imgNothing = PhotoImage(file='Images/nothing.png')
        Button(text = "Quitter", command = self.root.quit).grid(row=5,column=4)
        for room in self.env.roomList:
            Label(self.root, image=self.imgNothing).grid(row=room.getXPos(), column=room.getYPos(), padx=4, pady=4)

    def update_draw(self):
        panel = Label() 
        for room in self.env.roomList:
            if (room.getDirt()):
                panel =  Label(self.root, image=self.imgDirt)
                if (room.getJewel()):
                    panel =  Label(self.root, image=self.imgDustAndJewel)
            elif (room.getJewel()):
                panel =  Label(self.root, image=self.imgJewel)
            if(self.robot.x == room.xPos and  self.robot.y == room.yPos):
                panel =  Label(self.root, image=self.imgRobot)
            panel.grid(row=room.getXPos(), column=room.getYPos(), padx=4, pady=4)
            
                
                
    def close_env(self, root):
        root.quit()

                          