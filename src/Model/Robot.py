# -*- coding: utf-8 -*-
from Model.Capteur import Capteur
from Model.Environment import Environment

class Robot:
    
    #Recuperation du 
    def __init__(self, controller):
        self.controller = controller
        self.capteur = Capteur()
        self.env = self.capteur.scan(controller)
        self.x = 0 #
        self.y = 0 # A random
        
        
    def agent_behaviour(self): 
        self.env = self.capteur.scan(self.controller)
        while(not(self.env.isClean())):
            ChooseAnAction()
            
            
    def ObserveAndUpdate(self):
        self.env = self.capteur.scan(controller)
        
        
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
