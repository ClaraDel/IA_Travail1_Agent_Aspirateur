# -*- coding: utf-8 -*-
from Model.Capteur import Capteur
from Model.Environment import Environment
from Model.Vertice import Vertice
import time

class Robot:
    
    #Recuperation du 
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
        firstVertice = Vertice(self.x, self.y, [], [])
        verticeList.append(firstVertice)
        end = False
        while(not(end) and len(verticeList)>0): 
            # Pop la file
            # Marquer le noeud
            # Trouver ces voisins
            # Vérifier le marquage de ceux-ci
            # Les ajouter à la liste
            print("temp")
            
