# coding: utf-8

# Import regex
import re
from File_Reader import File_Reader

class BOTFile(File_Reader):
    """ Class which allow to extract information from a BOTFile """

    def __init__(self, fileName):
        """ Create BOTFile from File_Reader object """
        File_Reader.__init__(self, fileName)

    def __dir__(self):
        return ["get_nbSite", "get_nbBuilding", "get_nbStorey", "get_nbSpace", "get_infoSite", "get_infoBuilding", "get_infoStorey", "get_infoSpace"]

    def get_nbStorey(self):
        """ Return the number of the different instance of IfcBuildingStorey present in the BOT file """
        list = re.findall('IfcBuildingStorey_', File_Reader.get_file(self))
        nb = int(len(list)/2)
        return nb

    def get_nbSpace(self):
        """ Return the number of the different instance of IfcSpace present in the BOT file """
        list = re.findall("IfcSpace_", File_Reader.get_file(self))
        nb = int(len(list)/2)
        return nb

    def get_infoSpace(self):
        """ Return the IfcSpace IDs present in the BOT file """
        listIDs = re.findall(r'(?<=IfcSpace_)\w+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs;

    def get_infoStorey(self):
        """ Return the IfcBuildingStorey IDs present in the BOT file """
        listIDs = re.findall(r'(?<=IfcBuildingStorey_)\w+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs;

    def get_nbBuilding(self):
        """ Return the number of the different instance of IfcBuilding present in the BOT file """
        list = re.findall("IfcBuilding_", File_Reader.get_file(self))
        nb = int(len(list)/2)
        return nb

    def get_infoBuilding(self):
        """ Return the IfcBuilding IDs present in the BOT file """
        listIDs = re.findall(r'(?<=IfcBuilding_)\w+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs;

    def get_nbSite(self):
        """ Return the number of the different instance of IfcSite present in the BOT file """
        list = re.findall("IfcSite_", File_Reader.get_file(self))
        nb = len(list)
        return nb

    def get_infoSite(self):
        """ Return the IfcSite IDs present in the BOT file """
        listIDs = re.findall(r'(?<=IfcSite_)\w+', File_Reader.get_file(self))
        for i in listIDs:
            while listIDs.count(i) > 1:
                listIDs.remove(i)
        return listIDs;

# __main__


