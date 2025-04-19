import pygame
from stable_baselines3 import DQN
from environnement import PierrePapierCiseauxEnv

# Initialiser Pygame
pygame.init()

# Configurer la fenêtre
largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pierre Papier Ciseaux - IA")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police
police = pygame.font.SysFont("arial", 30)

# Charger l'IA
env = PierrePapierCiseauxEnv()
model = DQN.load("modele_ia")

# Variables
choix_possibles = ["pierre", "papier", "ciseaux"]
joueur_choix = None
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
    texte_resultat = police.render(resultat, True, NOIR)
    fenetre.blit(texte_resultat, (300, 50))

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, choix in enumerate(choix_possibles):
                if 50 <= x <= 200 and 50 + i * 50 <= y <= 90 + i * 50:
                    joueur_choix = choix
                    # L'IA choisit
                    obs = 0
                    action, _ = model.predict(obs)
                    ia_choix = choix_possibles[action]

                    # Déterminer le gagnant
                    if joueur_choix == ia_choix:
                        resultat = "Égalité !"
                    elif (joueur_choix == "pierre" and ia_choix == "ciseaux") or \
                         (joueur_choix == "papier" and ia_choix == "pierre") or \
                         (joueur_choix == "ciseaux" and ia_choix == "papier"):
                        resultat = "Tu gagnes !"
                    else:
                        resultat = "IA gagne !"
                    resultat += f" (IA: {ia_choix})"

    pygame.display.flip()

pygame.quit()