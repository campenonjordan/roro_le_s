# Fonction pour afficher le menu principal

def afficher_menu():
    # TODO: Afficher les options disponibles pour l'utilisateur
    print("************************************")
    print("\tMenu progamme sport")
    print("************************************")
    print("Voici les choix possibles : ")
    print("1. Ajouter un excercie.")
    print("2. Voir la liste d'exercies.")
    print("3. Calculer les calories brulees.")
    print("4. Quitter le menu")
 


# Fonction pour ajouter un exercice à la liste
def ajouter_exercice(exercices):
    exercices = input("Entre vos excercies de la façon suivante : Nom exercice-duree en mintes-calories brulee par minutes (ex : pompe-15-12)\t").split("-")
    print("Exercice ajouté : {}\nTemps de l'exercie en minute : {}\nTes calories brulées par minute : {} ".format(exercices[0], exercices[1], exercices[2] ))

    # TODO: Demander à l'utilisateur d'entrer les détails de l'exercice
    # TODO: Ajouter l'exercice à la liste des exercices
    #    
    pass

# Fonction pour afficher la liste des exercices
def afficher_exercices(exercies):
    if len(exercies) == 0 : 
        return "Liste vide" 
    else : 
        return (exercies)
    # TODO: Vérifier si la liste des exercices est vide
    # TODO: Si non, afficher tous les exercices avec leurs détails

    pass

# Fonction pour calculer et afficher le total des calories brûlées
def calculer_calories_brulees(exercices):
    # TODO: Calculer le total des calories brûlées pour tous les exercices
    # TODO: Afficher le résultat total des calories brûlées
    pass

# Fonction principale qui orchestre l'application
def main():
    exercices = []  # Liste pour stocker les exercices
    while True:
        afficher_menu()  # Afficher le menu principal
        choix = int(input("choisissez une option : "))
        if choix == 1:
            ajouter_exercice(list)  # Appeler la fonction pour ajouter un exercice
        elif choix == 2:
            afficher_exercices(list)  # Appeler la fonction pour afficher les exercices
            print(list)
        elif choix == 3:
            calculer_calories_brulees(list)  # Appeler la fonction pour calculer les calories brûlées
        elif choix == 4:
            print("Au revoir!")  # Afficher un message de départ et quitter la boucle
            break
        else:
            print("Choix invalide. Veuillez réessayer.\n")  # Gérer les choix invalides

# Point d'entrée du programme
if __name__ == '__main__':
    main()  # Appeler la fonction principale pour démarrer l'application