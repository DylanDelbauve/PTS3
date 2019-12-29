# coding: utf-8

class File_Reader(object):

    """ Classe pour lire un fichier IFC ou BOT et le stocker. """

    def __init__(self, fileName):
        """ Une classe File_Reader par fichier .IFC ou .BOT """
        self._fileName = fileName
        if (self._fileName != ""):
            self.readFile()
    
    def readFile(self):
        """ Lire un fichier IFC/BOT et le stocker en mémoire """
        with open(self._fileName, 'r', encoding='utf-8') as file:
             self._file = file.read()
           
    def get_file(self):
        """ Donne le contenu du fichier """
        return self._file