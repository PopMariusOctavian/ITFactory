""""

1.Având lista:

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',

'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;

● ‘Mașina mea preferată este x’.

● Fă același lucru cu un for each.

● Fă același lucru cu un while.

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',

          'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(f"Mașina mea preferată este {masina}")

a = 0

while a <= len(masini) - 1:
    print(f"Mașina mea preferată este {masini[a]}")

    a += 1

for masina in range(len(masini)):

    print(f"Masina mea preferata este {masini[masina]}")

else:

    pass

""" 

2. Aceeași listă: 

Folosește un for else 

În for 

- Modifică elementele din listă astfel încât să fie scrie cu majuscule, 

exceptând primul și ultimul. 

În else: 

- Printează lista. 

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',

          'Fiat', 'Trabant', 'Opel']

for masina in range(1, len(masini[:-1])):

    masini[masina] = masini[masina].upper()

else:

    print(masini)

""" 

3. Aceeași listă: 

Vine un cumpărător care dorește să cumpere un Mercedes. 

Itereaza prin ea prin modalitatea aleasă de tine. 

Dacă mașina e mercedes: 

Printează ‘am găsit mașina dorită de dvs’ 

Ieși din ciclu folosind un cuvânt cheie care face acest lucru 

Altfel: 

Printează ‘Am găsit mașina X. Mai căutam‘ 

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',

          'Fiat', 'Trabant', 'Opel']

car_wanted = input("Introdu marca de masina dorita: ").capitalize()

for car in masini:

    if car == car_wanted:

        print(f"Am găsit mașina dorită de dvs: {car_wanted}")

        break

    else:

        print(f"Am găsit mașina {car}. Mai căutam")

else:

    print("Nu avem la vanzare modelul de masina introdus")

""" 

4. Aceași listă; 

Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu 

excepția Trabant și Lăstun. 

- Dacă mașina e Trabant sau Lăstun: 

Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie 

else). 

- Printează S-ar putea să vă placă mașina x. 

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',

          'Fiat', 'Trabant', 'Opel']

for car in masini:

    if car == 'Lăstun':

        continue

    elif car == 'Trabant':

        continue

    print(f"S-ar putea să vă placă mașina {car}")

""" 

5. Modernizează parcul de mașini: 

● Crează o listă goală, masini_vechi. 

● Itereaza prin mașini. 

● Când găsesti Lăstun sau Trabant: 

- Salvează aceste mașini în masini_vechi. 

- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini). 

● Printează Modele vechi: x. 

● Modele noi: x. 

"""

masini_vechi = []

for car in masini:

    if car == 'Lăstun':

        masini_vechi.append(car)

        masini.remove(car)

        masini.append("Tesla")

    elif car == 'Trabant':

        masini_vechi.append(car)

        masini.remove(car)

        masini.append("Tesla")

print(masini)

print(masini_vechi)

""" 

6. Având dict: 

pret_masini = { 

'Dacia': 6800, 

'Lăstun': 500, 

'Opel': 1100, 

'Audi': 19000, 

'BMW': 23000 

} 

Vine un client cu un buget de 15000 euro. 

● Prezintă doar mașinile care se încadrează în acest buget. 

● Itereaza prin dict.items() și accesează mașina și prețul. 

● Printează Pentru un buget de sub 15000 euro puteți alege mașină 

xLastun 

● Iterează prin listă. 



"""

pret_masini = {

    'Dacia': 6800,

    'Lăstun': 500,

    'Opel': 1100,

    'Audi': 19000,

    'BMW': 23000

}

for masina in pret_masini:

    if pret_masini[masina] <= 15000:
        print(f"{masina} si costa {pret_masini[masina]}")

a = pret_masini.items()

for masina in a:
    print(masina)

for masina1 in a:

    if masina1[1] <= 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașină ", masina1[0])

"""
7. Având lista:numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
●Iterează prin ea.
●Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in numere:
    print(numar)
apare = 0
for numar in numere:
    if numar == 3:
        apare += 1
print (f"Numarul 3 apare de {apare} ori")

"""
8. Aceeași listă:
●Iterează prin ea
●Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for numar in range(len(numere)):
    sum += numere[numar]
    print(sum)

"""
9. Aceeași listă:
●Iterează prin ea.
●Afișază cel mai mare număr (nu ai voie să folosești max).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere:
    if numere[i] < i:
        print(i)

"""
10. Aceeași listă:
●Iterează prin ea.
●Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.Ex: dacă e 3, să devină -3
●Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for n in numere:
    print(-n)

