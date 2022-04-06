print(" 1 Mt. Fuji \n 2 Tokiói torony \n 3 Kinkakudzsi \n 4 Himedzsi várkastély \n 5 Hirosimai Atombomba-dóm \n 6 The Great Wall of China \n 7 Lungmen-barlangok \n 8 Putung \n 9 Wudang-hegység \n 10 Hszian \n 11 Ocean Park Hong Kong \n 12 Viktória Csúcs \n 13 Wong Tai Sin templom \n 14 Tízezer Buddha-kolostor \n 15 Arany Bauhinia tér \n 16 Tanah Lot \n 17 Toba-tó \n 18 Borobudur \n 19 Gardens by the Bay \n 20 Merlion \n 21 A fog temploma \n 22 Amber erőd \n 23 Lake Palace \n 24 Váránaszi \n 25 Tádzs Mahal")
valasz = int(input("Válassz az érdekességek közűl: "))
asia = open("asia.txt","r",encoding = "utf-8")
ListaAsia = []
for sor in asia:
    kisLista = sor[:-1].split(";")
    ListaAsia.append(kisLista)
asia.close()
print(ListaAsia[valasz])