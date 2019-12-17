from pyswip import Prolog
prolog = Prolog

prolog.asserta("libelle(cellier)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("superficie(9)") # La supérficie du lieu en m2