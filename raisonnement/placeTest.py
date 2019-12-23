from pyswip import Prolog
import os
import facts
prolog = Prolog

#rules------------------------------------------------
prolog.asserta("accessible() :- ouverture(X), X == porte") # une ouverture type "porte" ? si vrai il est possible d'accéder au lieu
prolog.asserta("chauffe() :- desservi(X), X == chauffage") # dersservi par le chauffage ? si vrai la piece est chauffe
prolog.asserta("espace() :- mur(X), X == 4, desservi(electricite), accessible()") # 4 murs & acces electricite & accessible ? si vrai c'est un espace
prolog.asserta("piece() :- espace(), chauffe() ,superficie(X), X >= 9") # une piece ? vrai si c'est un espace & surface > 9m2


def Space():
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

def Room():
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

def writeFacts(tab):
    """
        Writes in the facts.py file the assertions of a place
       
        tab: 
            an array that takes the content of the assertion
    """

    with open("facts.py", "w") as f:
        f.write("from pyswip import Prolog\nprolog = Prolog\n")

        for i in tab:
            f.write("prolog.asserta(\""+i+"\")\n")
    
def iskitchen():
    """
       determines if the place is a kitchen according to established rules and based on the facts
       
       Returns Dictionary liste: 
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

    if Room():
        liste['Piece'] = True
        liste["Accessible"] = True
        liste['Chauffage'] = True
    else:
        if len(queryAccessible):
            liste['Accessible'] = True
        if len(queryChauffe):
            liste['Chauffafe'] = True
    if len(queryGaz):
        liste['Gaz'] = True

    return liste

def isOffice():
    """
       determines if the place is an office according to established rules and based on the facts

       Returns two-dimensional table: 

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
    
    if Room():
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