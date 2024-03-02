
Chat with me!
• Tryck på File, New file
• Tryck på File, Save as ’ChatWithMe_1.py’
• I filen skriver vi MY_NAME = ’< name >’ Ditt egna namn alltså! Notera understrecket
• Under skriver vi MY_AGE = < age > Din ålder, notera int() och understrecket
• Under det skriver vi MY_HOBBY = < hobby > Din hobby, notera understrecket
• Under det skriver vi name = input(’Skriv in ditt namn: ’)
• Under det skriver vi age = int(input(’Skriv in din ålder: ’))
• Under det skriver vi hobby = input(’Skriv in din favorithobby: ’)
• Under det skriver vi print(f’Hejsan {name}, mitt namn är {MY_NAME}.’)
• Under det skriver vi print(f’Du är {age} gammal och jag är {MY_AGE}.’)
• Under det skriver vi print(f’Jag gillar {MY_HOBBY} och du gillar{hobby}.’)
• Under det skriver vi print(f’Trevligt att pratas vid {name}, hoppas vi hörs snart igen!’)
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Skriv ett fake-< name > och tryck Enter Skriv en fake-< age > och tryck Enter Skriv en fake-< hobby > oich tryck Enter
Svårighetsgrad 2
– Skriv ut namnen med stora bokstäver!
– Beräkna skillanden i ålder och avgör om du är äldre eller yngre än använda-
ren.
– Svara användaren om ni har samma hobby eller inte!
 


 
mitt_Name = 'Rajneet Kaur'
mitt_Ålder = 33
mitt_Hobby = 'Badminton'
ditt_Name = input("skriv in ditt namn: ").upper()
ditt_Ålder = int(input("skriv in ditt ålder: "))
ditt_Hobby = input("skriv in ditt hobby: ")


print(f"Hejsan {ditt_Name}, my name is {mitt_Name}")

print(f"du är {ditt_Ålder} gammal och jag är {mitt_Ålder}")
if ditt_Ålder>mitt_Ålder:
    print("du är äldre än mig")
elif ditt_Ålder<mitt_Ålder:
    print("print du är yngre än mig")
else:
    print("vi är samma ålder")

print(f"jag gillar {mitt_Hobby} och du gillar {ditt_Hobby} ")   
if mitt_Hobby == ditt_Hobby:
    print("vi har samma hobby")
else:
    print(" vi har inte samma hobby")

print(f"Trevligt att pratas vid {ditt_Name}, hoppas att vi ses igen!") 
