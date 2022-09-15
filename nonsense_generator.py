# The Star Trek writers are on strike and you need some new Sci-Fi sounding words that the actors can talk about
# https://www.youtube.com/watch?v=h4idB5KAfyc
import random


words_1 = ["Hyperdimentional", "Electron", "hyperspace", "Pocket Universe", "Photon", "Wave", "Beam", "Antigravity",
           "Cyberspace"]
words_2 = ["Combuster", "Emitter", "Dampener", "Array", "Android", "Cyborg", "Torpedo", "Sail", "Terraformner",
           "Alien", "Elevator"]


def greet_nonsense(name):
    print(f'Hi {name}, here is some nonsense: {random.choice(words_1)} + " " + {random.choice(words_2)}')
