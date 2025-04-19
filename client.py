import pygame
import socket

# Initialiser Pygame
pygame.init()

# Configurer la fenêtre
largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pierre Papier Ciseaux - Client")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police
police = pygame.font.SysFont("arial", 30)

# Connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

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
                    client.send(joueur_choix.encode())

    # Recevoir les messages du serveur
    try:
        message = client.recv(1024).decode()
        resultat = message
    except:
        pass

    pygame.display.flip()

client.close()
pygame.quit()