# Ptut S3

## Introduction

Ce projet permet dans une démarche ontologique, à partir de fichiers IFC, d'avoir un raisonnement de topologie sémantique. Le programme devrait à terme être capable à partir d'un fichier IFC
d'interpréter les informations du ficher de norme IFC pour en tirer un raisonnement.

## Dépendances

- Un environnement prolog (SWIProlog de préférence) (https://www.swi-prolog.org/)
- Python3
- La librairie Python PySwip (https://pypi.org/project/pyswip/)

## Quick start

Dans un fichier ou dans l'interpréteur python directement :

```python
import spaceOrRoom
print(Space()) 
```

Donne, en l'occurrence : 
```
Le lieu est un espace
```
## Notes

Il s'agit avant tout d'un projet scolaire de découverte, il n'est pas terminé, il dispose à l'heure actuelle :

- D'une base de connaissances de différents espaces et pièces ;
- D'une interface graphique permettant de recueillir des informations dans un fichier IFC ; 
- de quelques fonctions de démonstrations de raisonnement possible.


### Raisonnement 

La partie raisonnement fonctionne pour l'instant de la manière suivante :

- un fichier python (**facts py**) contient un ensemble de fait sur une pièce ;
- le fichier **SpaceOrRoom lui contient un ensemble de règles Prolog ; 
- enfin les fonctions appelées, appliquent les règles aux faits et retournent à l'utilisateur le résultat.

