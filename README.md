# Ptut S3

## Introduction

Il s'agit foncièrement d'une IA capable à partir d'un fichier IFC d'en interpréter les informations pour réaliser un raisonnement logique en fonction d'un ensemble de règles définies.

À terme, *via* un système de chat bot, L'IA devrait être capable de converser en posant des questions à l'utilisateur pour au final proposer une solution d'agencement de l'espace et ce dans le respect de normes diverses, de l'ontologie et de la topologie sémantique inhérent à un bâtiment.

## Dépendances

- Un environnement prolog (https://www.swi-prolog.org/)
- Python3 (https://www.python.org/download/releases/3.0/)
- La librairie Python PySwip (https://pypi.org/project/pyswip/)

## Quick start

### Pour tester la partie raisonnement : 

Dans un fichier ou dans l'interpréteur python directement insérer comme suit 

```python
import spaceOrRoom
print(Space()) 
```

Qui devrait donner en l'occurrence : 
```
Le lieu est un espace
```
## Notes

Il s'agit avant tout d'un projet scolaire de découverte, il n'est pas terminé, il dispose à l'heure actuelle :

- D'une base de connaissances ;
- D'une interface graphique permettant de recueillir des informations dans un fichier IFC ; 
- de quelques fonctions de démonstrations de raisonnement possible.

### Base de connaissances

Il s'agit d'un ensemble de faits sur des pièces et espaces avec leurs attributs propres. Cette base de connaissances n'a pas été créer dans une démarche de respect des normes etc. Mais plutôt dans le cadre d'une réflexion ouverte de ce qui constitue pour nous, à notre niveau et avec notre subjectivité propre, une pièce en elle-même ou par rapport à une autre. Il en va de même pour la définition même de pièce et espace.

### Raisonnement 

La partie raisonnement fonctionne pour l'instant de la manière suivante :

- un fichier python (**facts py**) contient un ensemble de fait sur une pièce ;
- le fichier **SpaceOrRoom lui contient un ensemble de règles Prolog ; 
- enfin les fonctions appelées, appliquent les règles aux faits et retournent à l'utilisateur le résultat.

