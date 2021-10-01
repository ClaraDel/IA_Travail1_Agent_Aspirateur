from Model.Room import Room

class Environment :

    def __init__(self):
        self.roomList = []
        self.dirtNumber = 0
        self.jewelNumber = 0
        self.realPerformance = 0
        self.timeSinceLastPerformanceComparison = 0

        # Création des 25 salles
        for i in range(5):
            for j in range(5):
                self.roomList.append(Room(i,j))


    def addDirt(self, index):
        if(not(self.roomList[index].getDirt())):
            self.roomList[index].setDirt(True)
            self.upDirtNumber()
    def addJewel(self, index):
        if(not(self.roomList[index].getJewel())):
            self.roomList[index].setJewel(True)
            self.upJewelNumber()

    def setDirtNumber(self, _dirtNumber):
        self.dirtNumber = _dirtNumber
    def setJewelNumber(self, _jewelNumber):
        self.jewelNumber = _jewelNumber
    def getDirtNumber(self):
        return self.dirtNumber
    def getJewelNumber(self):
        return self.jewelNumber
    def upJewelNumber(self):
        self.jewelNumber+=1
    def downJewelNumber(self):
        self.jewelNumber-=1
    def upDirtNumber(self):
        self.dirtNumber+=1
    def downDirtNumber(self):
        self.dirtNumber-=1
        
    def cleanRoom(self, x, y):
        self.removeDirt(x, y)
        if(self.roomList[5*y+x].getJewel()):
            self.removeJewel(x, y)
            print("Aïe ! Un bijou a été aspiré !")
            self.realPerformance += 10 # On ajoute une grosse pénalité lorsque le robot aspire un bijou
    def removeDirt(self, x, y):
        if(self.roomList[5*y+x].getDirt()):
            self.roomList[5*y+x].setDirt(False)
            self.downDirtNumber()
        else:
            print("Le robot aspire dans le vide !")
    def removeJewel(self, x, y):
        if(self.roomList[5*y+x].getJewel()):
            self.roomList[5*y+x].setJewel(False)
            self.downJewelNumber()
        else:
            print("Le robot essaye de prendre un bijou alors qu'il n'y a rien !")
            
    # Return True si toutes les salles sont propres
    def isClean(self):
        for room in self.roomList:
            if (room.getDirt()):
                return False
        return True


    def setRealPerformance(self, _realPerformance):
        self.realPerformance = _realPerformance

    def getRealPerformance(self):
        return self.realPerformance


    # Renvoie la salle aux coordonnées (x,y)
    def getRoom(self, _x, _y):
        index = _y + 5 * _x
        if(index < 25):
            return self.roomList[index]
        """for room in self.roomList:
            if room.getXPos() == _x and room.getYPos() == _y:
                return room"""

    def getDirtyRoomsPosition(self):
        dirtyRoomsPosition = []
        for room in self.roomList:
            if(room.getDirt()):
                dirtyRoomsPosition.append((room.getXPos(), room.getYPos()))
        return dirtyRoomsPosition

    def resetPerformanceChecking(self):
        self.realPerformance = 0
        self.timeSinceLastPerformanceComparison = 0

    def checkMyPerformance(self, robot):
        self.realPerformance += self.InverseManhattanDistance((robot.getXPos(), robot.getYPos())) + 1 # +1 correspond à l'energie dépensée par le robot
        self.timeSinceLastPerformanceComparison += 1
        if(self.timeSinceLastPerformanceComparison >= 5):
            self.timeSinceLastPerformanceComparison = 0
            if(robot.informRealPerformance(self.realPerformance)):
                self.realPerformance = 0
        
    def InverseManhattanDistance(self, position):
        invManhattan = 0
        for coord in self.getDirtyRoomsPosition():
            # On inverse la distance de manhattan (10 étant le distance max dans un tableau 5*5) pour pénaliser
            # les distance plus proches plutôt que les distances élevées
            invManhattan += 10 - (abs(position[0] - coord[0]) + abs(position[1] - coord[1]))
        return invManhattan
    
    def ManhattanDistance(self, position):
        manhattan = 0
        for coord in self.getDirtyRoomsPosition():
            manhattan += abs(position[0] - coord[0]) + abs(position[1] - coord[1])
        return manhattan


    # Display the env in console
    def print_env(self):
        column = 0
        print("----------")
        for room in self.roomList:
            if (room.getDirt()):
                print("D", end='')
            if (room.getJewel()):
                print("J", end='')
            else:
                print(".",end='')

            print("  ",end='')
            column += 1

            if (column == 5):
                column = 0
                print('')
        print("----------")
    