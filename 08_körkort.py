

Körkortet
Skriv ett program som gör följande:
• Frågar användaren om sin ålder
• Om åldern är 18 år eller mer, skriv ut ”Du får ta körkort!”. Annars, skriv ut ”Du får vänta tills du är 18 för att ta körkort.”
Svårighetsgrad 2+
– Fråga användaren innan om denne har körkort (y/n)!
– Om användaren har körkort men är under 18 ska det skrivas ut: ”Omöjligt!
Man måste vara 18 år eller äldre för att ta körkort!”
– Annars, beroende på svaren från användaren, så ska antingen något av ovanstående skrivas ut eller ”Gratulerar! Du får köra på vägarna!







din_ålder = int(input('skriv in din ålder: '))

print('har du körkort: y/n')
svar = input( 'y/n: ').lower()

if svar == 'y' and din_ålder< 18:
    print('omöjligt! man måste vara 18 år eller äldre att ta körkort')

elif din_ålder >=18 and svar == 'n':
    print('du får ta körkort')

elif din_ålder< 18 and svar == 'n':
    print('du får vänta tills du är 18 för att ta körkort')
else:
 print('gratulera! du får köra på vägen')   
