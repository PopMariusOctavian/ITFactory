# 1. am "complicat" aplicatia, sper sa iti placa ce a iesit

jucatori = ["Andi", "Marius", "Ada", "Marcela", "Maria"]
print(f"Avem jucatorii {jucatori} ")
schimbari_efectuate = 1
schimbari_maxime = 3
in_teren = ["Andi", "Marius", "Ada"]
rezerve = ["Marcela", "Maria"]
print(f"Rezervele tale sunt: {rezerve}")
print(f"In teren sunt urmatorii jucatori {in_teren}")
if schimbari_maxime - schimbari_efectuate > 0:
    print(f"Mai ai {schimbari_maxime - schimbari_efectuate} schimbari disponibile" )
    jucator_iesit = input("Introdu numele jucatorului ce doresti sa iasa de pe teren: ").capitalize()
    jucator_intrat = input("Introdu numele jucatorului ce doresti sa intre pe teren: ").capitalize()
    if jucator_iesit in in_teren and schimbari_efectuate < schimbari_maxime and jucator_intrat in rezerve:
        in_teren.remove(jucator_iesit)
        rezerve.append(jucator_iesit)
        in_teren.append(jucator_intrat)
        rezerve.remove(jucator_intrat)
        schimbari_efec = schimbari_efectuate + 1
        print(f"A intra {jucator_intrat}, A ieșit {jucator_iesit}, mai ai {schimbari_maxime - schimbari_efec} schimbări")
        print(f"Acum ai in teren jucatorii {in_teren} si rezervele sunt {rezerve}")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren, sau {jucator_intrat} nu este rezerva")
        print(f"Mai ai {schimbari_maxime - schimbari_efectuate} schimbari disponibile")
else:
    print("Ai facut maximul de schimbari permise")




