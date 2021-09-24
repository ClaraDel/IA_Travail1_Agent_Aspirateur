
class Vertice:

    def __init__(self,roomX, roomY,listRooms, roomsCleaned, roomState):
        # Coordonnées de la salle
        self.x = roomX
        self.y = roomY
        # Etat propre ou salle
        self.clean = roomState
        # List des salles visitées pour arriver dans cette salle (=chemin de la branche)
        self.path = listRooms
        # Liste des salles nettoyées sur le chamin ci dessus (donc dans la branche)
        self.roomsCleaned = roomsCleaned

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
