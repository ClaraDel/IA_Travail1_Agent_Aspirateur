
class Effecteur:
    
    def __init__(self,env):
        self.env = env

    def processAction(self, robot, action):
        if (action == "right"):
            robot.x += 1
        elif (action == "left"):
            robot.x -= 1
        elif (action == "up"):
            robot.y -= 1
        elif (action == "down"):
            robot.y += 1
        elif (action == "clean"):
            self.env.getRoom(robot.x, robot.y).setDirt(False)
            self.env.downDirtNumber()