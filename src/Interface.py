from tkinter import *
from PIL import ImageTk,Image  
import time
  
class Table(): 
      
    def __init__(self, env, root): 
        self.root = root
        self.env = env

    def update_draw(self):
        self.imgRobot = PhotoImage(file='D:/cours UQAC/IA/aspirobot/src/Images/robot.png')
        self.imgDirt = PhotoImage(file='D:/cours UQAC/IA/aspirobot/src/Images/dirt.png')
        self.imgJewel = PhotoImage(file='D:/cours UQAC/IA/aspirobot/src/Images/jewel.png')
        self.imgDustAndJewel = PhotoImage(file='D:/cours UQAC/IA/aspirobot/src/Images/DustAndJewel.png')
        self.imgNothing = PhotoImage(file='D:/cours UQAC/IA/aspirobot/src/Images/nothing.png')
        
        for room in self.env.roomList:
            panel = Label(self.root, image=self.imgNothing)         
            if (room.getDirt()):
                panel =  Label(self.root, image=self.imgDirt)
                if (room.getJewel()):
                    panel =  Label(self.root, image=self.imgDustAndJewel)
            elif (room.getJewel()):
                panel =  Label(self.root, image=self.imgJewel)
            panel.grid(row=room.getXPos(), column=room.getYPos(), padx=4, pady=4)
                
    def close_env(self, root):
        root.quit()

                          