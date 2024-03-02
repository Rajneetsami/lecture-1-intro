


Kvadrater
Skriv ett program som gör följande:
• Frågar användaren om ett tal
• Beräkna kvadraten av talet och skriver ut svaret
Svårighetsgrad 2+
– Fråga användaren om den vill beräkna kvadratroten istället(y/n)? Om ja, beräkna kvadratroten och skriv ut svaret och avsluta. Annars avsluta pro- grammet!
Kolla in python:s math modul! → math.sqrt(









import math

tal = int(input('skriv in ett tal: '))
kvadraten = tal*tal
print(f'kvardratten är {kvadraten}')

print(" vill du beräkna kvadratroten: (y/n)")
svar = input('svar med hjälp av y/n: ').lower()

if svar == 'y':
    kvadratroten = round(math.sqrt(tal),3)
    print(f'kvadratroten är {kvadratroten}')
else:
    print("avsluta programmet")
