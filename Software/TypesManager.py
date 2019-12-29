class TypesManager():

    @staticmethod
    def GetTypesEnum(language):
        """ Renvoie une liste contenant les noms des pièces selon la langue choisie """
        switcher = {
            "fr":lambda: ["Cuisine", "Buanderie", "Cellier", "Cave", "Bureau", "Chambre", "Entree", "Mezzanine", "Escaliers", "Wc"],
            "en":lambda: ["Kitchen", "Washroom", "Cellar", "Cave", "Office", "Bedroom", "Hall", "Mezzanine", "Stairs", "Wc"]
        }

        func = switcher.get(language, "Langue invalide.")
        return func()
