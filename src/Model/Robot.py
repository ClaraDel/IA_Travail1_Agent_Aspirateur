# -*- coding: utf-8 -*-

class Robot:
    # Capteur
    # Effecteur
    # Environnement
    
    def __init__(self, controller):
        #self.capteur = Capteur(environnement)
        controller.getEnv().print_env()