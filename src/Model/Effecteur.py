
class Effecteur:
    
    def __init__(self,env):
        self.env = env

    def processAction(self, robot, action):
        if (action == "right"):
            robot.y += 1
        elif (action == "left"):
            robot.y -= 1
        elif (action == "up"):
            robot.x -= 1
        elif (action == "down"):
            robot.x += 1
        elif (action == "clean"):
            self.env.cleanRoom(robot.y, robot.x)
        elif (action == "takeObj"):
            self.env.removeJewel(robot.y, robot.x)
        self.env.checkMyPerformance(robot)
    
    def resetPerformance(self):
        self.env.resetPerformanceChecking()