"""Zatražiti od korisnika da unese broj. Ukoliko je paran, ispisati sve brojeve unatrag od
unesenog do 1, u suprotnom, zbrojiti sve brojeve od 1 do unesenog broja."""
x = int(input("Insert nuber"))
i = x
suma = 0
if x % 2 == 0:
    while i >= 1:
        print (i)
        i -= 1
else:
    while i >= 1:
        suma += i
        i -= 1
    print (suma)