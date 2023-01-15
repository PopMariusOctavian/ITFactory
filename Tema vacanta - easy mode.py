# """"Ex1.
# Creeaza 3 liste care sa contina animale:
# Mamifere
# Reptile
# Pasari
# -Sorteaza fiecare lista alphabetic
# -Creeaza alte 3 liste in care sa salvezi aceleasi elemente din primele 3 liste, dar cuvintele sa fie pe dos. Exemplu insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]
# -Numara caracterele din fiecare element string din fiecare lista si afiseaza lista cu cele mai multe caractere.
# -Inlocuieste fiecare al doilea element din fiecare lista cu “I am an intruder”
# -Sa se amestece toate elementele random din prima lista. Poti folosi .shuffle()
# -Sa se parcurga lista si daca se gaseste elemental “I am an intruder”, sa se returneze pozitia lui, sa se stearga din lista si sa se returneze mesajul “The intruder was kicked out
# """
# import random
#
# #1
# mamifere = ['caine', 'pisica', 'urs']
# reptile = ['sarpe', 'crocodil', 'iguana']
# pasari = ['porumbel', 'gaina', 'uliu']
#
# #2
# mamifere.sort()
# reptile.sort()
# pasari.sort()
#
# #3
# mamifere2, reptile2, pasari2 = [], [], []
# mamifere.reverse()
# reptile.reverse()
# pasari.reverse()
#
# for mamifer in mamifere:
#     mamifer = mamifer[::-1]
#     mamifere2.append(mamifer)
#
# for reptila in reptile:
#     reptila = reptila[::-1]
#     reptile2.append(reptila)
#
# for pasare in pasari:
#     pasare = pasare[::-1]
#     pasari2.append(pasare)
#
# #4
# mamifere = ['caine', 'pisica', 'urs']
# reptile = ['sarpe', 'crocodil', 'iguana']
# pasari = ['porumbel', 'gaina', 'uliu']
#
# mamiferX = 0
# reptileX = 0
# pasariX = 0
#
# for mamifer in mamifere:
#     mamiferX += len(mamifer)
# for reptila in reptile:
#     reptileX += len(reptila)
# for pasare in pasari:
#     pasariX += len(pasare)
# print(max(mamiferX, reptileX, pasariX))
#
# #5
# mamifere = ['caine', 'pisica', 'urs']
# reptile = ['sarpe', 'crocodil', 'iguana']
# pasari = ['porumbel', 'gaina', 'uliu']
#
# mamifere[1] = 'I am an intruder'
# reptile[1] = 'I am an intruder'
# pasari[1] = 'I am an intruder'
#
# #6
# random.shuffle(mamifere)
# random.shuffle(reptile)
# random.shuffle(pasari)
#
# #7
# for x in range(len(mamifere)-1):
#     if mamifere[x] == 'I am an intruder':
#         print(f'{x} este indexul cautat')
#         mamifere.remove(mamifere[x])
#         print('The intruder was kicked out')
#     else:
#         pass
#
# for x in range(len(reptile)-1):
#     if reptile[x] == 'I am an intruder':
#         print(f'{x} este indexul cautat')
#         reptile.remove(reptile[x])
#         print('The intruder was kicked out')
#     else:
#         pass
#
# for x in range(len(pasari)-1):
#     if pasari[x] == 'I am an intruder':
#         print(f'{x} este indexul cautat')
#         pasari.remove(pasari[x])
#         print('The intruder was kicked out')
#     else:
#         pass
# #cand indexul random este 0 imi da eroare codul din cate mi-am dat seama si nu stiu de ce....
#
# """Ex2.
# Creeaza clasa animal cu 4 atribute si 2 metode
# Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
# """
# class Animal:
#     def __init__(self, sex, continent, greutate, varsta ):
#         self.sex = sex
#         self.continent = continent
#         self.greutate = greutate
#         self.varsta = varsta
#
#     def continent(self):
#         return self.continent
#
#     def greutate(self):
#         return self.greutate()
#
#
# class Zoo:
#     def __init__(self, locatie, animale):
#         self.locatie = locatie
#         self.animale = []
#
#
#     def add_animal(self, animale):
#         return self.animale.append(animale)
#
# class Stapan:
#     def __int__(self, nume_stapan, nr_animale):
#        self.nume_stapan = nume_stapan
#        self.nr_animale = 0
#
#     def cumpara_animnal(self, animal):
#         self.nr_animale += 1
#
# class Loc_animale_noaptea:
#     def __init__(self, cabana, numar_maxim):
#         self.animale_cabana = []
#         self.numar_maxim = 0
#         self.cabana = cabana
#     def adauga_la_somn(self, animal):
#         if len(self.animale_cabana) < self.numar_maxim:
#             self.cabana.append(animal)
#         else:
#             pass
#
# """"
# Ex3.
# Sa se introduca un cuvant de la tastatura si sa se afiseze
# ce lungime are, cate consoane, cate vocale are si daca are vreun numar in compozitie.
#
# """
# x = input("Introdu un cuvant pentru a afisa detaliile cerute: ")
# nr_vocale = 0
# nr_consoane = 0
# numar = 0
# vocale = ['a', 'e', 'i', 'o', 'u']
# for i in range(len(x)):
#     if x[i].isdigit():
#         numar += 1
#     elif x[i] in vocale:
#         nr_vocale += 1
#     else:
#         nr_consoane +=1
# print(f'Cuvantul introdus contine {numar} numere, {nr_vocale} vocale si {nr_consoane} consoane')

""""
Ex4.
1.   Sa se creeze un dictionar cu 5 carti care sa contina numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
2.   Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
3.   Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.   Sa se creeze o functie care sa ii permita bibliotecarului sa introduca un nume de carte si sa verifice daca este available sau nu

"""

biblioteca = {}


def adaugareCarte(index_carte,carte,autor,nr_pag,mesaj):
    biblioteca.update({index_carte:{"carte":carte,"autor":autor, "nr_pag": nr_pag, "mesaj":mesaj}})

def stergereCarte(index_carte):
    biblioteca.pop(index_carte)

def verificareCarte():
    pass




adaugareCarte(1,"dune", "herbert",100,True)
adaugareCarte(2,"dune2","frank",120,True)
adaugareCarte(3,"pisica","eu",25,True)
print(biblioteca)
stergereCarte(3)
print(biblioteca)

