class Hond():

    # De object krijgt een naam
    def __init__ (self, mijn_naam, leeftijd):
        self.naam = mijn_naam
        self.leeftijd = leeftijd * 6

    # hier word er een zin gemaakt over de object
    def __str__(self):
        return ('hey ik ben {} en ik ben {}'.format(self.naam,self.leeftijd))


# Hier krijgt de hond een naam
hond1 = Hond('Wodan', 5)
hond2 = Hond('Fifi', 4 )
hond3 = Hond('Pauw', 5)
hond4 = Hond('Fresca', 6)
hond5 = Hond('Brian', 9)
hond6 = Hond('Sia', 5)
hond7 = Hond('Rex', 8)
hond8 = Hond('Obie', 8)
hond9 = Hond('Bully', 4)

#Hier word de functie uitgevoerd
print (hond1, 'Woef')
print (hond2, 'Bark')
print (hond3, 'Waf')
print (hond4, 'Woef')
print (hond5, 'Bark')
print (hond6, 'Waf')
print (hond7, 'Woef')
print (hond8, 'Bark')
print (hond9, 'Waf')