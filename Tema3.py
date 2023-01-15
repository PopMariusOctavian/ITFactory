# 1.
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[: : -1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2.
print(note_muzicale.count("do"))

# 3.
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list1.extend(list2)
#list3 = list1 + list2

#4.
list1.sort()
print(list1)
elem = list1[0]
list1.remove(elem)
print(list1)

# 5.
if len(list1) == 0:
    print("Lista este goala")
else:
    print("lista nu este goala")

# 6.
list1.clear()

# 7.
if len(list1) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# 8.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
elevii = dict1.keys()
print(elevii)

# 9.
print(f"Ana a luat nota", dict1['Ana'])
print(f"Gigel a luat nota", dict1['Gigel'])
print(f"Dorel a luat nota", dict1['Dorel'])

# 10.
dict1['Dorel'] = 6
print(f"Dorel a luat nota", dict1['Dorel'], "dupa contestatie")

# 11.
del dict1['Gigel']
dict1.update({'Ionica' : 9})
print(dict1)

# 12.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# 13.
if weekend.issubset(zile_sapt) == True:
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")

# 14.
difference = zile_sapt.difference(weekend)
print(difference)

# 15.
intersection = zile_sapt.intersection(weekend)
print(intersection)

