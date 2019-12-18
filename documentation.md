# Documentation technique P tut S3

## partie raisonnement

### Démarche

Dans la conception du raisonnement, une pièce est considéré comme un espace, cependant, un espace ne peut pas être considéré comme une pièce. En résumé,  les attributs d'un espace sont encapsulés dans ceux d'une pièce.

### Règles utiles au raisonnement 

Pour être un espace le lieu doit :
- être accessible (avoir une porte)
- disposer de 4 murs
- être desservi par un accès à l'électricité

Pour être une pièce le lieu doit :
- être un espace
- avoir un accès au chauffage
- avoir une superficie supérieure à 9 m²


### fonctions

#### Space

```python
Space()
```
##### Utilisation

```python
print(Space())
```

##### Description

Détermine si un lieu est un espace ou non en fonction des différentes règles établies.Il retourne ensuite une chaîne de caractères en fonction du contexte disant si ou oui ou non il s'agit d'un espace.

#### Room

```python
Room()
```
##### Utilisation

```python
print(Room())

```
#### Description

Détermine si un lieu est une pièce ou non en fonction des différentes règles établies. Il retourne ensuite une chaîne de caractères en fonction du contexte disant si ou oui ou non il s'agit d'une pièce.