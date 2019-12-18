# Documentation technique P tut S3

## partie raisonnement

### Démarche

Dans la conception du raisonnement, une pièce est considérer comme un espace, cependant, un espace ne peut pas être considérer comme un pièce. En résumé,  les attributs d'un espace sont encapsulés dans ceux d'une pièce.

### Règles utiles au raisonnement 

Pour être un espace le lieu doit :

- être accessible (avoir une porte)
- disposer de 4 murs
- être desservi par un accès à l'électricité

Pour être une pièce le lieu doit :

- être un espace
- avoir un accès au chauffage
- avoir une supérficie supérieur à 9m²


### fonctions

#### Space

```python
Space()
```
##### Utilisation :

```python
print(Space())
```

##### Description :

Détermine si un lieu est un espace ou non en fonction des différentes règles établies.
Il retourne ensuite une chaîne de caractère en fonction du contexte disant si ou oui ou
non il s'agit d'un espace.

#### Room

```python
Room()
```
##### Utilisation :

```python
print(Room())

```
#### Description :

Détermine si un lieu est une pièce ou non en fonction des différentes règles établies.
Il retourne ensuite une chaîne de caractère en fonction du contexte disant si ou oui ou
non il s'agit d'une piece.