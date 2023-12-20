import math
import time
podmienka = True
while podmienka:
    print("======Vitaj v kalkulacke======")
    print("Vyber si matematicku operaciu")
    print(" 1 = Scitanie")
    print(" 2 = Odcitanie")
    print(" 3 = Nasobenie")
    print(" 4 = Delenie")
    print(" 5 = Celociselne delenie")
    print(" 6 = Druha odmocnina")
    print(" 7 = Mocnenie")
    print(" 8 = Tretia odmocnina")
    print(" 9 = Porovnavanie")
    x = int(input("Zadaj operaciu: "))
    def scitanie():
        a = int(input("Zadaj prvé číslo: "))
        b = int(input("Zadaj druhé číslo: "))
        print("Sčítanie je: ", a + b)
    if x == 1:
        delenie()
    def odcitanie():
        a = int(input("Zadaj prvé číslo: "))
        b = int(input("Zadaj druhé číslo: "))
        print("Odčítanie je: ", a - b)
    if x == 2:
        delenie()
    def nasobenie():
        a = int(input("Zadaj prvé číslo: "))
        b = int(input("Zadaj druhé číslo: "))
        print("Násobenie je: ", a * b)
    if x == 3:
        delenie()
    def delenie():
        a = int(input("Zadaj prvé číslo: "))
        b = int(input("Zadaj druhé číslo: "))
        print("Delenie je", a/b)
    if x == 4:
        delenie()
    def celociselne_delenie():
        a = int(input("Zadaj prvé číslo: "))
        b = int(input("Zadaj druhé číslo: "))
        print("Celočíselné delenie je: ", a // b)
    if x == 5:
        celociselne_delenie()
    def odmocnina():
        a = int(input("Zadaj číslo: "))
        print("Druhá odmocnina je: ", math.sqrt())
    if x == 6:
        odmocnina()
    def mocnenie():
        a = int(input("Zadaj číslo: "))
        print("Mocnenie je: ", math.pow)






    if x == 7:
        print("Mocnenie je:", math.pow(f, g))
    if x == 8:
        print("Tretia odmocnina cisla je:", math.cbrt(h))
    if x == 9:
        podmienkaporov1 = input("Chces zistit ci je prve cislo vacsie ako druhe alebo naopak? (ano/naopak): ")
        if podmienkaporov1 == "ano":
            print(bool(a > b))
        if podmienkaporov1 == "naopak":
            print(bool(b > a))

    podmienka1 = input("Napis ano alebo nie ak chces pokracovat: ")
    if podmienka1 == "nie":
        print("Dakujeme za pouzivanie nasej kalkulacky")
        time.sleep(3)
        break

