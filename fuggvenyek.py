etelek=[
    {"nev": "Húsleves", "ar": 1999, "tipus": "eloetel"}
    {"nev": "Gyümölcsleves", "ar": 3499, "tipus": "eloetel"}
    {"nev": "Paradicsomleves", "ar": 2499, "tipus": "eloetel"}
    {"nev": "Steak", "ar": 1999, "tipus": "foetel"}
    {"nev": "Körömpörkölt", "ar": 3499, "tipus": "foetel"}
    {"nev": "The fortress Stilt Fisherman Idulgence", "ar": 5600000, "tipus": "foetel"}
]
def szamlazo(foodlista):
    print("=" * 50)
    print(" " * 20 + "Hekk Tuah")
    print("=" * 50)
    osszeg=0
    index=0
    print()
    print("-" *50)
    print(f"{'VÉGÖSSZEG:':<30} {osszeg:>16} Ft")
    print("=" * 50)
    print()
    print(" "* 14 + "Köszönjük a vásárlását!")
    print("=" * 50)
    

def osszegzo(foodlista):
    osszeg = 0
    hossz = 0
    while hossz < len(foodlista):
        osszeg += foodlista[hossz]["ar"]
        hossz += 1
    return osszeg
