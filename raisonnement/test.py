import placeTest
place = placeTest

tab = (
    "mur(4)",
    "ouverture(porte)",
    "desservi(electricite)",
    "desservi(chauffage)",
    "desservi(gaz)",
    "superficie(9)"
)

place.writeFacts(tab)

print(place.iskitchen())
