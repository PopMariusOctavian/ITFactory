# 1. #IF...ELSE = daca o conditie este indeplinita (if), executam un cod, daca nu (else) executam alt cod

# 2. #
x = int(input("Introdu valoarea lui x: "))
if x >= 0:
    print(f"Numarul introdus este {x} si este un numar natural")
else:
    print(f"Numarul introdus este {x} si Nu este un numar natural")

# 3. #
if x > 0:
    print(f"Numarul introdus este {x} si este un numar pozitiv")
elif x == 0:
    print(f"Numarul introdus este {x} si este un numar neutru")
else:
    print(f"Numarul introdus este {x} si este un numar negativ")

# 4. #
if x <= -3:
    print(f"Numarul introdus este {x} si NU este între -2 și 13")
elif x <= 13:
    print(f"Numarul introdus este {x} si este între -2 și 13")
else:
    print(f"Numarul introdus este {x} si NU este între -2 și 13")

# 5. #
y = int(input("Introdu valoarea lui y: "))
z = x - y
if z < 5:
    print(f"Diferența dintre {x} și {y} este mai mică de 5")
else:
    print(f"Diferența dintre {x} și {y} este mai mare de 5")

# 6. #
if not(x > 5):
    print(f"Numarul introdus este {x} si NU este între 5 și 27")
elif not(x < 27):
    print(f"Numarul introdus este {x} si NU este între 5 și 27")
else:
    print(f"Numarul introdus este {x} si este între 5 și 27")

# 7. #
if x == y:
    print(f"Numarul {x} si {y} sunt egale")
elif x < y:
    print(f"Numarul {y} este mai mare decat {x}")
else:
    print(f"Numarul {x} este mai mare decat {y}")

# 8. #
z = int(input("Introdu valoarea lui z: "))
if (x > 0 and y > 0 and z > 0)==True:
    if (x==y and y!=z) == True:
        print(f"Triunghiul este isoscel si are laturile x={x} , y={y} si z={z}")
    elif(x!=y and x==z )== True:
        print(f"Triunghiul este isoscel si are laturile x={x} , y={y} si z={z}")
    elif (x!=y and x!=z and y!=z) ==True:
        print(f"Triunghiul este oarecare si are laturile x={x} , y={y} si z={z}")
    elif (x == y and x == z and y == z) == True:
        print(f"Triunghiul este echilateral si are laturile x={x} , y={y} si z={z}")
else:
    print(f"Valorile introduse nu pot forma un triunghi")

# 9. #
a = input("introdu o litera: ").lower()
vocals = ("a", "e", "i", "o","u")
if a in vocals:
    print("litera este o vocala")
else:
    print("litera nu este o vocala")

# 10. #
nota = int(input("Introdu nota obtinuta: "))
if (nota <= 4 and nota > 0):
    print(f"Ai obtinut nota {nota}, deci calificativul F")
elif (nota == 5 or nota == 6)== True:
    print(f"Ai obtinut nota {nota}, deci calificativul E")
elif nota == 7:
    print(f"Ai obtinut nota {nota}, deci calificativul D")
elif nota == 8:
    print(f"Ai obtinut nota {nota}, deci calificativul C")
elif nota == 9:
    print(f"Ai obtinut nota {nota}, deci calificativul B")
elif nota == 10:
    print(f"Ai obtinut nota {nota}, deci calificativul A")
else:
    print("Ai introdus nota gresit, te rog reincearca")
