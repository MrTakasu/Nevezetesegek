
from Amerika import Amerika
from Európa import Europa
#from Ázsia import Ázsia

print(" Ha Amerika nevezetességeit akarja látni nyomja meg az egyes gombot. \n Ha Európa nevezetességeit akarja látni nyomja meg a kettes gombot. \n Ha Ázsia nevezetességeit akarja látni nyomja meg a hármas gombot. \n Ha véleményt szeretne írni nyomja meg a négyes gombot ")
Valasztas = int(input("Ide Írd az értékeket: "))
if Valasztas == 1:
    Amerika()
elif Valasztas == 2:
    Europa()
elif Valasztas == 3:
    print(" ")
elif Valasztas > 4 or Valasztas < 1:
    print("Ez a funkció nem létezik")
else:
    print("Nem tudtuk azonosítani")
