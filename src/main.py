from Model.Environnement import Environnement
from Model.Robot import Robot
from Model.Capteur import Capteur

     
def main():
    env = Environnement()
    print("Environnement créé \n")
    capteur = Capteur(env)
    robot = Robot(capteur)
    print("Robot créé avec capteurs")
    #voir quand faire ça et quoi faire
    
    

if __name__ == "__main__":
    main()
    
    
    # def getEnv(self):
    #     return self.env
    
    # def __init__(self):
         
    #     self.env = Environnement()
    #     self.robot = Robot(self)