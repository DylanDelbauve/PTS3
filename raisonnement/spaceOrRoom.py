from pyswip import Prolog
import facts
prolog = Prolog


#rules------------------------------------------------
prolog.asserta("accesible() :- ouverture(X), X == porte") # une ouverture type "porte" ? si vrai il est possible d'accéder au lieu
prolog.asserta("chauffe() :- desservi(X), X == chauffage") # dersservi par le chauffage ? si vrai la piece est chauffe
prolog.asserta("espace() :- mur(X), X == 4, desservi(electricite), accesible()") # 4 murs & acces electricite & accesible ? si vrai c'est un espace
prolog.asserta("piece() :- espace(), chauffe() ,superficie(X), X >= 9") # une piece ? vrai si c'est un espace & surface > 9m2


def Space():
    """
       determines if the place is a space according to established rules and based on the facts
        Returns:
            string: A string saying whether the place is a space or not.
    """
    out = ""
    queryEsp= list(prolog.query("espace()"))
    if not len(queryEsp):
       out += "Le lieu n'est pas un espace"
    else:
       out += "Le lieu est un espace"
    return out

def Room():
    """
       determines if the place is a room according to established rules and based on the facts
        Returns:
            string: A string saying whether the place is a room or not.
    """
    out = ""
    queryRoom = list(prolog.query("piece()"))
    if not len(queryRoom):
       out += "le lieu n'est pas une piece"
    else:   
       out += "le lieu est une piece"

    return out


print(Space())