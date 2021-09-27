
class Effecteur:

    def processAction2(self, robot, action, trueEnvironment):
        if (action == "right"):
            robot.positionX += 1
        elif (action == "left"):
            robot.positionX -= 1
        elif (action == "up"):
            robot.positionY -= 1
        elif (action == "down"):
            robot.positionY += 1
        elif (action == "suck"):
            trueEnvironment.getRoom(robot.positionX, robot.positionY).setDirt(False)
            trueEnvironment.setDirtNumber(trueEnvironment.getDirtNumber()-1)