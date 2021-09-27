# -*- coding: utf-8 -*-
from Model.Vertice import Vertice

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
        firstVertice = Vertice(self.x, self.y, [(self.x,self.y)], [], False)
        verticeListToExplore.append(firstVertice)


        end = False   # Condition d'arret (état propre trouvé)

        # Tant qu'il y a des noeuds à explorer et que la condition d'arret n'est pas atteiente
        while(not(end) and len(verticeListToExplore)>0):

            # Pop la file pour récupérer le prochain noeud à explorer
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
        previousCoordinates = (self.x,self.y)

        # On va reconstituer la liste d'action en fonction du chemin vers le noeud final et des salles nettoyées
        for roomCoordinates in finalVertice.getPath():

                if roomCoordinates in finalVertice.getRoomsCleaned():
                    self.actionList.append("clean")
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

        # On regarde l'état de propreté de la salle
        if self.env.getRoom(vertice.getX(), vertice.getY()).getDirt():
            # Cas non propre - on ajoute le noeud suivant avec la salle propre
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
                        and verticeExplored.getRoomsCleaned().sort() == vertice.getRoomsCleaned().sort()):
                            # noeuds déjà exploré dans cette branche
                            break
                else:
                    # Salle non explorée dans cette branche
                    newVertice = Vertice(coord[0],
                                         coord[1],
                                         vertice.getPath.append(coord),
                                         vertice.getRoomsCleaned(),
                                         self.env.getRoom(coord[0],coord[1]).getDirt()
                                         )
                    neighbourList.append(newVertice)
        # TODO gérer quand on a tout exploré
        return neighbourList


    #
    # Renvoie les coordonnées des salles voisines en fonction de la position
    #
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



     # Le robot applique les actions contenues dans sa liste d'actions
    def JustDoIt(self):

        # Tant que la liste d'action n'est pas vide, effectuer les actions
        while (len(self.actionList > 0)):

            # Pop la file
            currentAction = self.actionList.pop(0)

            # On appelle une méthode de l'effecteur pour mettre à jour la position du robot ou lui ordonner d'aspirer la salle
            self.effecteur.processAction2(self, currentAction)
