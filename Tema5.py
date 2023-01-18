# 1.Funcție care să calculeze și să returneze suma a două numere
a = int(input("Introdu primul numar: "))
b = int(input("introdu al doilea numar: "))


def sum_numbers(a, b):
    return a + b


print(sum_numbers(a, b))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

numar = int(input("introdu numarul dorit spre verificare: "))


def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


print(f"daca numar este par, afisam True, daca este impar afisam False: ", par_impar(numar))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)

nume = input("introdu numele: ")
prenume = input("introdu prenumele: ")
nume_mijlociu = input("introdu numele mijlociu: ")


def numar_total_caractere(nume, nume_mijlociu, prenume):
    suma = len(nume) + len(prenume) + len(nume_mijlociu)
    return suma


print(f"numărul total de caractere din numele tău complet este: ", numar_total_caractere(nume, nume_mijlociu, prenume))

# 4. Funcție care returnează aria dreptunghiului

latimea = int(input("introdu latimea dreptunghiului: "))
lungimea = int(input("introdu lungimea dreptunghiului: "))


def aria_dreptunghiului(latime, lungime):
    aria = latime * lungime
    return aria


print(f"aria dreptunghiului este: ", aria_dreptunghiului(latimea, lungimea))

# 5. Funcție care returnează aria cercului

raza = int(input("introdu raza cercului: "))


def aria_cercului(raza):
    aria = raza * raza
    return aria


print(f"aria cercului este: ", aria_cercului(raza))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

string = "Sunt tare obosit, am nevoie de un concediu sau sa ma angajez intr-o firma de IT"
print(string)
caracter = input("introdu caracterul de verificat daca este in stringul de mai sus: ")


def verificare(caracter):
    if caracter in string:
        return True
    else:
        return False


print(f"caracterul '{caracter}' este in string? Raspuns: ", verificare(caracter))

"""
. Funcție fără return, primește un string și printează pe ecran:
●Nr de caractere lower case este x
●Nr de caractere upper case exte y
"""


def functie():
    string = input("Introdu string: ")
    string1 = string.join(string.split())
    string_upper = 0
    string_lower = 0
    for caracter in string1:
        if caracter.islower():
            string_lower += 1
        elif caracter.isupper():
            string_upper += 1
        else:
            pass  # am pus aici asa pentru a nu contoriza semnele de punctuatie
    print(f"Nr de caractere lower case este {string_lower}")
    print(f"Nr de caractere upper case este {string_upper}")


functie()


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cunumerele pozitive


def functie_nr_pozitive():
    inputul = input("Introdu o lista de numere pozitive sau negative separate de spatiu: ").split()
    lista = []
    for numar in inputul:
        if int(numar) > 0:
            lista.append(numar)
            print(lista)


functie_nr_pozitive()

"""9 Funcție care nu returneaza nimic.
Primește două numere și PRINTEAZA●
Primul număr x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale.
"""


def numere():
    numere_primite = input("Introdu doua numere despartite prin spatiu: ").split()
    if numere_primite[0] > numere_primite[1]:
        print(f"Primul număr {numere_primite[0]} este mai mare decat al doilea nr {numere_primite[1]}")
    elif numere_primite[0] < numere_primite[1]:
        print(f"Al doilea nr {numere_primite[1]} este mai mare decat primul nr {numere_primite[0]}")
    else:
        print("Numerele sunt egale.")


numere()

"""10. Funcție care primește un număr și un set de numere
Printeaza ‘am adaugat numărul nou în set’ + returnează True
Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +returnează False
"""


def adaugam_numere():
    numar = input("Introdu un numar: ").split()
    numere = input("Introdu un set de numere despartite prin spatiu: ").split()

    if numar[0] not in numere:
        numere.insert(0, numar[0])
        print("Am adaugat numărul nou în set", True)
    else:
        print("Nu am adaugat numărul în set. Acesta există deja", False)


adaugam_numere()
