from pyswip import Prolog
prolog = Prolog

#cusine
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("ouverture(fenetre)") # il y a une fenetre
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("desservi(gaz)") # il y a un un acces au gaz
prolog.asserta("superficie(9)") # La supérficie du lieu en m2