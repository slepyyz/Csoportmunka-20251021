def osszegzo(foodlista):
    osszeg = 0
    hossz = 0
    while hossz < len(foodlista):
        osszeg += foodlista[hossz]["ar"]
        hossz += 1
    return osszeg

def szamlazo(foodlista,osszeg,hossz):
    print("=" * hossz)
    print(" " * 20 + "Hekk Tuah")
    print("=" * hossz)
    print()
    print("-" * hossz)
    print(f"{'VÉGÖSSZEG:':<30} {osszeg:>16} Ft")
    print("=" * hossz)
    print()
    print(" "* 14 + "Köszönjük a vásárlását!")
    print("=" * hossz)

def bekeres(etelek):
    foodlista=[]
    etel=int(input("Mit eszel!?: "))
    while etel != 100:
        foodlista.append(etelek[etel])
        etel=int(input("Mit eszel!?: "))

    return foodlista
def kiiras():
    print("Üdvözöljük az Éttermünkben!")
    valasz=input("Előételt vagy Főételt szeretne fogyasztani?")
    if valasz == "Előétel":
        print("Mai választások: Húsleves, Gyümölcsleves, Paradicsomleves")
    elif valasz == "Főétel":
        print("Mai választások: Steak, Körömpörkölt, The Fortress Stilt Fisherman Idulgence")