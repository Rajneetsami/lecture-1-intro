

Rabbaten
Skriv ett program som gör följande:
• Frågar användaren om ursprungspriset på en vara
• Frågar användaren om rabbat i form av procent
• Beräkna rabbaten och skriv ut svaret
25% är ju 25 100
Svårighetsgrad 2+
– Beräkna förändringen i värdet baserat ursprungspriset och skriv ut detta – Beräkna rabbat på rabbaten och skriv ut detta










ursprungspriset = int(input('skriv in: '))
rabbat_procent = int(input('skriv in: '))
räkna_rabbat = (ursprungspriset*rabbat_procent)/100
print (räkna_rabbat)
förandrning = ursprungspriset-räkna_rabbat
print (förandrning)
rabbat = (räkna_rabbat*rabbat_procent)/100
print (rabbat)
