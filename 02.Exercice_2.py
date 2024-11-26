'''Exercice_2
Contexte : Vous développez un programme qui aide les utilisateurs à comprendre la nature des nombres qu'ils saisissent. 
Ce programme doit informer l'utilisateur si le nombre qu'il entre est positif, négatif ou égal à zéro.
Objectif : Écrivez un programme qui demande à l'utilisateur d'entrer un nombre. 
Ensuite, utilisez des structures conditionnelles pour vérifier si le nombre est positif, négatif ou zéro, et affichez un message correspondant à chaque cas.'''

number = int(input("Entrez votre nombre "))

if number > 0 :
    print("Nombre positif")

elif number == 0 :
    print ("Zéro")

else :
    print ("Nombre négatif") 
