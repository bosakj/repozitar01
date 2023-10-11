premenna1 = int(input("Zadajte cislo: "))
print(" ")
print(" ")
n = 0
print("Malá násobilka: ")
for i in range(0, 10):
                n = n + 1
                print(premenna1 * n)
                
print(" ")
print(" ")
print("Veľká násobilka: ")

n = 0
for i in range(0, 100):
    n = n + 1
    print(premenna1 * n)
print(" ")
print("Mocnina z čísla", premenna1, "je", premenna1 ** 2)


print("Násobok 4 a", premenna1, "je", premenna1 * 4)
