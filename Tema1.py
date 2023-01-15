# ##### 1. Variabila este un recipient unde se pun niste obiecte (le etichetam)

# ##### 2. #####
car = 'Mercedes'
years_old = 10
price = 25.57
inmatriculated = True


##### 3. #####
print(type(car))
print(type(years_old))
print(type(price))
print(type(inmatriculated))

##### 4. #####
print(round(price))

# ##### 5. #####
print(f"Detin o masina {car} dar este cel mai ieftin model")
print(f"Masina mea {car} are {years_old} ani vechime")
print(f"Pretul uleiului de masina este de {price} lei")
assert inmatriculated == True
print(f'Masina mea {car} este inmatriculata')

##### 6. #####
name = input("Introdu numele: ")
surname = input("Introdu prenumele: ")

namelenght = len(name + surname)
print(f"Numele complet are {namelenght} caractere")
#
##### 7. #####
lenght = float(input("Introdu lungimea dreptunghiului: "))
wide = float(input("Introdu latimea dreptunghiului: "))
arrayof = (lenght * wide)
print(f"Aria dreptunghiului este: {arrayof}")

##### 8 si 9 #####
quote = 'Coral is either the stupidest animal or the smartest rock'
print(len(quote))
print(quote.count('the',0 ,57))

###### 10 ######

only_numbers = quote.isnumeric()
assert only_numbers == False
print('Citatul nu contine numere')
# assert only_numbers == True
# print('Citatul contine numere')

##### Exerciții Opționale#####
##### 1. #####
string_impare = input("Introdu textul: ")
string_lenght = int(len(string_impare))
if (string_lenght % 2) ==0:
    print("Stringul este format dintr-un numar par de caractere, voi afisa varianta stringului cu numar impar de caractere")
    print(f"{string_impare[0:(string_lenght -1)]} ")
else:
    print(f"{string_impare}")

###### caracterul din mijloc #####
if (string_lenght % 2) ==0:
    print(f"Caracterul din mijloc este: {string_impare[round(int((string_lenght / 2)-1))]}")
else:
    print(f"Caracterul din mijloc este: {string_impare[round(int(string_lenght / 2))]}")

##### 2. #####
str1 = "Marius invata Python"
str2 = str1 == str1[:: -1]
assert str2 == False
print("string NU este palindrom")

##### 3. #####
#print(input("Introdu textul: \v"))
m =input("Introdu textul: \v")
variable_list = m.split()
print(f"variabilele sunt {variable_list}")

##### 4. #####
word = input("Introdu textul: \v")
primul = word[0:1]
print(primul.capitalize())
ultimul = word[-1]
print(primul + word[1:-1].replace(primul, primul.capitalize()) + str(ultimul))

##### 5.#####
x = input("userul este: ")
y = input("parola este: ")
z = "*" * (int(len(y)))
print(f"Parola pt user {x} este {z} și are {len(z)} caractere")

