sex = input('[k]obieta czy [m]ezczyzna ?:')
if sex.isdigit() =="k":
    print("mozesz uzywac aplikacji Droga pani")
else:
    print("ej to jest tylko dla kobiet")
    exit("koniec")






wiek = input("Podaj wiek: ")

# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 21 and wiek <= 65:
    print("Witamy!")
elif wiek > 65:
    print("Jesteś już za starya na alkohol")
else:
    exit('jesteś za młoda!. w USA wymagany jest 21 lat!')





    
