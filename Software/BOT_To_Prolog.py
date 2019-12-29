from pyswip import Prolog
import libPerso
import rules
prolog = Prolog

# Règles
prolog.asserta("interface(X, Y) :- zone(X), zone(Y)") # Définit qu'une interface est possible entre deux zones OU
prolog.asserta("interface(X, Y) :- zone(X), element(Y)") # Définit qu'une interface est possible entre une zone et un élément OU
prolog.asserta("interface(X, Y) :- element(X), zone(Y)") # Définit qu'une interface est possible entre un élément et une zone OU
prolog.asserta("interface(X, Y) :- element(X), element(Y)") # Définit qu'une interface est possible entre deux éléments.

prolog.asserta("hasElement(X, Y) :- zone(X), element(Y)") # Définit qu'une zone peut avoir des éléments, ces éléments seront alors
prolog.asserta("adjacentElement(X, Y) :- zone(X), element(Y), hasElement(X, Y)") # Définit qu'une zone peut posséder des éléments qui la délimite.
prolog.asserta("intersectingElement(X, Y) :- zone(X), element(Y), hasElement(X, Y)") # Définit qu'une zone peut posséder des éléments qui sont présents dans cette zone.

prolog.asserta("adjacentZone(X, Y) :- zone(X), zone(Y)") # Définit qu'une zone X peut posséder une zone Y adjacente.
prolog.asserta("adjacentZone(X, Y) :- adjacentZone(Y, X)") # Si X est adjacente à Y, alors Y est adjacente à X.
prolog.asserta("intersectsZone(X, Y) :- zone(X), zone(Y)") # Définit qu'une zone X peut-être coupée par une zone Y (comme pour un escalier qui "coupe" l'espace d'un étage).
prolog.asserta("intersectsZone(X, Y) :- adjacentZone(Y, X)") # Si une zone X coupe une zone Y, avec la zone Y coupe la zone X.

prolog.asserta("hasSubElement(X, Y) :- element(X), element(Y)") # Définit qu'une élément peut incorporer un autre élément en lui


# Raisonnement
def IsInterface(_item1: str, _item2: str) -> bool:
    """
        Prend 2 noms en paramètres qui correspondent à : une/deux zone(s) ou une/deux élément(s).
        Exemple : une zone avec un mur -> Vrai s'ils sont reliés, faux sinon.
        Return : Vrai s'il y a une interface entre les deux noms, faux sinon ou s'il y a un problème de paramètre
    """

    result: bool = False
    if (libPerso.IsParamString(_item1) and libPerso.IsParamString(_item2)):
        queryList = list(prolog.query("interface({}, {})".format(_item1, _item2))) # Fait la requête dans un sens
        queryList += list(prolog.query("interface({}, {})".format(_item2, _item1))) # Puis dans l'autre comme les deux cas sont possibles.
        if not len(queryList):
            result = False
        else:
            result = True

    return result


def ElementToZoneInfo(_zone: str, _element: str) -> int:
    """
        Donne des informations sur un élément par rapport à une zone donnée.
        Exemple : Zone1 avec élément1 -> -1 Si aucune relation, 1 si l'élément est adjacent à la zone, 2 s'il intersecte la zone.
        Return : -1 Si aucune relation entre les deux ou problème de paramètre, 1 si l'élément est adjacent à la zone, 2 s'il est dans la zone.
    """

    result: int = -1

    if (libPerso.IsParamString(_zone) and libPerso.IsParamString(_element)):
        queryList = list(prolog.query("hasElement({}, {})".format(_zone, _element)))
        if not len(queryList):
            result = -1
        else:
            queryList = list(prolog.query("adjacentElement({}, {})".format(_zone, _element)))  
            if not len(queryList):
                result = 1
            else:    
                result = 2

    return result


def nameOfParentElement(_childElement: str) -> str:
    """
    Renvoie le nom de l'élément le plus "ancien" s'il existe, sinon renvoie une chaîne vide.
    Arguments:
        _childElement {str} -- Le nom de l'élément pour lequel on recherche son ancêtre le plus loin.

    Returns:
        str -- Nom de l'ancêtre le plus loin, chaîne vide si inexistant ou problème de paramètre.
    """

    result: str = ""

    if (libPerso.IsParamString(_childElement)):
        queryList = list(prolog.query("hasSubElement(X, {})".format(_childElement)))
        if not len(queryList):
            result = ""
        else:
            while (not len(queryList)):
                result = queryList[0]
                queryList = list(prolog.query("hasSubElement(X, {})".format(_childElement)))


    return result