"""__repr__ este o metodă specială (numită magic method sau dunder method) în Python care definește cum este reprezentat un obiect ca string,
în special pentru debugging și dezvoltare."""

class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __repr__(self):
        return f"Persoana(nume='{self.nume}', varsta={self.varsta})"

p = Persoana("Ana", 25)
print(repr(p))  #Persoana(nume='Ana', varsta=25)

#__init__ este metoda care se ocupă de inițializarea obiectului — adică setează valorile inițiale atunci când creezi o instanță.
"""__init__ → pune datele în obiect  //   __repr__ → arată obiectul"""