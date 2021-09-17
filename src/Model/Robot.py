# -*- coding: utf-8 -*-
from Model.Capteur import Capteur

class Robot:
    # Capteur
    # Effecteur
    # Environnement
    
    def __init__(self, controller):
        self.capteur = Capteur()
        self.capteur.scan(controller).print_env()