from Model.Room import Room


class Environment :
    
    def __init__(self):

        self.roomList = []
        self.dirtNumber = 0
        self.jewelNumber = 0

        for i in range(5):
            for j in range(5):
                self.roomList.append(Room(i,j))
    
        #Display the env in console
    def print_env(self):
        for row in self.env:
            for col in row:
                if col.jewel:
                    print("J",end='')
                if col.dirt:
                    print("D",end='')
                if col.aspi:
                    print("A",end='')
                if (not(col.dirt) and not(col.jewel) and not(col.aspi)):
                    print("X",end='')
                print("  ",end='')
            print('')
        print("----------")

    def isClean(self):
        for room in self.roomList:
            if (room.getDirt()):
                return False
        return True

    def getSalle(self, _x, _y):
        for room in self.roomList:
            if room.xPos == _x and room.yPos == _y:
                return room

    def getNeighbor(self, _x, _y):
        neighborList = []

        for room in self.roomList:
            if room.xPos == _x + 1 and room.yPos == _y:
                neighborList.append(room)
            if room.xPos == _x - 1 and room.yPos == _y:
                neighborList.append(room)
            if room.xPos == _x and room.yPos == _y - 1:
                neighborList.append(room)
            if room.xPos == _x and room.yPos == _y + 1:
                neighborList.append(room)

        return neighborList