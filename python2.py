odpoved1 = input("Ako sa voláš?: ")
print("Ahoj, " + odpoved1)
odpoved2 = int(input("Kolko je 9+2?: "))
if odpoved2 == 11:
    print("Múdry si!")
else:
    print("Nesprávne")
odpoved3 = input("Ako sa máš?: ")
print("To rád počujem!")
print("Napis mi dve čísla a ja ich vynásobím.")
a = int(input("Napis prvé číslo: "))
b = int(input("Napís druhé číslo: "))
odpoved4 = a * b
print("Výsledok je: " + str(odpoved4))
odpoved5 = input("Dám ti hádanku. Čo má štyri nohy, ale nehýbe sa?: ")
if odpoved5 == "stolicka":
    print("Správne!")
else:
    print("Nesprávne!")
print("Teraz ti vydelím dve čísla!")
a2 = int(input("Napíš prvé číslo: "))
b2 = int(input("Napis druhé cislo: "))
odpoved6 = a2 / b2
print("Výsledok je: " + str(odpoved6))
