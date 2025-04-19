import pygame
import random

# Initialiser Pygame
pygame.init()

# Créer la fenêtre du jeu
largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pierre Papier Ciseaux")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police pour le texte
police = pygame.font.SysFont("arial", 30)

# Choix possibles
choix_possibles = ["pierre", "papier", "ciseaux"]

# Variables pour le jeu
joueur_choix = None
ordinateur_choix = None
resultat = ""

# Boucle principale
running = True
while running:
    fenetre.fill(BLANC)

    # Afficher les boutons
    for i, choix in enumerate(choix_possibles):
        texte = police.render(choix.capitalize(), True, NOIR)
        fenetre.blit(texte, (50, 50 + i * 50))

    # Afficher le résultat
    if joueur_choix:
        texte_joueur = police.render(f"Tu as choisi : {joueur_choix}", True, NOIR)
        texte_ordi = police.render(f"Ordinateur : {ordinateur_choix}", True, NOIR)
        texte_resultat = police.render(resultat, True, NOIR)
        fenetre.blit(texte_joueur, (300, 50))
        fenetre.blit(texte_ordi, (300, 100))
        fenetre.blit(texte_resultat, (300, 150))

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Vérifier si un bouton est cliqué
            for i, choix in enumerate(choix_possibles):
                if 50 <= x <= 200 and 50 + i * 50 <= y <= 90 + i * 50:
                    joueur_choix = choix
                    ordinateur_choix = random.choice(choix_possibles)

                    # Déterminer le gagnant
                    if joueur_choix == ordinateur_choix:
                        resultat = "Égalité !"
                    elif (joueur_choix == "pierre" and ordinateur_choix == "ciseaux") or \
                         (joueur_choix == "papier" and ordinateur_choix == "pierre") or \
                         (joueur_choix == "ciseaux" and ordinateur_choix == "papier"):
                        resultat = "Tu gagnes !"
                    else:
                        resultat = "Ordinateur gagne !"

    pygame.display.flip()

pygame.quit()