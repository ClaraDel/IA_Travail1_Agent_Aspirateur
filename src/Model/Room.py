from dataclasses import dataclass

@dataclass
class Room:

    def __init__(self, _x, _y):
        self.jewel = False
        self.dirt = False
        self.xPos = _x
        self.yPos = _y

    def setJewel(self, _jewel):
        self.jewel = _jewel
    def setDirt(self, _dirt):
        self.dirt = _dirt

    def getJewel(self):
        return self.jewel
    def getDirt(self):
        return self.dirt
    def getXPos(self):
        return self.xPos
    def getYPos(self):
        return self.yPos