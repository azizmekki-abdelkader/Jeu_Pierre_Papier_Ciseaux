import gym
from gym import spaces
import numpy as np

class PierrePapierCiseauxEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(3)  # Pierre, Papier, Ciseaux
        self.observation_space = spaces.Discrete(1)  # Pas d'observation complexe
        self.choix = ["pierre", "papier", "ciseaux"]

    def reset(self):
        return 0

    def step(self, action):
        joueur_choix = self.choix[action]
        adversaire_choix = np.random.choice(self.choix)  # Adversaire aléatoire

        if joueur_choix == adversaire_choix:
            recompense = 0
        elif (joueur_choix == "pierre" and adversaire_choix == "ciseaux") or \
             (joueur_choix == "papier" and adversaire_choix == "pierre") or \
             (joueur_choix == "ciseaux" and adversaire_choix == "papier"):
            recompense = 1
        else:
            recompense = -1

        done = True
        return 0, recompense, done, {}

    def render(self):
        pass