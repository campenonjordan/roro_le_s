#Contexte : Vous développez un programme de gestion de contacts. 
# Ce programme doit pouvoir ajouter des contacts, afficher la liste des contacts et rechercher un contact par nom.

#Objectif : Créez une fonction ajouter_contact qui prend un dictionnaire de contacts et les informations d'un nouveau contact (nom, téléphone) 
# et ajoute ce contact au dictionnaire. 
# Créez une fonction afficher_contacts qui affiche tous les contacts dans le dictionnaire. 
# Enfin, créez une fonction rechercher_contact qui prend le dictionnaire de contacts et un nom, puis affiche les informations du contact 
# si celui-ci existe. Testez ces fonctions en ajoutant quelques contacts, en les affichant et en effectuant une recherche.

personne = {'nom': 'Alice', 'num': '+3312345678'}

for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

personne["profession"] = "Ingénieur"
print(personne)



