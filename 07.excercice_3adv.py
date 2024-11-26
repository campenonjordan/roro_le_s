#Contexte : Vous développez une application éducative pour aider les étudiants à pratiquer les tables de multiplication. 
# Votre tâche est de générer et d'afficher la table de multiplication pour un nombre donné.
#Objectif : Demandez à l'utilisateur d'entrer un nombre. 
# Ensuite, utilisez une boucle for pour afficher la table de multiplication de ce nombre (de 1 à 10). 
# Puis, faites la même chose en utilisant une boucle while.

n = int(input("Tapez la valeur à multiplier : "))
print("La table de multiplication de", n,"est :")

for i in range(1,11):
    print(n, "x", i, "=",i*n)
    
i = 1 
while i < 10 :
    print(i, "x", n, "=", i*n)
    i += 1
    #pourquoi i += 1 sinon tourne en boucle sur 2 ? 


