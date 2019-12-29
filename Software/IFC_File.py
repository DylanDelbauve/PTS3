# coding: utf-8

# Import regex
import re
from File_Reader import File_Reader

class IFC_File_Info(File_Reader):
    """ Classe similaire à BOTFileInfo, pour obtenir des informations à partir d'un fichier IFC. """

    def __init__(self, fileName):
        """ Créer un IFCFileInfo à partir d'un objet File_Reader """
        File_Reader.__init__(self, fileName)

    def __dir__(self):
        return ["get_ISO", "get_nbStorey", "get_nbSpaces", "get_nbWalls", "get_infoSpaces", "get_infoWalls", "get_nbZones", "get_infoZones"]

    def get_ISO(self):
        """ Return the ISO standard of the file """
        ISO = re.findall(r'(?<=ISO-)\w+-+\w+', File_Reader.get_file(self))
        return "ISO-"+ISO[0]     

    def get_nbStorey(self):
        """ Donne le nombre d'étages du fichier """
        if (File_Reader.get_file(self) is None):
            File_Reader.readFile(self)
        listStorey = re.findall('IFCBUILDINGSTOREY', File_Reader.get_file(self))
        result = len(listStorey)
        return result


    def get_nbSpaces(self):
        """ Donne le nombre d'espaces du fichier (inclut les étages) """
        if (File_Reader.get_file(self) is None):
            File_Reader.readFile(self)
        listSpace = re.findall('IFCSPACE', File_Reader.get_file(self))
        result = len(listSpace)
        return result

    def get_infoSpaces(self):
        """Renvoie tous les IDs des espaces du fichier IFC """
        listIDs = re.findall(r'(?<=IFCSPACE\(\')+[a-zA-Z0-9_$]+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs


    def get_nbWalls(self):
        """ Donne le nombre de murs du fichier """
        if (File_Reader.get_file(self) is None):
            File_Reader.readFile(self)
        listSpace = re.findall('IFCWALL', File_Reader.get_file(self))
        result = len(listSpace)
        return result

    def get_infoWalls(self):
        """ Renvoie tous les IDs des murs du fichier IFC """
        listIDs = re.findall(r'(?<=IFCWALLSTANDARDCASE\(\')+[a-zA-Z0-9_$]+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs

    def get_nbZones(self):
        """ Donne le nombre de zones du fichier """
        if (File_Reader.get_file(self) is None):
            File_Reader.readFile(self)
        listSpace = re.findall('IFCZONE', File_Reader.get_file(self))
        result = len(listSpace)
        return result

    def get_infoZones(self):
        """ Renvoie tous les IDs des zones du fichier IFC """
        listIDs = re.findall(r'(?<=IFCZONE\(\')+[a-zA-Z0-9_$]+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs       

# __main__
