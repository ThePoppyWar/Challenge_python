with open("moj_plik.txt", "w") as f:
    for n in range(1, 101):
        f.write(str(n) + "\n")

with open("moj_plik.txt", "r") as f:
    z_pliku = f.readlines()

print(z_pliku)