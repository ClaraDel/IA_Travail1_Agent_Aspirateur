# -*- coding: utf-8 -*-
from Model.Capteur import Capteur

class Robot:
    # Capteur
    # Effecteur
    # Environnement
    
    def __init__(self, controller):
        self.capteur = Capteur()
        self.capteur.scan(controller).print_env()
        self.env = self.capteur.scan(controller)
        self.actionPlan = []

    def ChooseAnAction(actionChoisie): # classe Salle à implémenter

        if (CheckGoalNode()):
            return actionPlan

        else:

            sallesAExplorer = []
            sallesAExplorer.append(getSalle(xRobot, yRobot))

            while(!CheckGoalNode()):
                salleCourante = sallesAExplorer[0]
                salleCourante.dejaExploree = True # implémenter un attribut booléen permettant de dire si la salle a déjà été explorée

                if (salleCourante.bijouxPresent): # implémenter ces 4 attributs
                    salleCourante.bijouxAttrape = True
                    salleCourante.bijouxPresent = False

                if (salleCourante.poussierePresente):
                    salleCourante.poussiereAttrapee = True
                    salleCourante.poussierePresente = False

                for salleVoisines in salleCourante.getSallesVoisines(): # implémenter cette méthode
                    sallesAExplorer.append(salleVoisines)

                sallesAExplorer.pop(0)




    def CheckGoalNode(): # A CHANGERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        goalReached = True
        for i in range(5):
            for j in range(5):
                if (env[i][j].jew or env[i][j].dirt):
                    contientPoussiereOuBijoux = False
        return contientPoussiereOuBijoux