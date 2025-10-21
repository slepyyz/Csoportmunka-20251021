import fuggvenyek

etelek=[
    {"nev": "Húsleves", "ar": 1999, "tipus": "eloetel"},
    {"nev": "Gyümölcsleves", "ar": 3499, "tipus": "eloetel"},
    {"nev": "Paradicsomleves", "ar": 2499, "tipus": "eloetel"},
    {"nev": "Steak", "ar": 1999, "tipus": "foetel"},
    {"nev": "Körömpörkölt", "ar": 3499, "tipus": "foetel"},
    {"nev": "The fortress Stilt Fisherman Idulgence", "ar": 5600000, "tipus": "foetel"}
]

foodlista=[]

fuggvenyek.kiiras(etelek)
foodlista=fuggvenyek.bekeres(etelek)
osszeg=fuggvenyek.osszegzo(foodlista)
fuggvenyek.szamlazo(foodlista,osszeg,50)