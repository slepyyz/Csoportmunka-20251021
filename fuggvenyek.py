

def osszegzo(foodlista):
    osszeg = 0
    hossz = 0
    while hossz < len(foodlista):
        osszeg += foodlista[hossz]["ar"]
        hossz += 1
    return osszeg

def szamlazo(foodlista,osszeg):
    print("=" * 50)
    print(" " * 20 + "Hekk Tuah")
    print("=" * 50)
    hossz=0
    print()
    print("-" *50)
    print(f"{'VÉGÖSSZEG:':<30} {osszeg:>16} Ft")
    print("=" * 50)
    print()
    print(" "* 14 + "Köszönjük a vásárlását!")
    print("=" * 50)