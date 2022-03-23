def Amerika():
    print(" 1 Rushmore-hegy \n 2 Kennedy Űrközpont (Kennedy Space Center) \n 3 Bryce Canyon Nemzeti Park \n 4 Disneyland (Orlando) \n 5  A Fehér-ház (Washington D.C.) \n 6  Kilauea \n 7 Niagara-vízesés \n 8 Golden Gate híd (San Francisco) \n 9 Yellowstone \n 10 Grand Canyon")
    valasz = int(input("Vélassz az érdekességek közűl: "))
    amerika = open("Amerika látvanyosgágok.txt","r")
    ListaAmerika = []
    for sor in amerika:
        kisLista = sor[:-1].split(";")
        ListaAmerika.append(kisLista)
    amerika.close()
    print(ListaAmerika[valasz])
Amerika()