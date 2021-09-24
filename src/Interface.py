from tkinter import *
import time
  
class Table(): 
      
    def __init__(self, env, root): 
        self.root = root
        self.env = env
        self.messageCaseJew = ""
        self.messageCaseDirt = ""

    def update_draw(self):
        
        for room in self.env.roomList:
            self.e = Entry(self.root, width=20)
            self.e.grid(row=room.getXPos(), column=room.getYPos())
            if (room.getDirt()):
                self.messageCaseDirt = "Poussière"
            if (room.getJewel()):
                self.messageCaseJew = "Bijoux"
            self.e.insert(END, str(self.messageCaseJew + " " + self.messageCaseDirt))
            self.messageCaseJew = self.messageCaseDirt = ""
        time.sleep(1)
                
    def close_env(self, root):
        root.quit()

                          