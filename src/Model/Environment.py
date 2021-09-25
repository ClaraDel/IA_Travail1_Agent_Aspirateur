from Model.Room import Room

class Environment :

    def __init__(self):

        self.roomList = []
        self.dirtNumber = 0
        self.jewelNumber = 0

        for i in range(5):
            for j in range(5):
                self.roomList.append(Room(i,j))


    def setDirtNumber(self, _dirtNumber):
        self.dirtNumber = _dirtNumber
    def setJewelNumber(self, _jewelNumber):
        self.jewelNumber = _jewelNumber
    def getDirtNumber(self):
        return self.dirtNumber
    def getJewelNumber(self):
        return self.jewelNumber
        

    def isClean(self):
        for room in self.roomList:
            if (room.getDirt()):
                return False
        return True


    def getRoom(self, _x, _y):
        for room in self.roomList:
            if room.getXPos() == _x and room.getYPos() == _y:
                return room


    #Display the env in console
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
    