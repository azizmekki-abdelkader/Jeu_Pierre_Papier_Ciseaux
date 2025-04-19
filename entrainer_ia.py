from stable_baselines3 import DQN
from environnement import PierrePapierCiseauxEnv

# Créer l'environnement
env = PierrePapierCiseauxEnv()

# Créer le modèle
model = DQN("MlpPolicy", env, verbose=1)

# Entraîner le modèle
model.learn(total_timesteps=10000)

# Sauvegarder le modèle
model.save("modele_ia")