'''Projet : Gestion des Entraînements en Salle de Sport
Contexte : Vous êtes chargé de développer une application simple pour aider les utilisateurs à suivre leurs séances d'entraînement en salle de sport. L'application permettra aux utilisateurs d'ajouter de nouveaux exercices, de voir la liste des exercices qu'ils ont effectués, et de calculer le total des calories brûlées pendant une séance.

Objectifs :

Créer un menu principal pour naviguer entre les différentes fonctionnalités de l'application.
Ajouter des exercices à la liste avec des informations telles que le nom de l'exercice, la durée (en minutes), et les calories brûlées par minute.
Afficher la liste des exercices effectués.
Calculer le total des calories brûlées pendant une séance d'entraînement.
Fonctionnalités et Implémentation
1. Menu Principal
Le menu principal permettra aux utilisateurs de choisir entre ajouter un exercice, voir la liste des exercices ou calculer les calories brûlées.

2. Ajouter un Exercice
L'utilisateur pourra ajouter un exercice avec les informations suivantes : nom de l'exercice, durée (en minutes) et calories brûlées par minute.

3. Afficher la Liste des Exercices
L'application affichera tous les exercices ajoutés par l'utilisateur.

4. Calculer les Calories Brûlées
L'application calculera le total des calories brûlées en fonction de la durée et des calories brûlées par minute pour chaque exercice.

Squelette du Code'''
# Fonction pour afficher le menu principal
def afficher_menu():
    # TODO: Afficher les options disponibles pour l'utilisateur
    pass

# Fonction pour ajouter un exercice à la liste
def ajouter_exercice(exercices):
    # TODO: Demander à l'utilisateur d'entrer les détails de l'exercice
    # TODO: Ajouter l'exercice à la liste des exercices
    pass

# Fonction pour afficher la liste des exercices
def afficher_exercices(exercices):
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
        choix = input("Choisissez une option : ")  # Demander à l'utilisateur de choisir une option
        
        if choix == '1':
            ajouter_exercice(exercices)  # Appeler la fonction pour ajouter un exercice
        elif choix == '2':
            afficher_exercices(exercices)  # Appeler la fonction pour afficher les exercices
        elif choix == '3':
            calculer_calories_brulees(exercices)  # Appeler la fonction pour calculer les calories brûlées
        elif choix == '4':
            print("Au revoir!")  # Afficher un message de départ et quitter la boucle
            break
        else:
            print("Choix invalide. Veuillez réessayer.\n")  # Gérer les choix invalides

# Point d'entrée du programme
if __name__ == "__main__":
    main()  # Appeler la fonction principale pour démarrer l'application
'''Explications
afficher_menu :

Cette fonction affichera les options du menu principal pour l'utilisateur.
Le but est de permettre à l'utilisateur de naviguer entre les différentes fonctionnalités de l'application.
TODO: Afficher les options disponibles.
ajouter_exercice :

Cette fonction demandera à l'utilisateur d'entrer les détails d'un nouvel exercice : nom, durée et calories brûlées par minute.
Les informations de l'exercice seront ensuite ajoutées à une liste de dictionnaires exercices.
TODO: Demander à l'utilisateur d'entrer les détails de l'exercice.
TODO: Ajouter l'exercice à la liste des exercices.
afficher_exercices :

Cette fonction vérifiera si la liste des exercices est vide.
Si elle n'est pas vide, elle affichera tous les exercices avec leurs détails respectifs (nom, durée, calories brûlées par minute).
Le but est de permettre à l'utilisateur de voir tous les exercices qu'il a ajoutés.
TODO: Vérifier si la liste des exercices est vide.
TODO: Si non, afficher tous les exercices avec leurs détails.
calculer_calories_brulees :

Cette fonction calculera le total des calories brûlées en multipliant la durée de chaque exercice par les calories brûlées par minute.
Le total sera ensuite affiché à l'utilisateur.
Le but est de permettre à l'utilisateur de connaître le total des calories brûlées pendant ses séances d'entraînement.
TODO: Calculer le total des calories brûlées pour tous les exercices.
TODO: Afficher le résultat total des calories brûlées.
main :

Cette fonction sera le point d'entrée principal de l'application.
Elle initialisera une liste vide pour stocker les exercices et utilisera une boucle while pour afficher le menu principal et gérer les choix de l'utilisateur.
Selon le choix de l'utilisateur, elle appellera les fonctions appropriées pour ajouter un exercice, afficher les exercices ou calculer les calories brûlées.
Elle permettra également à l'utilisateur de quitter l'application en sélectionnant l'option correspondante.
if name == "main":

Cette ligne vérifiera si le script est exécuté directement (et non importé comme un module).
Si le script est exécuté directement, elle appellera la fonction main pour démarrer l'application.'''