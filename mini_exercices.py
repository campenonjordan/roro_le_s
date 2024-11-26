def ajouter_element(ma_liste, element):
    # Ajoute l'élément à ma_liste
    details = input("Ajouter élément : ")
    ma_liste.append(element)
    print(details)
    

# Exemple d'appel de la fonction
details = []
ajouter_element(details, "élément1")
print(details)  # Devrait afficher ["élément1"]