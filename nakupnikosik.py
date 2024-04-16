print ("Vítejte na webové stránce oblock zde můžete zakoupit pc komponenty")

zbozi = ["RYZEN 7 800x3d", "NVIDIA 4070ti", "CORSAIR Vengeance RGB DDR4 32GB", "GIGABYTE zdroj UD750GM, 750W", "Asus ROG MAXIMUS Z790 HERO"]
kosik = []

def vypis_1():
    print("---------------------------")
    print(" ")
    print("Zde je zboží")
    print(" ")
    print("---------------------------")

def vypis_2():
    print("---------------------------")
    print(" ")
    print("Zde jsou vaše vybrané produkty")
    print(" ")
    print("---------------------------")

def vypis_3(prvek):
    
    for x in range(len(prvek)): 
        print(f"Komponent s číslem {x+1}: {prvek[x]}")
    
    print(" ")
    print("---------------------------")


while(True):
    vypis_1()
    vypis_3(zbozi)

    vyber = int(input("Zde zadejte Vaší volbu produktu podle čísla: "))

    if 0<vyber<=len(zbozi):
        kosik.append(zbozi[vyber])
        vypis_2()
        vypis_3(kosik)
        zbozi.pop(vyber)
                