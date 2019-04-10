import random
import sys

#Geheime code maken
cijfer1 = str(random.randint(1,6))
#print("cijfer1 =",cijfer1)
cijfer2 = str(random.randint(1,6))
while cijfer1 == cijfer2:
    cijfer2 = str(random.randint(1,6))
#print("cijfer2 =",cijfer2)
cijfer3 = str(random.randint(1,6))
while cijfer3 == cijfer1 or cijfer3 == cijfer2:
    cijfer3 = str(random.randint(1,6))
#print("cijfer3 =",cijfer3)
cijfer4 = str(random.randint(1,6))
while cijfer4 == cijfer1 or cijfer4 == cijfer2 or cijfer4 == cijfer3:
    cijfer4 = str(random.randint(1,6))
#print("cijfer4 =",cijfer4)
raadcode = cijfer1+cijfer2+cijfer3+cijfer4
#print("raadcode =",raadcode)

#Spellus
for ronde in range(1,11):
    print("Ronde", ronde)

    # Invoeren van de code door de speler
    while True:
        code = input("Geef je code van 4 cijfers op (stop met 9999): ")
        #Controleren op alleen cijfers
        if code.isdigit():
            #Stop met het spel
            if int(code) == 9999:
                sys.exit()
            #Controle op 4 cijfers
            if len(code) == 4:
                #Controleren op cijfers <1 of >6
                fout = 0
                for x in range(0,4):
                    if int(code[x]) <1 or int(code[x]) >6:
                        fout = 1
                if fout == 0:
                    gelijk = 0
                    for x in range(0,4):
                        for y in range(0,4):
                            if x != y and code[x] == code[y]:
                                gelijk = 1
                    if gelijk == 0:
                        break
                    else:
                        print("Twee of meer cijfers zijn hetzelfde.")
                        
                else:
                    print("Cijfers mogen niet lager zijn dan 1 of hoger dan 6")
            
            else:
                print("Te weinig of teveel cijfers.")

        else:
            print("Er staan letters in.")

    #Vergelijk de ingevoerde code met de geheime code
    goede_plaats = 0
    goede_cijfer = 0
    for x in range(0,4):
        #Cijfer goed en op de goede plaats
        if raadcode[x] == code[x]:
            goede_plaats = goede_plaats + 1
            #De code is goed geraden
            if goede_plaats == 4:
                print("Gefeliciteerd! Dat was de code.")
                sys.exit()
        #Cijfer goed maar niet op de goede plaats
        else:
            for y in range(0,4):
                if x != y and raadcode[x] == code[y]:
                    goede_cijfer = goede_cijfer + 1
    #Afbeelden resultaat
    if goede_plaats > 0:
        print("Goede cijfer op de goede plaats.", goede_plaats)
    if goede_cijfer > 0:
        print("Goede cijfer op de verkeerde plaats.", goede_cijfer)
#De code is niet geraden
print("Helaas niet geraden! De code was", raadcode)

