from tkinter import *
from tkinter.filedialog import askopenfilename
from File_Reader import File_Reader
from IFC_File import IFC_File_Info
from BOTFile import BOTFile
from Logic import Logic
from collections.abc import Iterable

class IFC_Interface_infos(Frame):

    def __init__(self, window, file_reader, itemId, **kwargs):

        Frame.__init__(self, window, width=1000, height=400, **kwargs)
        self.master.title("{} Infos".format(itemId))
        self.pack(fill=BOTH)

        #self._processor = file_reader
        self._processor = Logic(file_reader, itemId)

        self.labelId = Label(self, text="ID : {}".format(itemId))
        self.labelId.pack()

        self.labelItemType = Label(self, text="Type : {}".format(self._processor.getItemType()))
        self.labelItemType.pack()

        self.labelItemOwner= Label(self, text="Owner : {}".format(self._processor.getItemOwner()))
        self.labelItemOwner.pack()

        self.labelItemName= Label(self, text="Name : {}".format(self._processor.getItemCommonName()))
        self.labelItemName.pack()             

        prologResults = self._processor.getSpaceProperty()

        if (isinstance(prologResults, dict)):
            print (prologResults)
            self.lb_problems = Listbox(self, background="darkred", fg="white", width=50, height=20)
            self.lb_problems.pack(side="left")

            self.lb_validateds = Listbox(self, background="Green", fg="white", width=50, height=20)
            self.lb_validateds.pack(side="left")

            for item in prologResults:
                if (prologResults[item]):
                    self.lb_validateds.insert(END, item)
                else:
                    self.lb_problems.insert(END, item)
