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

#### Space()

```python
Space()
```
##### Utilisation

```python
print(Space())
```

##### Description

Détermine si un lieu est un espace ou non en fonction des différentes règles établies.Il retourne ensuite une chaîne de caractères en fonction du contexte disant si ou oui ou non il s'agit d'un espace.

#### Room()

```python
Room()
```
##### Utilisation

```python
print(Room())

```
##### Description

Détermine si un lieu est une pièce ou non en fonction des différentes règles établies. Il retourne ensuite une chaîne de caractères en fonction du contexte disant si ou oui ou non il s'agit d'une pièce.

#### writeFacts()

```python
writeFacts(tab)
```

##### Utilisation

```python
tab = (
    "mur(4)",
    "ouverture(porte)",
    "desservi(electricite)",
    "desservi(chauffage)",
    "desservi(gaz)",
    "superficie(9)"
)

writeFacts(tab)
```
##### Description

Permets d'écrire les assertions correspondant à un lieu dans un fichier python (facts py) prévu pour.

#### isKitchen(), isOffice()

```python
import placeTest
place = placeTest

print(place.iskitchen()) # OR print(place.isOffice()
```

##### Utilisation

```python
import placeTest
place = placeTest

tab = (
    "mur(4)",
    "ouverture(porte)",
    "desservi(electricite)",
    "desservi(chauffage)",
    "desservi(gaz)",
    "superficie(9)"
) # Or facts for an Office

place.writeFacts(tab)

print(place.iskitchen()) # Or print(place.isOffice()
```

##### Description

Permet de dire si oui ou non il s'agit d'un cuisine (ou d'un burreau). A chaque fois la fonctionn en question retourne un dictionnaire, avec ce qui en fait une cuisine (ou un burreau) ou non. Dans l'exemple d'utilisation ci-dessus, le dictionnaire retourné sera celui ci :
```python
{'Gaz': True, 'Piece': True, 'Accessible': True, 'Chauffage': True}
```
