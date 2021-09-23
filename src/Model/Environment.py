from Model.Room import Room
import threading
import time
import random


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
        column = 0
        print("----------")
        for room in self.room:

            if (room.getDirt()):
                print("D", end='')
            if (room.getJewel()):
                print("J", end='')
            else:
                print("X",end='')

            print("  ",end='')
            column += 1

            if (column == 5):
                column = 0
                print('')
        print("----------")

    def isClean(self):
        for room in self.roomList:
            if (room.getDirt()):
                return False
        return True

    def getSalle(self, _x, _y):
        for room in self.roomList:
            if room.getXPos() == _x and room.getYPos() == _y:
                return room

    def getNeighbor(self, _x, _y):
        neighborList = []

        for room in self.roomList:
            if room.getXPos() == _x + 1 and room.getYPos() == _y:
                neighborList.append(room)
            if room.getXPos() == _x - 1 and room.getYPos() == _y:
                neighborList.append(room)
            if room.getXPos() == _x and room.getYPos() == _y - 1:
                neighborList.append(room)
            if room.getXPos() == _x and room.getYPos() == _y + 1:
                neighborList.append(room)

        return neighborList