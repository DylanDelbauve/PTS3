from pyswip import Prolog
import os
import facts
prolog = Prolog

#rules------------------------------------------------
prolog.asserta("accessible() :- ouverture(X), X == porte") # une ouverture type "porte" ? si vrai il est possible d'accéder au lieu
prolog.asserta("chauffe() :- desservi(X), X == chauffage") # dersservi par le chauffage ? si vrai la piece est chauffe
prolog.asserta("espace() :- mur(X), X == 4, desservi(electricite), accessible()") # 4 murs & acces electricite & accessible ? si vrai c'est un espace
prolog.asserta("piece() :- espace(), chauffe() ,superficie(X), X >= 9") # une piece ? vrai si c'est un espace & surface > 9m2

class ProcessorProlog(object):

    def Process(self, typeName):
        """ Fonction permettant d'utiliser une fonction adaptée au type demandé, appeler la fonction de vérification d'une cuisine si c'est une cuisine par exemple """

        switcher = {
            "Cuisine" : self.isKitchen,
            "Bureau" : self.isOffice
        }

        func = switcher.get(typeName, lambda: "Impossible de résoudre le nom de la pièce")        
        return func()


    def Space(self):
        """
        determines if the place is a space according to established rules and based on the facts

        Returns:
                bool: Saying whether the place is a space or not.
        """
        out = False
        queryEsp= list(prolog.query("espace()"))
        if len(queryEsp):
            out = True
        return out

    def Room(self):
        """
        determines if the place is a room according to established rules and based on the facts

        Returns:
                bool: Saying whether the place is a room or not.
        """
        out = False
        queryRoom = list(prolog.query("piece()"))
        if len(queryRoom):
            out = True
        return out

    def writeFacts(self, tab):
        """
            Writes in the facts.py file the assertions of a place
        
            tab: 
                an array that takes the content of the assertion
        """
        with open("facts.py", "w") as f:
            f.write("from pyswip import Prolog\nprolog = Prolog\n")

            for i in tab:
                f.write("prolog.asserta(\""+i+"\")\n")
        
    def writeFact(self, item):
        """ Fonction reprise de writeFacts pour écrire non pas un tableau mais simplement un seul fait"""

        with open("facts.py", "w") as f:
            f.write("from pyswip import Prolog\nprolog = Prolog\n")
            f.write("prolog.asserta(\""+item+"\")\n")


    def isKitchen(self):
        """
        determines if the place is a kitchen according to established rules and based on the facts
        
        Returns a Dictionary liste: 
                Saying what makes it a kitchen or not. For example: "piece : True"
        """
        prolog.asserta("gaz() :- desservi(X), X == gaz") # vrai si deservi par le gaz
        queryGaz = list(prolog.query("gaz()"))
        queryAccessible = list(prolog.query("accessible()"))
        queryChauffe = list(prolog.query("chauffe()"))

        liste = {
            "Gaz": False,
            "Piece": False,
            "Accessible": False,
            "Chauffage": False
        }

        if self.Room():
            liste['Piece'] = True
            liste['Accessible'] = True
            liste['Chauffage'] = True
        else:
            if len(queryAccessible):
                liste['Accessible'] = True
            if len(queryChauffe):
                liste['Chauffage'] = True
        if len(queryGaz):
            liste['Gaz'] = True

        return liste

    def isOffice(self):
        """
        determines if the place is an office according to established rules and based on the facts

        Returns a two-dimensional table: 

                Saying what makes it an office or not. For example: [piece][true]
        """
        prolog.asserta("electricite() :- desservi(X), X == electricite") # vrai si deservi par l'électricité
        prolog.asserta("planTravail() :- meuble(X), X == bureau")
        
        queryElectricite = list(prolog.query("electricite()"))
        queryMeuble = list(prolog.query("planTravail()"))
        queryAccessible = list(prolog.query("accessible()"))
        queryChauffe = list(prolog.query("chauffe()"))

        liste = {
            "Electricite": False,
            "Bureau": False,
            "Piece": False,
            "Accessible": False,
            "Chauffage": False
        }
        
        if self.Room():
            liste['Piece'] = True
            liste["Accessible"] = True
            liste['Chauffage'] = True
        else:
            if len(queryAccessible):
                liste['Accessible'] = True
            if len(queryChauffe):
                liste['Chauffage'] = True
        if len(queryElectricite):
            liste['Electricite'] = True
        if len(queryMeuble):
            liste['Bureau'] = True

        return liste