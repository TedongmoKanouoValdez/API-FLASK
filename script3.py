class Voiture:
    # def __int__(self,couleur,marque,immatriculation):
    #     self.couleur=couleur
    #     self.marque = marque
    #     self.immatriculation = immatriculation
    # def color(self):
    #     print(f"la couleur du vehicule{self.immatriculation} est de {self.couleur}")
    
    # v=color(111)

    def __int__(self,x,y):
        self.x=x
        self.y=y
    def avancer(self):
        self.x +=1
    def reculer(self):
        self.x -=1
    
    v=avancer(1,2)