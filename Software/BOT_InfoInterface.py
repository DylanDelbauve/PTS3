# coding: utf-8

# Import regex
import re

from tkinter import *
from tkinter.filedialog import askopenfilename
from File_Reader import File_Reader
from IFC_Interface_infos import IFC_Interface_infos

class BOT_InfoInterface(Frame):
    """ Tkinter class in which the user can open an IFC file from a BOT Ifc ID and see the corresponding infos """

    def __init__(self, window, value, **kwargs):
        """ Initialize the components of the window """
        Frame.__init__(self, window, width=1000, height=400, **kwargs) 
        self.pack(fill=BOTH)
        self.kwargs = kwargs
        self.ifcPath = ""
        self.ifcName = value
        self.master.title(self.ifcName + " infos")

        self.lb_results = Listbox(self, width=50, height=20)
        self.lb_results.pack(side="top")

        self.buttonOpenFile = Button(self, text="Open associated IFC file...", command=self.openIfcFile, width=20, height=1, bg="darkgray", fg="black", activebackground="lightgray")
        self.buttonOpenFile.pack(side="bottom")

    def process(self):
        """ Find the infos of the Ifc ID """
        self._processor = File_Reader(self.ifcPath)
        list = re.findall(r'(?<=%s).+' % self.ifcName, self._processor.get_file())
        
        if list[0] != "":
            list = re.split(',', list[0])
        
        fin = len(list)
        i = 1
        
        while i < fin:
            if i == fin-1:
                temp = re.split('\);', list[i])
                list[i] = temp[0]
            elif i < fin-2:
                if '(' in list[i]:
                    while not ')' in list[i+1]:
                        list[i] += ", "+list[i+1]
                        fin -= 1
                        del(list[i+1])
                    list[i] += ", "+list[i+1]
                    fin -= 1
                    del(list[i+1])
            self.lb_results.insert(END, list[i])
            i += 1

    def openIfcFile(self):
       """ Only open an Ifc File and run the process function """
       self.ifcPath = askopenfilename(filetypes = [("IFC File","*.ifc")],
                      title = "Choose the corresponding IFC file.") 

       if (self.ifcPath != ""):
           self.process()
           infoWindow = Tk()
           interface_infos = IFC_Interface_infos(infoWindow, self._processor, self.ifcName)
           interface_infos.mainloop()


