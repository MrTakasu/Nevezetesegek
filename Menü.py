print(" Ha Amerika nevezetességeit akarja látni nyomja meg az egyes gombot. \n Ha Európa nevezetességeit akarja látni nyomja meg a kettes gombot. \n Ha Ázsia nevezetességeit akarja látni nyomja meg a hármas gombot. \n Ha véleményt szeretne írni nyomja meg a négyes gombot ")
Valasztas = int(input("Ide Írd az értékeket: "))
if Valasztas == 1:
    from Amerika import Amerika
    Amerika()
elif Valasztas == 2:
    from Európa import Europa
elif Valasztas == 3:
    from Asia import Asia
    Asia()
elif Valasztas > 4 or Valasztas < 1:
    print("Ez a funkció nem létezik")
else:
    print("Nem tudtuk azonosítani")
