#Contexte : Vous développez une application de salutation personnalisée et de calcul simple. 
# Cette application doit être capable de saluer les utilisateurs par leur nom et de réaliser des additions sur demande.

#Objectif : Créez une fonction saluer qui prend un argument nom et affiche "Bonjour, [nom]!". 
# Ensuite, créez une fonction additionner qui prend deux arguments a et b et retourne leur somme. 
# Appelez ces fonctions avec des exemples de votre choix et affichez les résultats pour vérifier leur fonctionnement.

name = input("Quel est ton nom ? ")

print("Bonjour " + name + " !\nQue souhaites tu additionner ?")
a = int(input("Première valeur "))
b = int(input("Deuxième valeur "))
s = (a+b)
print("La somme de {}" .format(a) + " + {}" .format(b) + " est {}" .format(s))

