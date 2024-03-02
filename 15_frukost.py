
Frukost
Skriv ett program som gör följande:
• Be användaren att skriva ner tre saker de åt till frukost
• Skriv ut en mening som säger Till frukost åt du {mat1}, {mat2} och {mat3}. Låter gott!”
Svårighetsgrad 2+
– Skriv ner några av dina favoritsaker att äta till frukost
– Jämför utifall du och användaren har samma smak när det kommer till fru-
kost! Om så fallet så ska det skrivas ut att du också gillar den matvaran!









måt1 = input('kan du skriva tre saker måt1: ')
måt2 = input('kan du skriva tre saker måt2: ')
måt3 = input('kan du skriva tre saker måt3: ')

print(f'till frukost åt du {måt1},{måt2} och {måt3}. låter gott!')

mitt_favourit_mat = ['mjölk','ägg','pankaka']

if måt1 in mitt_favourit_mat or måt2 in mitt_favourit_mat or måt3 in mitt_favourit_mat:
    print('vi gillar samma matvaran')

else:
    print('vi har olika smak sak')
