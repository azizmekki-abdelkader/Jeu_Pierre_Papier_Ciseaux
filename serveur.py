import socket
import threading

# Configurer le serveur
host = "127.0.0.1"  # Adresse locale
port = 55555

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((host, port))
serveur.listen()

print("Serveur en attente de connexions...")

# Liste des clients connectés
clients = []
choix = {}

# Envoyer un message à tous les clients
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# Gérer un client
def handle(client):
    while True:
        try:
            # Recevoir le choix du client
            message = client.recv(1024).decode()
            if message in ["pierre", "papier", "ciseaux"]:
                choix[client] = message
                if len(choix) == 2:  # Deux joueurs ont fait un choix
                    joueur1, joueur2 = list(choix.keys())
                    choix1, choix2 = choix[joueur1], choix[joueur2]

                    if choix1 == choix2:
                        resultat = "Égalité !"
                    elif (choix1 == "pierre" and choix2 == "ciseaux") or \
                         (choix1 == "papier" and choix2 == "pierre") or \
                         (choix1 == "ciseaux" and choix2 == "papier"):
                        resultat = "Joueur 1 gagne !"
                    else:
                        resultat = "Joueur 2 gagne !"

                    broadcast(f"Choix: {choix1} vs {choix2}. {resultat}")
                    choix.clear()
        except:
            clients.remove(client)
            client.close()
            break

# Accepter les connexions
while True:
    client, adresse = serveur.accept()
    print(f"Connecté à {adresse}")
    clients.append(client)
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()