from Model.Environment import Environment
from Model.Robot import Robot

class Controller:  

    
        
    def getEnv(self):
        return self.env
    
    def __init__(self):
         
        self.env = Environment()
        self.robot = Robot(self)
    
    
if __name__ == "__main__":
    Controller()
    