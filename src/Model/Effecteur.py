
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