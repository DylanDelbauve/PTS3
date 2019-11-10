from pyswip import Prolog
prolog = Prolog

#faits ------------------------------------------------

#cusine
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("ouverture(fenetre)") # il y a une fenetre
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("desservi(gaz)") # il y a un un acces au gaz
prolog.asserta("superficie(9)") # La supérficie du lieu en m2

#buandrie
prolog.asserta("libelle(buandrie)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("desservi(eau)") # il y a un un acces a l'eau
prolog.asserta("superficie(9)") # La supérficie du lieu en m2

#cellier
prolog.asserta("libelle(cellier)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("superficie(9)") # La supérficie du lieu en m2

#cave
prolog.asserta("libelle(cave)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("superficie(9)") # La supérficie du lieu en m2
prolog.asserta("emplacement(sous-sol)") # se situe au sous-sol

#bureau
prolog.asserta("libelle(bureau)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("superficie(9)") # La supérficie du lieu en m2
prolog.asserta("meuble(bureau)") #presence d'un meuble bureau

#chambre
prolog.asserta("libelle(chammbre)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("superficie(9)") # La supérficie du lieu en m2
prolog.asserta("meuble(lit)") #presence d'un meuble lit

#couloir
prolog.asserta("libelle(couloir)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("longeur(8)") # longeur en metre
prolog.asserta("largeur(2)") #largeur en metre

#entree / vestibule
prolog.asserta("libelle(entre / vestibule)") # nom du lieu
prolog.asserta("mur(4)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("desservi(chauffage)") # il y a un acces au chauffage
prolog.asserta("superficie(9)") # La supérficie du lieu en m2

#mezzanine
prolog.asserta("libelle(entre / vestibule)") # nom du lieu
prolog.asserta("mur(2)") # nombre de mur
prolog.asserta("ouverture(porte)") # il y a une porte
prolog.asserta("desservi(electricite)") # il y a un acces a l'electricite
prolog.asserta("superficie(9)") # La supérficie du lieu en m2
prolog.asserta("dispose(barriere)") # dispose d'une barriere