# -*- coding: utf-8 -*-
from Model.Vertice import Vertice
from copy import deepcopy
import time

class Robot:

    def __init__(self, capteur, effecteur, positionX, positionY):
        self.capteur = capteur
        self.effecteur = effecteur
        self.x = positionX
        self.y = positionY
        self.actionList = []
        self.verticeListToCleanState = []
        self.needToRescan = False



    # Observe l'environnement et récupère une copie grâce au capteur
    def ObserveAndUpdate(self):
        self.env = self.capteur.scan()

    # Le robot délibère de la série d'actions à effectuer pour nettoyer le manoir
    def ChooseAnAction(self):
        verticeListToExplore = []  # Liste des états à visiter (File)
        verticeListExplored = []   # Liste des états déjà explorer

        # Noeud de départ ajouté à la file
        path =[]
        path2=[]
        path3=[]

        #path.append((self.x,self.y))
        firstVertice = Vertice(self.x, self.y, path, path2, path3, False, self.env.ManhattanDistance([self.x, self.y]), [],
                                    self.env.InverseManhattanDistance([self.x, self.y]))
                                    
        verticeListToExplore.append(firstVertice)

        
        end = False   # Condition d'arret (état propre trouvé)
        if(self.env.getDirtNumber() == 0):
            return

        # Tant qu'il y a des noeuds à explorer et que la condition d'arret n'est pas atteinte
        while(not(end) and len(verticeListToExplore)>0):
            #print("--\nITERATION\n--")
            # Pop la file pour récupérer le prochain noeud à explorer
            verticeListToExplore.sort(key=lambda myVertices: myVertices.getHeuristic())
            currentVertice = verticeListToExplore.pop(0)
            
           # print("Noeud pop",currentVertice.getX(),currentVertice.getY())

            # Trouver ces voisins
            neighbours = self.addNeighbours(currentVertice,verticeListToExplore, verticeListExplored)

            # Les ajouter à la liste
            for neighbour in neighbours:
                #print("Voisin :",neighbour.getX(),neighbour.getY(),neighbour.getPath(),neighbour.getRoomsCleaned())
                # Vérifier si l'état final est atteint
                #print(self.env.dirtNumber , len(neighbour.getRoomsCleaned()))
                if (self.env.dirtNumber == len(neighbour.getRoomsCleaned())):
                    # Si oui on stoppe la boucle while
                    end = True
                    #print("end")
                    # On sauvegarde le dernier noeud
                    self.finalVertice = neighbour

                else:
                    #print("Added to list")
                    # Si non l'ajouter à la liste des états à explorer
                    verticeListToExplore.append(neighbour)
            verticeListExplored.append(currentVertice)

        # Les premières coordonnées visitées sont celles sur lesquelles débute le robot
        previousCoordinates = (self.x,self.y)

        # On va reconstituer la liste d'action en fonction du chemin vers le noeud final et des salles nettoyées
        
        #print("###")
        #print(finalVertice.getPath())
        print(previousCoordinates)
        print(self.finalVertice.getPath())
        print(self.finalVertice.getRoomsTidy())
        print(self.finalVertice.getRoomsCleaned())

        for roomCoordinates in self.finalVertice.getPath():
            #print(roomCoordinates,previousCoordinates)
    
            if roomCoordinates == (previousCoordinates[0],previousCoordinates[1]):
                isThereJewel = False
                for roomJewelCoordinates in self.finalVertice.getRoomsTidy():
                    if(roomJewelCoordinates == (previousCoordinates[0],previousCoordinates[1])):
                        self.actionList.append("takeObj")
                        isThereJewel = True
                        self.finalVertice.getRoomsTidy().remove(roomJewelCoordinates)
                        break
                if(not(isThereJewel)):
                    self.actionList.append("clean")
            elif roomCoordinates[0] == previousCoordinates[0]-1:
                self.actionList.append("up")
            elif roomCoordinates[0] == previousCoordinates[0]+1:
                self.actionList.append("down")
            elif roomCoordinates[1] == previousCoordinates[1]-1:
                self.actionList.append("left")
            elif roomCoordinates[1] == previousCoordinates[1]+1:
                self.actionList.append("right")

            previousCoordinates = roomCoordinates





    # Fonction pour ajouter les voisins d'une salle
    # +1 voisin si salle sale
    # +x voisin si salle propre, si celles ci ne sont pas visitées dans la branche
    def addNeighbours(self,vertice,verticeListToExplore,verticeListExplored):
        neighbourList = []
        #print("%%",vertice.getRoomsCleaned())

        # On regarde l'état de propreté de la salle
        if self.env.getRoom(vertice.getX(), vertice.getY()).getJewel() and not ((vertice.getX(), vertice.getY()) in vertice.getRoomsTidy()):
            #print("Salle non rangée")
            #print(str(self.env.getRoom(vertice.getX(), vertice.getY()).getJewel()) + " " + str(vertice.getX()) + " " + str(vertice.getY()))
            #print("%%",vertice.getRoomsCleaned())
            # Cas non rangé - on ajoute le noeud suivant avec la salle rangée
            exist = False
            path = deepcopy(vertice.getRoomsCleaned()).append((vertice.getX(),vertice.getY()))
            for verticeExplored in verticeListExplored:
                #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                if (verticeExplored.getX(), verticeExplored.getY()) == (vertice.getX(),vertice.getY()) and verticeExplored.getRoomsCleaned() == path:
                    # noeuds déjà exploré dans cette branche
                    
                    exist=True
                    break
            #print("-")
            for verticeExplored in verticeListToExplore:
                #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                if (verticeExplored.getX(), verticeExplored.getY()) == (vertice.getX(),vertice.getY()) and verticeExplored.getRoomsCleaned() == path:
                    # noeuds déjà exploré dans cette branche
                    
                    exist=True
                    break
            if (exist):
                    #print("noeud existant")
                    pass
                    
                    
            else:
                    #print("%%",vertice.getRoomsCleaned())
                    path = deepcopy(vertice.getPath())
                    path.append((vertice.getX(),vertice.getY()))
                    path2 = deepcopy(vertice.getRoomsCleaned())
                    path3 = deepcopy(vertice.getRoomsTidy())
                    path3.append((vertice.getX(),vertice.getY()))
                    newVertice = Vertice (vertice.getX(),
                                          vertice.getY(),
                                          path,
                                          path2,
                                          path3,
                                          self.env.getRoom(vertice.getX(),vertice.getY()).getDirt(),
                                          self.env.ManhattanDistance([vertice.getX(), vertice.getY()]),
                                          vertice.getTheoricalPerformanceTab(),
                                          self.env.InverseManhattanDistance([vertice.getX(), vertice.getY()])
                                          )
                    neighbourList.append(newVertice)
                    #print("add cleaned")
        elif self.env.getRoom(vertice.getX(), vertice.getY()).getDirt() and not((vertice.getX(),vertice.getY())in vertice.getRoomsCleaned()):
            #print("Salle non propre")
            #print("%%",vertice.getRoomsCleaned())
            # Cas non propre - on ajoute le noeud suivant avec la salle propre
            exist = False
            path = deepcopy(vertice.getRoomsCleaned()).append((vertice.getX(),vertice.getY()))
            for verticeExplored in verticeListExplored:
                #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                if (verticeExplored.getX(), verticeExplored.getY()) == (vertice.getX(),vertice.getY()) and verticeExplored.getRoomsCleaned() == path:
                    # noeuds déjà exploré dans cette branche
                    
                    exist=True
                    break
            #print("-")
            for verticeExplored in verticeListToExplore:
                #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                if (verticeExplored.getX(), verticeExplored.getY()) == (vertice.getX(),vertice.getY()) and verticeExplored.getRoomsCleaned() == path:
                    # noeuds déjà exploré dans cette branche
                    
                    exist=True
                    break
            if (exist):
                    #print("noeud existant")
                    pass
                    
                    
            else:
                self.env.getDirtyRoomsPosition().remove((vertice.getX(), vertice.getY()))
                #print("%%",vertice.getRoomsCleaned())
                path = deepcopy(vertice.getPath())
                path.append((vertice.getX(),vertice.getY()))
                path2 = deepcopy(vertice.getRoomsCleaned())
                path2.append((vertice.getX(),vertice.getY()))
                path3 = deepcopy(vertice.getRoomsTidy())
                newVertice = Vertice (vertice.getX(),
                                      vertice.getY(),
                                      path,
                                      path2,
                                      path3,
                                      False,
                                      self.env.ManhattanDistance([vertice.getX(), vertice.getY()]),
                                      vertice.getTheoricalPerformanceTab(),
                                      self.env.InverseManhattanDistance([vertice.getX(), vertice.getY()])
                                      )
                neighbourList.append(newVertice)
                #print("add cleaned")

        else:
            # Cas propre
            # On récupère les coordonnées des salles adjacentes
            listCoord = self.getNeighbourCoord(vertice.getX(),vertice.getY())

            # On regarde si elles sont déjà parcourues dans cette branche
            #print("Salle propre")
            for coord in listCoord:
                #print("Potentiel voisin",coord[0],coord[1])
                
                exist = False
                for verticeExplored in verticeListExplored:
                    #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                    if (verticeExplored.getX(), verticeExplored.getY()) == coord and verticeExplored.getRoomsCleaned() == vertice.getRoomsCleaned():
                        # noeuds déjà exploré dans cette branche
                        
                        exist=True
                        break
                #print("-")
                for verticeExplored in verticeListToExplore:
                    #print("test",verticeExplored.getX(), verticeExplored.getY(),verticeExplored.getRoomsCleaned(),vertice.getRoomsCleaned())
                    if (verticeExplored.getX(), verticeExplored.getY()) == coord and verticeExplored.getRoomsCleaned() == vertice.getRoomsCleaned():
                        # noeuds déjà exploré dans cette branche
                        
                        exist=True
                        break
                
                if (not(exist)):
                    # Salle non explorée dans cette branche
                    #print("add in neighbourList")
                    path = deepcopy(vertice.getPath())
                    path.append(coord)
                    path2 = deepcopy(vertice.getRoomsCleaned())
                    path3 = deepcopy(vertice.getRoomsTidy())
                    newVertice = Vertice(coord[0],
                                         coord[1],
                                         path,
                                         path2,
                                         path3,
                                         self.env.getRoom(coord[0],coord[1]).getDirt(),
                                         self.env.ManhattanDistance([vertice.getX(), vertice.getY()]),
                                         vertice.getTheoricalPerformanceTab(),
                                         self.env.InverseManhattanDistance([vertice.getX(), vertice.getY()])
                                         )
                    neighbourList.append(newVertice)
                    
        # TODO gérer quand on a tout exploré
        return neighbourList


    #
    # Renvoie les coordonnées des salles voisines en fonction de la position
    #
    def getNeighbourCoord(self,x,y):
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


    def getXPos(self):
        return self.x
    
    def getYPos(self):
        return self.y


    #Return true if difference between performances is too high and rescan is mandatory
    def informRealPerformance(self, performance):
        myPerformance = 0
        for i in range(len(self.finalVertice.getTheoricalPerformanceTab()) - len(self.actionList)):
            myPerformance += self.finalVertice.getTheoricalPerformanceTab()[i]
        if(performance - myPerformance > 15):
            self.needToRescan = True
            print("Ma performance estimée (" + str(myPerformance) + ") est trop loin de ma performance réelle (" + str(performance) + "). Je rescan !")
            return True
        return False

    # Le robot applique les actions contenues dans sa liste d'actions
    def JustDoIt(self):
        print(self.actionList)
        actionIndex = 0
        # Tant que la liste d'action n'est pas vide, effectuer les actions
        while (len(self.actionList) > 0 and not(self.needToRescan)):

            # Pop la file
            currentAction = self.actionList.pop(0)

            # On appelle une méthode de l'effecteur pour mettre à jour la position du robot ou lui ordonner d'aspirer la salle
            self.effecteur.processAction(self, currentAction)
            actionIndex += 1
            time.sleep(1)
        self.needToRescan = False
        self.actionList = []
