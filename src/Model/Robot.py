# -*- coding: utf-8 -*-
from Model.Capteur import Capteur
from Model.Vertice import Vertice
from Model.Effecteur import Effecteur
from Model.Environment import Environment

class Robot:
    
    def __init__(self, capteur, effecteur, positionX, positionY):
        self.capteur = capteur
        self.effecteur = effecteur
        self.x = positionX #
        self.y = positionY # A random
        self.actionList = []
        
        
    def agent_behaviour(self): 
        self.env = self.capteur.scan(self.controller)
        while(not(self.env.isClean())):
            self.ChooseAnAction()


    def ObserveAndUpdate(self):
        self.env = self.capteur.scan()


    # Le robot applique les actions contenues dans sa liste d'actions
    def JustDoIt(self, trueEnvironment):

        # Tant que la liste d'action n'est pas vide, effectuer les actions
        while (len(self.actionList > 0)):

            # Pop la file
            currentAction = self.actionList.pop(0)

            # On appelle une méthode de l'effecteur pour mettre à jour la position du robot ou lui ordonner d'aspirer la salle
            # dans laquelle il se trouve 
            self.x, self.y, toSuckOrNotToSuck = self.effecteur.processAction(self.x, self.y, currentAction)
            
            #Alternative : a voir si fonctionne
            self.effecteur.processAction2(self, currentAction, trueEnvironment)

            # Si jamais il doit aspirer, on set le booléen dirt de la salle dans laquelle se trouve le robot à False
            # On réduit aussi le nombre de poussière dans l'environnement
            if (toSuckOrNotToSuck):
                trueEnvironment.getRoom(self.x,self.y).setDirt(False)
                trueEnvironment.setDirtNumber(trueEnvironment.getDirtNumber()-1)


    # Le robot délibère de la série d'actions à effectuer pour nettoyer le manoir
    def ChooseAnAction(self):
        verticeListToExplore = []
        verticeListExplored = []
        firstVertice = Vertice(self.x, self.y, [(self.x,self.y)], [], False)
        verticeListToExplore.append(firstVertice)
        end = False
        
        while(not(end) and len(verticeListToExplore)>0):
            
            # Pop la file
            currentVertice = verticeListToExplore.pop(0)
            verticeListExplored.append(currentVertice)
            
            # Trouver ces voisins
            neighbours = self.addNeighbours(currentVertice, verticeListExplored)
            
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
                    verticeListToExplore.append(neighbour)

        # Les premières coordonnées visitées sont celles sur lesquelles débute le robot
        previousCoordinates = [self.x,self.y]

        # On va reconstituer la liste d'action en fonction du chemin vers le noeud final et des salles nettoyées
        for roomCoordinates in finalVertice.getPath():

                if roomCoordinates in finalVertice.getRoomsCleaned():
                    self.actionList.append("suck")
                elif roomCoordinates[0] == previousCoordinates[0]-1:
                    self.actionList.append("left")
                elif roomCoordinates[0] == previousCoordinates[0]+1:
                    self.actionList.append("right")
                elif roomCoordinates[1] == previousCoordinates[1]-1:
                    self.actionList.append("up")
                elif roomCoordinates[1] == previousCoordinates[1]+1:
                    self.actionList.append("down")

                previousCoordinates = roomCoordinates
                
            
            
            
            
    # Fonction pour ajouter les voisins d'une salle
    # +1 voisin si salle sale
    # +x voisin si salle propre, si celles ci ne sont pas visitées dans la branche
    def addNeighbours(self,vertice,verticeListExplored):
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
            # On récupère les coordonnées des salles adjacentes
            listCoord = self.getNeighbourCoord(vertice.getX(),vertice.getY())
            # On regarde si elles sont déjà parcourues dans cette branche
            for coord in listCoord:                
                if (coord in vertice.getPath()): 
                    for verticeExplored in verticeListExplored:
                        if ((verticeExplored.getX, verticeExplored.getY) == coord 
                        and verticeExplored.getRoomsCleaned() == vertice.getRoomsCleaned()):
                            # noeuds déjà exploré dans cette branche
                            break                
                else:
                    # Salle non explorée dans cette branche
                    newVertice = Vertice(coord[0],
                                         coord[1],
                                         vertice.getPath.append(coord),
                                         vertice.getRoomsCleaned()
                                         )
                    neighbourList.append(newVertice)
        # TODO gérer quand on a tout exploré
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
            

