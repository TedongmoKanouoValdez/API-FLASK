mon_dictionnaire = {}

mon_dictionnaire['nom'] = 'valdez'
mon_dictionnaire['age'] = 21
mon_dictionnaire ['pays'] = 'France'
mon_dictionnaire['nationnalite'] = 'Camerounaise'

print(mon_dictionnaire)

dict = {"val": "valdou"}
for keys in dict:
    print(dict["val"])

list = [1,5,3]
for nombre in list:
    print(list)

def addition(a,b,c):
    print(a+b+c)
    return a+b+c 
sum = addition(1,5,2)

import random

def addition_aleatoire():
    nombre1 = random.randint(1, 100)
    nombre2 = random.randint(1, 100)
    
    somme = nombre1 + nombre2
    
    print(f"{nombre1} + {nombre2} = {somme}")

addition_aleatoire()

import random

ma_liste = ["a", "b", "c", "d", "e"]


element_aleatoire = random.choice(ma_liste)

print(element_aleatoire)
