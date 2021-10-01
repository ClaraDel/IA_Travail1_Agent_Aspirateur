from copy import deepcopy 

class Capteur :
 
    def __init__(self, env ):
        self.env = env

    #def UpdateEnv(self,env):
    #    self.env = env
        
    def scan(self):
        self.env.resetPerformanceChecking()
        return deepcopy(self.env)
        
        