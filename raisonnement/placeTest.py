from pyswip import Prolog
import os
import spaceOrRoom
import facts
prolog = Prolog


def writeFacts(tab):
    """
        Writes in the facts.py file the assertions of a place
       
        tab: an array that takes the content of the assertion
    """

    with open("facts.py", "w") as f:
        f.write("from pyswip import Prolog\nprolog = Prolog\n")

        for i in tab:
            f.write("prolog.asserta(\""+i+"\")\n")
    
       

def iskitchen():
    """
       determines if the place is a kitchen according to established rules and based on the facts
       
       Returns two-dimensional table: Saying what makes it a kitchen or not. For example: [piece][true]
    """
