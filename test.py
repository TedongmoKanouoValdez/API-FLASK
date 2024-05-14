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

def aleatoire(choice_or_randint, list=[] , min=0, max=10): 

    if choice_or_randint == True: 

        return random.randint(min,max) 

    else: 

        return random.choice(list) 

print(aleatoire(False, list = [9,0,20,8,7,22,100,199992]))  

print(aleatoire(True, min=999, max=1000)) 

 