#Contexte : Vous développez un système de notation pour un site de critiques de films. 
# Chaque film reçoit une note sur 100, et en fonction de cette note, vous devez classer le film comme "Excellent", "Bon", "Passable" ou "Mauvais".
#Objectif : Écrivez un programme qui demande à l'utilisateur d'entrer la note d'un film. 
# Utilisez des structures conditionnelles pour classer le film selon la note :

#"Excellent" pour les notes de 90 à 100,
#"Bon" pour les notes de 70 à 89,
#"Passable" pour les notes de 50 à 69,
#"Mauvais" pour les notes inférieures à 50.
#Affichez le classement du film.

note = int(input("Bonjour, quelle note selon mérite le film sur une echelle de 1 à 100 ?\nQuelle est votre note : "))

if note > 90 :
    print("Vous avez jugé le film comme excellent")
elif note > 70 : 
    print("Vous avez jugé le film comme bon")
elif note > 50 : 
    print("Vous avez juger le film comme passable")
else : 
    print("Vous avez juger le film comme mauvais")

