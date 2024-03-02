
Procenträknare
Skriv ett program som gör följande:
• Frågar användaren om startvärdet/ursprungsvärdet
• Fråga användaren om nuvarande värde
• Beräkna den procentuella förändringen och skriv ut till användaren!
Start−Nuvarande → procent Start
Svårighetsgrad 2+
– Fråga användaren innan beräkningen vilken precision den önskar! Hela pro- cent, tiondels procent, hundradels procent!
– Skriv sedan ut svar efter önskad precision Kolla in strängformatering!










start_Värde = int(input("kan du skriva in start värde: "))
nuvarande_Värde = int(input("Kan du skriva in nuvarande värde: "))
svar = input('\nvill du räkna hela procent eller hundradedel eller tionde del: ').lower()
procent = ((nuvarande_Värde-start_Värde)/start_Värde)*100



if svar == 'hela':
 print('\n hela procent är: ', procent)

elif svar == 'tionde del':
 print('\n tionde del är: ',round(procent,1))

elif svar =='hundradedel':
 print('\n hundradedel är: ',round(procent,2))

else:
  print('\ndu ska välja mellan hela procent, tionde del eller hundradedel')

   

