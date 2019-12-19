import placeTest
test = placeTest

tab = (
    "mur(4)",
    "ouverture(porte)",
    "desservi(electricite)",
    "desservi(chauffage)",
    "desservi(gaz)",
    "superficie(9)"
)

test.writeFacts(tab)

print(test.Room())
