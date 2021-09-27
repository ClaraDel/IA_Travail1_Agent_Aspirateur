
class Effecteur:
    
    def __init__(self,env):
        self.env = env

    def processAction2(self, robot, action):
        if (action == "right"):
            robot.positionX += 1
        elif (action == "left"):
            robot.positionX -= 1
        elif (action == "up"):
            robot.positionY -= 1
        elif (action == "down"):
            robot.positionY += 1
        elif (action == "clean"):
            self.env.getRoom(robot.positionX, robot.positionY).setDirt(False)
            self.env.downDirtNumber()