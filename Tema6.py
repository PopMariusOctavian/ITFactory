"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        return self.culoare and self.raza

    def aria(self):
        return self.raza**2

    def diametru(self):
        return self.raza*2

    def circumferinta(self):
        return self.raza** 2 * 3.14


"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare


    def descrie(self):
        return self.lungime, self.latime, self.culoare

    def aria(self):
        return self.latime*self.lungime

    def perimetru(self):
        return 2*self.lungime + 2*self.latime

    def schimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare


"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return self.nume, self.prenume, self.salariu

    def nume_complet(self):
        return self.nume, self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu*12

    def marire_salariu(self, procent):
        return self.salariu*procent/100


"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} sre in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        cont_debitat = self.sold - suma
        print(f'Titularului {self.titular_cont} i s-a debitat contul cu suma {suma} si mai are in sold {cont_debitat} lei')

    def creditare_cont(self, suma):
        cont_creditat = self.sold + suma
        print(f'Titularului {self.titular_cont} i s-a creditat contul cu suma {suma} si acum are in sold {cont_creditat} lei')



