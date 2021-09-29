from Model.Room import Room

class Environment :

    def __init__(self):
        self.roomList = []
        self.dirtNumber = 0
        self.jewelNumber = 0

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

    # Renvoie la salle aux coordonnées (x,y)
    def getRoom(self, _x, _y):
        index = _y + 5 * _x
        if(index < 25):
            return self.roomList[index]
        """for room in self.roomList:
            if room.getXPos() == _x and room.getYPos() == _y:
                return room"""


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
    