from copy import deepcopy

class Vertice:

    def __init__(self,roomX, roomY,listRooms, roomsCleaned, roomsTidy, roomState, dirtNumberRemaining, _oldVerticeList):
        # Coordonnées de la salle avec le robot
        self.x = roomX
        self.y = roomY
        self.dirtNumberRemaining = dirtNumberRemaining
        
        # Etat propre ou sale
        self.clean = roomState
        
        # Liste des salles visitées pour arriver dans cette salle (=chemin de la branche)
        self.path = listRooms
        
        # Liste des salles nettoyées sur le chemin ci dessus (donc dans la branche)
        self.roomsCleaned = roomsCleaned

        # Calcul de l'heuristique
        self.heuristic = self.dirtNumberRemaining + len(self.path)
        
        # Liste contenant les coordonnées des salles nettoyées
        self.roomsTidy = roomsTidy

        # Liste contenant les vertices visités dans la branche
        oldVerticeList = deepcopy(_oldVerticeList)
        oldVerticeList.append(self)
        self.visitedVerticeList = oldVerticeList

    def __str__(self):
        return "(" + str(self.x) + "," +  str(self.y) + ")," + str(self.heuristic) + "||"

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getState(self):
        return self.clean

    def getPath(self):
        return self.path

    def getRoomsCleaned(self):
        return self.roomsCleaned

    def getDirtNumberRemaining(self):
        return self.dirtNumberRemaining

    def getHeuristic(self):
        return self.heuristic
    
    def getRoomsTidy(self):
        return self.roomsTidy

    def getVisitedVerticeList(self):
        return self.visitedVerticeList
