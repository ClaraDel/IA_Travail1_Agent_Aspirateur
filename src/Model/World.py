from Model.Environment import Environment
from Model.Room import Room

class World:
	
    def __init__(self):
        self.env = Environment()
        #print("Main: before creating thread")
        x = threading.Thread(target=self.thread_env, args=(1,))
        print("Main    : before running thread")
        #self.print_env()
        x.start()
        #x.join()
        #print("Main    : all done")

    def thread_env(self , name):
        print("Thread start")
        while(True):
            dirtProbability = random.randrange(100)
            if (dirtProbability <= 1):
                #Dirt placement
                dirt = random.randrange(25)
                self.env.roomList[dirt].setDirt(True)
                print("Dirt placed in",self.env.roomList[dirt].getXPos(),",",self.env.roomList[dirt].getYPos())
            
            jewelProbability = random.randrange(100)
            if (jewelProbability <= 1):
                #jew placement
                jewel = random.randrange(25)
                self.env.roomList[jewel].setJewel(True)
                print("Jew placed in",self.env.roomList[jewel].getXPos(),",",self.env.roomList[jewel].getYPos())
        print("Thread end")