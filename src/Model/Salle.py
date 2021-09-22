from dataclasses import dataclass

@dataclass
class Salle:

    def __init__(self, _x, _y):
        self.jewel = False
        self.poussiere = False
        self.xPos = _x
        self.yPos = _y

    def switchJewelPresence():
        jewel = !jewel
    def switchDirtPresence():
        dirt = !dirt

    def isEmpty():
        if (!jewel and !dirt):
            return True