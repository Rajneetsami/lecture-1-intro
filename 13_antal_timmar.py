
Antal timmar
Skriv ett program som gör följande:
• Fråga användaren om antalet veckor, dagar och timmar
• Omvandla detta till totalt antal timmar och skriv ut resultatet
Svårighetsgrad 2+
– Beräkna totalt antal dagar, svara med tiondels noggranhet och skriv ut svaret
– Beräkna totalt antal veckor, svara med tiondels noggranhet och skriv ut
svaret
– Beräkna totalt antal år, svara med hundradels noggranhet






antal_timmar = int(input('skriv in antal timmar: '))
antal_veckor = int(input('skriv in antal veckor: '))
anatl_dagar = int(input('skriv in antal dagar: '))

resultat1 = antal_timmar+antal_veckor*7*24+anatl_dagar*24
print('total timmar: ', resultat1)

resultat2 = (antal_timmar/24)+anatl_dagar+(antal_veckor*7)
print('total days: ', round(resultat2,1))

resultat3 = antal_veckor+(anatl_dagar/7)+(antal_timmar/168)
print('total weeks: ', round(resultat3,1))

resultat4 = (antal_veckor/52)+(anatl_dagar/365)+(antal_timmar/8760)
print('total year: ', round(resultat4, 2))
