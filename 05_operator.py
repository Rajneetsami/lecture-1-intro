

Skapa en applikation där användaren matar in två tal (heltal!)

a. Skriv in Mata in tal 1:
b. Ta emot detta tal i en variabel
c. Skriv in Mata in tal 2:
d. Ta emot värdet på detta tal
e. Nu ska ni göra massa beräkningar på dessa tal. OBS: lägg resultat i en variabel innan ni skriver ut
resultat = tal1 * tal2
f. räkna tal1 upphöjd till tal 2 och skriv ut
g. räkna tal1 gånger tal 2 och skriv ut
h. räkna tal1 delat med tal 2 och skriv ut (OBS!!! Kolla datatypen på resultat)
i. räkna tal1 plus tal 2 och skriv ut
j. räkna tal1 minus tal 2 och skriv ut
k. räkna tal1 heltalsdividerat (%) tal 2 och skriv ut
l. räkna ut resten från heltalsdivision (//) mellan tal1 och tal 2 och skriv ut


tal1 = int(input("mata in tal1: "))
tal2 = int(input("mata in tal2: "))

result = tal1**tal2
print(result)

result = tal1*tal2
print(result)

result = tal1/tal2
print(result)

result = tal1+tal2
print(result)

result = tal1-tal2
print(result)

result = tal1%tal2
print(result)

result = tal1//tal2
print(result)
