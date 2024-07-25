# Conseils avec Exemples, Explications et Mini Exercices

## Éviter les Mots-clés Réservés

- **Explication** : Les mots-clés réservés sont des mots spéciaux qui ont une signification particulière en Python. Utiliser un mot-clé réservé comme nom de variable peut causer des erreurs.

- **Ce qu'il ne faut pas faire** :

  ```python
  def ajouter_exercice(list):
      # Erreur d'utilisation d'un mot-clé réservé
      list.append("pompe-15-12")
  ```

- **Ce qu'il faut faire** :

  ```python
  def ajouter_exercice(exercices):
      exercices.append("pompe-15-12")
  ```

- **Mini Exercice** : Écris une fonction qui ajoute un élément à une liste sans utiliser de mots-clés réservés comme noms de variables.

  ```python
  def ajouter_element(ma_liste, element):
      # Ajoute l'élément à ma_liste
      pass

  # Exemple d'appel de la fonction
  liste = []
  ajouter_element(liste, "élément1")
  print(liste)  # Devrait afficher ["élément1"]
  ```

## Manipulation de Listes

- **Explication** : Si tu modifies une liste locale au lieu de la liste passée en paramètre, les modifications ne seront pas visibles en dehors de la fonction.

- **Ce qu'il ne faut pas faire** :

  ```python
  def ajouter_exercice(exercices):
      exercices = input("Entrez l'exercice : ").split("-")
      # Erreur : Ceci crée une nouvelle liste locale
  ```

- **Ce qu'il faut faire** :

  ```python
  def ajouter_exercice(exercices):
      details = input("Entrez l'exercice : ").split("-")
      exercices.append(details)
  ```

- **Mini Exercice** : Écris une fonction qui ajoute un nombre à une liste de nombres passée en paramètre sans créer de nouvelle liste locale.

  ```python
  def ajouter_nombre(liste_de_nombres, nombre):
      # Ajoute le nombre à liste_de_nombres
      pass

  # Exemple d'appel de la fonction
  nombres = [1, 2, 3]
  ajouter_nombre(nombres, 4)
  print(nombres)  # Devrait afficher [1, 2, 3, 4]
  ```

## Passage de Paramètres

- **Explication** : Assure-toi de passer tous les paramètres nécessaires lors de l'appel d'une fonction.

- **Ce qu'il ne faut pas faire** :

  ```python
  def main():
      afficher_exercices()  # Erreur : Aucun argument passé
  ```

- **Ce qu'il faut faire** :

  ```python
  def main():
      exercices = []
      afficher_exercices(exercices)
  ```

- **Mini Exercice** : Écris deux fonctions, `afficher_liste` et `main`, où `main` passe correctement une liste de chaînes de caractères à `afficher_liste`.

  ```python
  def afficher_liste(chaine_liste):
      # Affiche chaque chaîne dans la liste
      pass

  def main():
      ma_liste = ["a", "b", "c"]
      # Appelle afficher_liste avec ma_liste
      pass

  # Appel de main pour tester
  main()
  ```

## Utilisation de Boucles et Conditions

- **Explication** : Utilise des boucles et des conditions pour répéter des actions et gérer les différentes options de l'utilisateur.

- **Ce qu'il ne faut pas faire** :

  ```python
  def main():
      while True:
          if choix == 1:
              # Code pour ajouter un exercice
              break  # Erreur : Cela sort de la boucle dès la première itération
  ```

- **Ce qu'il faut faire** :

  ```python
  def main():
      while True:
          choix = input("Choisissez une option : ")
          if choix == '1':
              ajouter_exercice(exercices)
          elif choix == '4':
              print("Au revoir!")
              break
          else:
              print("Choix invalide. Veuillez réessayer.")
  ```

- **Mini Exercice** : Écris une fonction qui demande à l'utilisateur de choisir entre trois options et répète la demande jusqu'à ce que l'utilisateur choisisse de quitter.

  ```python
  def menu():
      while True:
          choix = input("Choisissez une option (1: Continuer, 2: Afficher message, 3: Quitter) : ")
          if choix == '1':
              print("Vous avez choisi de continuer.")
          elif choix == '2':
              print("Vous avez choisi d'afficher un message.")
          elif choix == '3':
              print("Au revoir!")
              break
          else:
              print("Choix invalide. Veuillez réessayer.")

  # Appel de la fonction pour tester
  menu()
  ```

## Décomposition du Problème

- **Explication** : Décompose ton programme en plusieurs fonctions pour le rendre plus lisible et plus facile à maintenir.

- **Ce qu'il ne faut pas faire** :

  ```python
  def main():
      exercices = []
      while True:
          choix = input("Choisissez une option : ")
          if choix == '1':
              details = input("Entrez l'exercice : ").split("-")
              exercices.append(details)  # Erreur : Trop de logique dans la boucle principale
  ```

- **Ce qu'il faut faire** :

  ```python
  def ajouter_exercice(exercices):
      details = input("Entrez l'exercice : ").split("-")
      exercices.append(details)

  def main():
      exercices = []
      while True:
          afficher_menu()
          choix = input("Choisissez une option : ")
          if choix == '1':
              ajouter_exercice(exercices)
          elif choix == '4':
              print("Au revoir!")
              break
          else:
              print("Choix invalide. Veuillez réessayer.")
  ```

- **Mini Exercice** : Décompose le code suivant en plusieurs fonctions ayant chacune une responsabilité spécifique.

  ```python
  def main():
      while True:
          choix = input("Entrez un nombre (ou 'q' pour quitter) : ")
          if choix == 'q':
              break
          elif choix.isdigit():
              print(f"Vous avez entré le nombre {choix}")
          else:
              print("Entrée invalide.")

  # Appel de la fonction pour tester
  main()
  ```

## Commentaires et TODOs

- **Explication** : Utilise des commentaires pour expliquer ce que fait chaque partie de ton code. Cela aide à comprendre et maintenir le code.

- **Ce qu'il ne faut pas faire** :

  ```python
  def ajouter_exercice(exercices):
      details = input("Entrez l'exercice : ").split("-")
      exercices.append(details)  # Erreur : Pas de commentaire expliquant le code
  ```

- **Ce qu'il faut faire** :

  ```python
  def ajouter_exercice(exercices):
      # Demander à l'utilisateur d
  ```
