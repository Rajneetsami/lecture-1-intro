
Tre luringar!
• Tryck på File, New file
• Tryck på File, Save as ’TreLuringar_1.py’
• I filen skriver vi print(’Skriv in tre heltal!’)
• Under skriver vi num1 = input(’Skriv tal 1: ’)
 • Under det skriver vi
• Under det skriver vi
• Under det skriver vi
• Under det skriver vi
• Under det skriver vi
• Under det skriver vi
num2 = input(’Skriv tal 2: ’)
num3 = input(’Skriv tal 3: ’)
print(f’Att {num1} är större än {num2} är {num1>num2}’) print(f’Att {num2} är större än {num3} är {num2>num3}’) print(f’Att {num3} är större än {num1} är {num3>num1}’)print(f’Medelvärdet av {num1} , {num2} och {num3} är {(num1+num2+num3)/3}’)
• Tryck på File, Save
• Tryck på F5 eller ’play’ knappen i höger hörn så körs programmet
Skriv ett fake-< name > och tryck Enter Svårighetsgrad 2
– Skriv ut talen i ordningen störst till minst
– Kontrollera om användaren skrev in negativa tal, om så fallet, skriv ut detta
med ett fint meddelande till användaren!
– Kontrollera om något/alla talen är lika. Om så fallet berätta det för använ- daren





print("skriv in tre heltal")

num1 = int(input('skriv tal1: '))
num2 = int(input("skriv tal2: "))
num3 = int(input("skriv tal3: "))

list_Number = [num1,num2,num3]
list_Number_sorted = sorted(list_Number)
print(list_Number)
print(list_Number_sorted)

# print(f"att {num1} är större än {num2} är {num1>num2}")
# print(f"att {num2} är större än {num3} är {num2>num3}")
# print(f"att {num3} är större än {num1} är {num3>num1}")

# print(f" medelvärdet är {num1}, {num2} och {num3} är {(num1+num2+num3)/3}")

# if num1<0 or num2<0 or num3<0:
#     print('du har använt negativa tal också')

# if num1==num2 or num2==num3 or num3==num1 or num1==num2==num3:
#     print("vi har talet som är lika med varandra")

    
