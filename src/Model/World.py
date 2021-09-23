from Model.Environment import Environment

class World:
	
	def __init__(self):
		self.env = Environment()
        print("Main    : before creating thread")
        x = threading.Thread(target=self.thread_env, args=(1,))
        print("Main    : before running thread")
        #self.print_env()
        x.start()
        #x.join()
        #print("Main    : all done")

	def thread_env(self , name):
        print("Thread start")
        while(True):
            #Dirt placement
            dirt = random.randrange(25)
            self.env.roomList.dirt=True
            print("Dirt placed in",xD,",",yD)
            
            #jew placement
            xJ = random.randrange(5)
            yJ = random.randrange(5)
            self.env[xJ][yJ].jew=True
            print("Jew placed in",xJ,",",yJ)
            #self.print_env()
            time.sleep(5)
        print("Thread end")