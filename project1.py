
def afficher_menu():
   
    print("************************************")
    print("\tMenu programme sport")
    print("************************************")
    print("Voici les choix possibles : ")
    print("1 : Ajouter un exercice.")
    print("2 : Voir la liste d'exercices.")
    print("3 : Calculer les calories brulees.")
    print("4 : Quitter.")

    choice = int(input("Choisissez une option : "))

    return choice
    

def ajouter_exercice(exercices):
    nom = input("Entrer le nom de l'exercice : ")
    duree = int(input("Entrer la durée en minutes de l'exercice : "))
    calories_par_minutes = int(input("Entrer le nombre de calories brûlées par minute : "))

    exercice = {
        'nom' : nom, 
        'duree' : duree, 
        'calories_par_minute' : calories_par_minutes
    }

    exercices.append(exercice)
    print(f"Exercice {nom} ajouté avec succès !\n")



def afficher_exercices(exercices):
    if len(exercices) == 0:
       print("Aucun exercice enregistré.\n")
    else:
       print("Liste des exercices :")
       for i, exercice in enumerate(exercices, 1): 
           print(f"{i}. {exercice['nom']} - durée : {exercice['duree']} min - Calories par minutes : {exercice['calories_par_minute']} kcal")
    print()
    

def calculer_calories_brulees(exercices):
    total_calories = 0
    for exercice in exercices:
        total_calories += exercice['duree'] * exercice['calories_par_minute']

    print(f"Total des calories brûlées : {total_calories} kcal\n")

 
def main():
    exercices = [] 
    while True:
        choix = afficher_menu()  
        
        if choix == 1:
            ajouter_exercice(exercices)
        elif choix == 2:
            afficher_exercices(exercices)
        elif choix == 3:
            calculer_calories_brulees(exercices)
        elif choix == 4:
            print("Aurevoir")
            break
        else:
            print("Choix invalide. Veuillez réesayer.\n")

        
if __name__ == "__main__":
    main() 
