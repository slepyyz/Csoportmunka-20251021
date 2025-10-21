

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