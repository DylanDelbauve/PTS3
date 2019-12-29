from pyswip import Prolog
prolog = Prolog()

from File_Reader import File_Reader
from TypesManager import TypesManager
from ProcessorProlog import ProcessorProlog

import re
import csv

class Logic(File_Reader):

    """ Classe pour traiter les données à partir d'un fichier BOT ou IFC """

    def __init__(self, file_reader, itemId):
        """ Créer un Logic à partir d'un objet File_Reader """
        self.File_Reader = file_reader
        self.itemId = itemId.replace('$', '\$')
        self.type = "none"
        self.commonName = "none"
        self.convertIFCToProlog()

    def getItemType(self):
        """ Renvoie le type de l'objet demandé """
        result = re.search(r'IFC(.*?)\(\'{}'.format(self.itemId), self.File_Reader.get_file()).group(1)

        self.type = result

        return result

    def getItemInfosOnLine(self):
        """ Renvoie un tableau sans case vide avec tous les éléments de la ligne contenant l'id de l'objet recherché """
        result = re.search(r'{}\'(.*?)\)\;'.format(self.itemId), self.File_Reader.get_file()).group(1)
        result = re.split(',', result)
        for i in range(len(result)):
            result[i] = result[i].replace("'", "")
        
        for s in result:
            if (s == ''):
                result.remove(s)

        return result

    def getInfosOnLine(self, _start):
        """ Renvoie un tableau sans case vide avec tous les éléments de la ligne contenant _start """
        result = re.search(r'{}(.*?)\)\;'.format(_start), self.File_Reader.get_file()).group(1)
        result = re.split(',', result)
        for i in range(len(result)):
            result[i] = result[i].replace("'", "")
        
        for s in result:
            if (s == ''):
                result.remove(s)

        return result

    def getItemOwner(self):
        """ Renvoie le propriétaire de l'objet demandé """
        result = self.getItemInfosOnLine()[0]
        while ('#' in result):
            tempResult = self.getInfosOnLine(result)[0]
            tempResult = tempResult.split("(",1)[-1]
            if (tempResult == "$"):
                result = self.getInfosOnLine(result)
                for s in result:
                    if (s != '$' and ('#' not in s)):
                        result = s
            else:
                result = tempResult

        return result


    def getItemCommonName(self):
        """ Renvoie le nom commun de l'objet demandé """
        result = self.getItemInfosOnLine()

        for s in result:
            hasChar = False
            for i in range(len(s)):
                if (s[i].isalpha()):
                    hasChar = True
                    break

            if ('#' not in s and hasChar):
                result = s
                break

        self.commonName = result

        return result


    def convertItemToProlog(self):
        """ Sert à convertir la ligne de l'objet sélectionné du fichier IFC en faits Prolog """
        
        result = re.findall(r'IFC(.+)\(\'(.*?)\'\,', self.File_Reader.get_file())
        
        for s in result:
            if ("zone" != s[0].lower() and "building" != s[0].lower() and "space" != s[0].lower()):
                result.remove(s)
            else:
                prolog.asserta("{}(\'{}\')".format(s[0].lower(), s[1].lower()))



    def convertIFCToProlog(self):
        """ Sert à convertir chaque ligne du fichier IFC en faits Prolog """
        
        result = re.findall(r'IFC(.+)\(\'(.*?)\'\,', self.File_Reader.get_file())
        
        for s in result:
            if ("zone" != s[0].lower() and "building" != s[0].lower() and "space" != s[0].lower()):
                result.remove(s)
            else:
                prolog.asserta("{}(\'{}\')".format(s[0].lower(), s[1].lower()))


    def getSpaceProperty(self):
        """ Pour un espace uniquement, renverra un tableau à deux dimensions pour vérifier si cet espace est bien une cuisine par exemple, le tableau aura comme colonne 0 les points qui sont bons, et colonne 1 les points mauvais """

        if ("SPACE" in self.type):
            types = TypesManager.GetTypesEnum("fr")

            typeAccuracy = 0.0
            correctType = ""

            for t in types:
                if (t in self.commonName.capitalize()):
                    # Appelle la fonction associée pour vérifier si l'objet est une cuisine par exemple."""
                    correctType = t
                else:
                    typeAccuracy = 0.0
                    for letter in t:
                        if (letter in self.commonName.capitalize()):
                            typeAccuracy += 100/len(types)

                        if (typeAccuracy > 50.0):
                            correctType = t
                            break
            
            pp = ProcessorProlog()

            prologFacts = (
                "mur(4)",
                "ouverture(porte)",
                "desservi(electricite)",
                "desservi(chauffage)",
                "desservi(gaz)",
                "superficie(9)"               
            )
            pp.writeFacts(prologFacts)
            if (correctType != "Cuisine" and correctType != "Bureau"):
                correctType = "Cuisine"

            return pp.Process(correctType.capitalize())



    