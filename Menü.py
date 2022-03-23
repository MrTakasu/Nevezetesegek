print(" Ha Amerika nevezetességeit akarja látni nyomja meg az egyes gombot. \n Ha Európa nevezetességeit akarja látni nyomja meg a kettes gombot. \n Ha Ázsia nevezetességeit akarja látni nyomja meg a hármas gombot. \n Ha véleményt szeretne írni nyomja meg a négyes gombot ")
Valasztas=int(input())
if Valasztas==1:
    print(Amerika())
elif Valasztas==2:
    print(Európa())
elif Valasztas==3:
    print(Ázsia())
elif Valasztas==4:
    print("Ez a funkció nem létezik")
else:
    print("Nem tudtuk azonosítani")    