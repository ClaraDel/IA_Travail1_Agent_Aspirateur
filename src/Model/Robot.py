# -*- coding: utf-8 -*-
from Model.Capteur import Capteur

class Robot:
    
    #Recuperation du 
    def __init__(self, controller):
        self.controller = controller
        self.capteur = Capteur()
        self.capteur.scan(controller).print_env()
        self.env = self.capteur.scan(controller)
        self.x = 0 #
        self.y = 0 # A random
        
        
    def fonction_agent(self): 
        self.env = self.capteur.scan(self.controller)
        while (!self.env.isClean()):    #Achanger pour appeler le monde et savoir si nettoyage est necessaire
            ObserveAnd Update()
            ChooseAnAction()
            
            
    def ObserveAndUpdate(self):
        self.env = self.capteur.scan(controller)
        
        
    def ChooseAnAction(self):
        listAExplorer = []
        listAExplorer.append(self.env)
        end = False
        while(!end && len(listAExplorer)>0): 
            # Pop la file
            # Marquer le noeud
            # Trouver ces voisins
            # Vérifier le marquage de ceux-ci
            # Les ajouter à la liste
            
        
