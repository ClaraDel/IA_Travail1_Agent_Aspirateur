# -*- coding: utf-8 -*-
from Model.Capteur import Capteur
from Model.Vertice import Vertice

class Robot:
    
    def __init__(self, capteur, positionX, positionY):
        self.capteur = capteur
        self.positionX = positionX #
        self.positionY = positionY # A random
        
    def agent_behaviour(self): 
        self.env = self.capteur.scan(self.controller)
        while(not(self.env.isClean())):
            self.ChooseAnAction()

    def ObserveAndUpdate(self):
        self.env = self.capteur.scan()

    def ChooseAnAction(self):
        verticeList = []
        firstVertice = Vertice(self.x, self.y, [(self.x,self.y)], [], False)
        verticeList.append(firstVertice)
        end = False
        
        while(not(end) and len(verticeList)>0):
            
            # Pop la file
            currentVertice = verticeList.pop(0)
            
            # Trouver ces voisins
            neighbours = self.addNeighbours(currentVertice,verticeList)
            
            # Les ajouter à la liste

            for neighbour in neighbours:
                # Vérifier si l'état final est atteint
                if (self.env.dirtNumber == len(neighbour.getRoomsCleaned())):
                    # Si oui on stoppe la boucle while
                    end = True
                    # On sauvegarde le dernier noeud
                    finalVertice = neighbour 
                    
                else:
                    # Si non l'ajouter à la liste des états à explorer
                    verticeList.append(neighbour)
        return finalVertice
            
            
            
            
    # Fonction pour ajouter les voisins d'une salle
    # +1 voisin si salle sale
    # +x voisin si salle propre, si celles ci ne sont pas visitées dans la branche
    def addNeighbours(self,vertice,verticeList):
        neighbourList = []
        if self.env.getRoom(vertice.getX(), vertice.getY()).getDirt():
            # Cas non propre
            newVertice = Vertice (vertice.getX(),
                                  vertice.getY(),
                                  vertice.getPath(),
                                  vertice.getRoomsCleaned.append((vertice.getX(),vertice.getY())),
                                  True)
            neighbourList.append(newVertice)
        else:
            # Cas propre
            # On récupère ls coordonnées des salles adjacentes
            listCoord = self.getNeighbourCoord(vertice.getX(),vertice.getY())
            # On regarde si elles sont déjà parcourues dans cette branche
            for coord in listCoord:
                if coord in verticeList:
                    # Salle déjà explorée dans cette branche
                    break
                else:
                    # Salle non explorée dans cette branche
                    newVertice = Vertice(coord[0],
                                         coord[1],
                                         vertice.getPath.append(coord),
                                         vertice.getRoomsCleaned()
                                         )
                    neighbourList.append(newVertice)
        return neighbourList
                    
            
            
    def getNeighbourCoord(x,y):
        if x==0:
            if y==0:
                return [(x+1,y), (x,y+1)]
            elif y==4:
                return [(x+1,y), (x, y-1)]
            else:
                return [(x+1,y), (x, y-1), (x,y+1)]
        elif x==4:
            if y==0:
                return [(x-1,y), (x,y+1)]
            elif y==4:
                return [(x-1,y), (x, y-1)]
            else:
                return [(x-1,y), (x, y-1), (x,y+1)]
        else :
            if y==0:
                return [(x-1,y), (x+1,y), (x,y+1)]
            elif y==4:
                return [(x-1,y), (x+1,y), (x, y-1)]
            else:
                return [(x-1,y), (x+1,y), (x, y-1), (x,y+1)]
            

