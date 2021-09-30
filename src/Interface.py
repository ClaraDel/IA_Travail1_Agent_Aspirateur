from tkinter import Label, PhotoImage, Button
  
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
        
        Button(text = "Quitter", command = self.stop).grid(row=5,column=4)
        
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
        self.root.destroy()

                          