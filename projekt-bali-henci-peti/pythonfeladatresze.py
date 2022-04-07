#------------[Alapvető listák/Adatok]------------#
nevek = [] # Ide tároljuk el az eszköz nevét(1. input)
arak = [] # Ide tároljuk el az eszköz beszerzési árát(2. input)
darabok = [] # Ide tároljuk el hogy mennyit szándékozunk vásárolni(3. input)
try:
    adat = int(input("Adja meg hogy hány darab eszközt szeretne hozzáadni!: ")) # Megkérdezzük hogy mennyi eszközt szeretne elmenteni
except:
    print("|HIBA!| Ügyeljen hogy csak egész számokat írjon!")
aki = [] # Ide mentjük el a teljes szöveget

#------------[Fő program amely kalkulál]------------#

def arkalkulacio():
    for i in range(0, adat): #Lefuttatja többször(amennyit megadtunk) a kérdéseket
        adat1 = str(input("Adja meg az eszköz nevét! Név: ")) # Megkérdezzük az eszköz nevét
        try:
            adat2 = int(input("Adja meg az eszköz beszerzési árát! Ára: ")) # Megkérdezzük az eszköz árát
            adat3 = int(input("Adja meg az eszköz darabszámát! Db: ")) # Megkérdezzük hogy mennyit szeretne vásárolni
        except:
            print("|HIBA!| Az adatok között volt egy betü! Ügyeljen arra hogy csak egész számokat írjon!")
        nevek.append(str(adat1)) # elmentjük a nevét
        arak.append(str(adat2)) # árát
        darabok.append(str(adat3)) # darabszámát
        a = str(adat1) + " költségvetése: " + str(adat2*adat3) # Alap szöveg
        aki.append(a) # Elmentjük a listába a szöveget
    f=open("Koltsegvetes.txt","w",encoding="UTF-8")
    for i in range(0, adat): #Lefuttatja többször(amennyit megadtunk) a szöveget 

        
        print("--------------------------") # Díszítés
        print() #Semmi
        print(aki[i]) #Szöveg az adott elemnél
        print() #Semmi
        print("--------------------------") #Díszítés
        f.write(aki[i]+"\n")
    f.close()

#------------[Meghívjuk a promgramot hogy lefusson]------------#                                                                                                                                                                                                                                                                                                                                                                        :D megtalált :D
arkalkulacio()
