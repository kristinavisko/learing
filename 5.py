"""Zatražiti od korisnika unos njegove godine rođenja. Izračunati starost korisnika i ispisati
odgovarajuću poruku (‘Punoljetni ste’/’Niste punoljetni’). Ne uzeti u obzir ako korisnik
unese nevaljanu godinu (npr. 2016) - u tom slučaju ispisati odgovarajuću poruku."""

year = int(input("Insert year of birth"))
if year >= 2014:
    print ("Please insert real year")
else:
    old = 2018 - year
    print ("You are:", old, "years old")
    if old > 18:
        print ("Punoljetni ste")
    else:
        print ("Maloljetni ste")

