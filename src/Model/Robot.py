# -*- coding: utf-8 -*-
from Model.Vertice import Vertice
from copy import deepcopy

class Robot:

    def __init__(self, capteur, effecteur, positionX, positionY):
        self.capteur = capteur
        self.effecteur = effecteur
        self.x = positionX
        self.y = positionY
        self.actionList = []



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

        #path.append((self.x,self.y))
        firstVertice = Vertice(self.x, self.y, path, path2, False, self.env.getDirtNumber())
        verticeListToExplore.append(firstVertice)


        end = False   # Condition d'arret (état propre trouvé)

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
                    finalVertice = neighbour

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
        for roomCoordinates in finalVertice.getPath():
                #print(roomCoordinates,previousCoordinates)

                if roomCoordinates == (previousCoordinates[0],previousCoordinates[1]):
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
        if self.env.getRoom(vertice.getX(), vertice.getY()).getDirt() and not((vertice.getX(),vertice.getY())in vertice.getRoomsCleaned()):
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
                    print("noeud existant")
                    
                    
            else:
                    #print("%%",vertice.getRoomsCleaned())
                    path = deepcopy(vertice.getPath())
                    path.append((vertice.getX(),vertice.getY()))
                    path2 = deepcopy(vertice.getRoomsCleaned())
                    path2.append((vertice.getX(),vertice.getY()))
                    newVertice = Vertice (vertice.getX(),
                                          vertice.getY(),
                                          path,
                                          path2,
                                          False,
                                          vertice.getDirtNumberRemaining()-1)
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
                
                if (exist):
                    print("noeud existant")
                    
                    
                else:
                    # Salle non explorée dans cette branche
                    #print("add in neighbourList")
                    path = deepcopy(vertice.getPath())
                    path.append(coord)
                    path2 = deepcopy(vertice.getRoomsCleaned())
                    newVertice = Vertice(coord[0],
                                         coord[1],
                                         path,
                                         path2,
                                         self.env.getRoom(coord[0],coord[1]).getDirt(),
                                         vertice.getDirtNumberRemaining()
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



     # Le robot applique les actions contenues dans sa liste d'actions
    def JustDoIt(self):
        print(self.actionList)
        # Tant que la liste d'action n'est pas vide, effectuer les actions
        while (len(self.actionList) > 0):

            # Pop la file
            currentAction = self.actionList.pop(0)

            # On appelle une méthode de l'effecteur pour mettre à jour la position du robot ou lui ordonner d'aspirer la salle
            self.effecteur.processAction2(self, currentAction)
