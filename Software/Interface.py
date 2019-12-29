from tkinter import *
from tkinter.filedialog import askopenfilename
from File_Reader import File_Reader
from IFC_File import IFC_File_Info
from BOTFile import BOTFile
from collections.abc import Iterable

from IFC_Interface_infos import IFC_Interface_infos
from BOT_InfoInterface import BOT_InfoInterface 

import os


class Interface(Frame):

    def __init__(self, window, **kwargs):

        Frame.__init__(self, window, width=1000, height=400, **kwargs)
        self.master.title("BOT/IFC Infos")
        self.pack(fill=BOTH)
        
        self._processor = File_Reader("")

        self.filePath = StringVar()

        self._buttonOpenFile = Button(self, text="Open File...", command=self.openFile, width=10, height=1, bg="darkgray", fg="black", activebackground="lightgray")
        self._buttonOpenFile.pack(side="bottom")

        self.lb_functions = Listbox(self, width=50, height=20)
        self.lb_functions.pack(side="left")
        self.lb_functions.bind('<Double-Button>', lambda x: self.process())

        self.lb_results = Listbox(self, width=50, height=20)
        self.lb_results.pack(side="left")
        self.lb_results.bind('<Double-Button>', lambda x: self.createInfoWindow())


    def process(self):
        """ Fonction pour obtenir toutes les fonctions disponibles par le processeur """
        if (len(self.lb_functions.curselection()) > 0):
            index = int(self.lb_functions.curselection()[0])
            value = self.lb_functions.get(index)
            if (value != ""):
                self.lb_results.delete(0, "end")
                results = getattr(self._processor, value) ()
                if isinstance(results, Iterable) and not isinstance(results, str):
                    for result in getattr(self._processor, value) ():
                        self.lb_results.insert(END, result)
                else:
                    self.lb_results.insert(END, results)


    def openFile(self):
        """ Fonction pour ouvrir un fichier et choisir un processeur selon son type """
        self.filePath = askopenfilename(filetypes =(("BOT File", "*.bot"),("IFC File","*.ifc")),
                           title = "Choose a BOT or IFC file.") 
        if (self.filePath != ""):
            self.lb_results.delete(0, "end")
            if (self.filePath.split(".")[-1] == "bot"):
                self._processor = BOTFile(self.filePath)
                self.lb_functions.delete(0, "end")
            else:
                if (self.filePath.split(".")[-1] == "ifc"):
                    self._processor = IFC_File_Info(self.filePath)
                    self.lb_functions.delete(0, "end")
        
            for s in self._processor.__dir__():
                self.lb_functions.insert(END, s)


    def createInfoWindow(self):
        """ Create a subwindow BOT_InfoInterface if the user work on a BOT file and double click on an Ifc ID or an IFC_InfoInterface if he's working on an IFC file"""
        if (len(self.lb_results.curselection()) > 0):
            index = int(self.lb_results.curselection()[0])
            value = self.lb_results.get(index)
            if (isinstance(value, str) and value != ""):
                if self.filePath.split(".")[-1] == "ifc":
                    infoWindow = Tk()
                    interface_infos = IFC_Interface_infos(infoWindow, self._processor, value)
                    interface_infos.mainloop()
                else:
                    if self.filePath.split(".")[-1] == "bot":
                        subwindow = Tk()
                        infoInterface = BOT_InfoInterface(subwindow, value)
                        subwindow.mainloop() 



# __main__
window = Tk()
interface = Interface(window)
interface.mainloop()