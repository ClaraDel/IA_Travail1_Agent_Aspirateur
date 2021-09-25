
class Effecteur:

    # En fonction de l'action appelée, le comportement des effecteurs ne sera pas le même
    def processAction(self, x, y, action):
        if (action == "right"):
            return x+1,y,False
        elif (action == "left"):
            return x-1,y,False
        elif (action == "up"):
            return x,y-1,False
        elif (action == "down"):
            return x,y+1,False
        elif (action == "suck"):
            return x,y,True
    
    #Alternative : a voir si fonctionne
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