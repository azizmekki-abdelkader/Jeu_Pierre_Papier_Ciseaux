# Jeu Pierre-Papier-Ciseaux

Ce projet est un jeu en ligne développé pour le cours Fondement des Réseaux. Il inclut une interface graphique, une connexion réseau et une IA basée sur Deep Reinforcement Learning.

## Prérequis
- Python 3.11
- Modules : `pygame`, `stable-baselines3`, `gym`

## Installation
1. Téléchargez les fichiers depuis ce dépôt.
2. Installez les modules :python -m pip install pygame stable-baselines3 gym
3. Lancez le serveur :python serveur.py
4. Lancez les clients :python client.py
## Fonctionnement
- `jeu_simple.py` : Jeu local dans le terminal.
- `jeu_graphique.py` : Jeu local avec interface graphique.
- `serveur.py` + `client.py` : Jeu en réseau entre deux joueurs.
- `client_ia.py` : Jeu contre une IA entraînée.

## Architecture
- **Réseau** : Utilise `socket` pour la communication client-serveur.
- **IA** : Modèle DQN entraîné avec Stable-Baselines3.
- **Interface** : Pygame pour l’affichage graphique.
