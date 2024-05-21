import random
def main():
    levesek = [
        "Gyümölcsleves",
        "Zöldborsóleves",
        "Paradicsomleves",
        "Gulyásleves",
        "Bableves",
        "Zöldbableves",
        "Karfiolleves",
        "Brokkolikrémleves",
        "Zöldségleves",
        "Erőleves",
        "Húsleves",
        "Halászlé"
    ]
    foetelek = [
        "Rántott hús",
        "Rántott sajt",
        "Rántott gomba",
        "Bolognai spagetti",
        "Csirkepaprikás",
        "Vadaspörkölt",
        "Pacalpörkölt",
        "Krumplifőzelék fasírttal",
        "Túrós csusza",
        "Lecsó",
        "Rakott krumpli",
        "Rakott karfiol"
    ]
    days = int(input("Adja meg, hogy hány nap adatait szeretné megadni: "))
    menu_foetel = []
    menu_leves = []
    meal_ratings = []
    for i in range(days):
        print()
        print(f"{i+1}. nap")
        menu_leves.append(random.choice(levesek))
        menu_foetel.append(random.choice(foetelek))
        print(f"Leves: {menu_leves[i]}")
        print(f"Főétel: {menu_foetel[i]}")
        print()
        meal_ratings.append(rate_meal(menu_leves[i], menu_foetel[i]))
        
    fav_levesek, fav_foetelek = fav_meals(menu_leves, menu_foetel, meal_ratings)
    print()
    print("Kedvenc levesek:")
    for i in fav_levesek:
        print(i)
    if len(fav_levesek) == 0:
        print("Nincs kedvenc leves")
    print()
    print("Kedvenc főételek:")
    for i in fav_foetelek:
        print(i)
    if len(fav_foetelek) == 0:
        print("Nincs kedvenc főétel")
    print()
    bad_levesek, bad_foetelek = bad_meals(menu_leves, menu_foetel, meal_ratings)
    print("Nem kedvelt levesek:")
    for i in bad_levesek:
        print(i)
    if len(bad_levesek) == 0:
        print("Nincs nem kedvelt leves")
    print()
    print("Nem kedvelt főételek:")
    for i in bad_foetelek:
        print(i)
    if len(bad_foetelek) == 0:
        print("Nincs nem kedvelt főétel")
    print()
    print("Értékelések:")
    for i in range(days):
        print(f"{i+1}. nap")
        print(f"Leves: {menu_leves[i]} - {meal_ratings[i][0]}")
        print(f"Főétel: {menu_foetel[i]} - {meal_ratings[i][1]}")
        print()
    
    
    
    
def rate_meal(leves, foetel):
    students = int(input("Hány diák értékelte a mai menüt? "))
    leves_rating = 0
    foetel_rating = 0
    for i in range(students):
        while True:
            rate = int(input(f"{i+1}. diák értékelése a levesre ami {leves} volt (1-5): "))
            if rate < 1 or rate > 5:
                print("Hibás érték!")
            else:
                leves_rating += rate
                break
        while True:
            rate = int(input(f"{i+1}. diák értékelése a levesre ami {foetel} volt (1-5): "))
            if rate < 1 or rate > 5:
                print("Hibás érték!")
            else:
                foetel_rating += rate
                break
    leves_rating /= students
    foetel_rating /= students
    return leves_rating, foetel_rating
    
def fav_meals(menu_leves, menu_foetel, meal_ratings):
    fav_levesek = []
    fav_foetelek = []
    for i in range(len(meal_ratings)):
        if meal_ratings[i][0] > 3.5:
            fav_levesek.append(menu_leves[i])
        if meal_ratings[i][1] > 3.5:
            fav_foetelek.append(menu_foetel[i])
    return fav_levesek, fav_foetelek

def bad_meals(menu_leves, menu_foetel, meal_ratings):
    bad_levesek = []
    bad_foetelek = []
    for i in range(len(meal_ratings)):
        if meal_ratings[i][0] < 2.5:
            bad_levesek.append(menu_leves[i])
        if meal_ratings[i][1] < 2.5:
            bad_foetelek.append(menu_foetel[i])
    return bad_levesek, bad_foetelek

main()