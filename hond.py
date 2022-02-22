#De Object is gecreerd (de hond)
class Hond():

    # De object krijgt een naam
    def __init__ (self, mijn_naam, leeftijd):
        self.naam = mijn_naam
        self.leeftijd = leeftijd

    # hier word er een zin gemaakt over de object
    def __str__(self):
        return ('hey ik ben {} en ik ben {}'.format(self.naam,self.leeftijd))


# Hier krijgt de hond een naam
hond1 = Hond('Wodan', 5)
hond2 = Hond('Fifi', 5 )
hond3 = Hond('Pauw', 5)

#Hier word de functie uitgevoerd
print (hond1)
print (hond2)
print (hond3)

    
