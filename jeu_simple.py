import random

# Liste des choix possibles
choix_possibles = ["pierre", "papier", "ciseaux"]

# Demander le choix du joueur humain
print("Choisis : pierre, papier ou ciseaux")
joueur = input().lower()

# Vérifier que le choix est valide
if joueur not in choix_possibles:
    print("Choix invalide ! Choisis pierre, papier ou ciseaux.")
else:
    # L'ordinateur choisit au hasard
    ordinateur = random.choice(choix_possibles)
    print(f"Tu as choisi : {joueur}")
    print(f"L'ordinateur a choisi : {ordinateur}")

    # Déterminer le gagnant
    if joueur == ordinateur:
        print("Égalité !")
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "papier" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "papier"):
        print("Tu gagnes !")
    else:
        print("L'ordinateur gagne !")