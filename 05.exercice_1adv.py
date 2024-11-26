#Contexte : Vous travaillez sur une application de gestion financière personnelle qui aide les utilisateurs à suivre leurs dépenses et revenus 
# mensuels. Vous devez calculer la balance mensuelle et déterminer si l'utilisateur est en déficit ou en excédent.

#Objectif : Créez des variables pour représenter le revenu mensuel (revenu) et les dépenses mensuelles (depenses). 
# Calculez la balance mensuelle en soustrayant les dépenses des revenus. 
# Ensuite, affichez le revenu, les dépenses et la balance. 
# Enfin, déterminez si l'utilisateur est en déficit ou en excédent et affichez un message approprié.

salary = int(input("Quel est votre salaire "))
spent = int(input("Quel est le montant de vos dépenses ? "))
balance = (salary-spent) 

print("Votre revenu est de {} €" .format(salary),"et vos dépense de {} €".format(spent),"soit un total restant de {} €" .format(balance))

if balance > 0 :
    print("Vous êtes en positif")

elif balance == 0 :
    print("Vous êtes à zéro")

else : 
    print("Vous êtes en négatif")