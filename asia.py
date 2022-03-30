def Asia():
    print("")
    valasz = int(input("Vélassz az érdekességek közűl: "))
    asia = open("Asian_Attractions","r")
    ListaAsia = []
    for sor in asia:
        kisLista = sor[:-1].split(";")
        ListaAsia.append(kisLista)
    Asia.close()
    print(ListaAsia[valasz])
Asia()