# Tema 5: Batalha Naval Simplificada
import random
barco_linha = random.randint(0, 4)
barco_coluna = random.randint(0, 4)

tiro_l = int(input("Atirar na linha (0-4): "))
tiro_c = int(input("Atirar na coluna (0-4): "))

if tiro_l == barco_linha and tiro_c == barco_coluna:
    print("POW! Acertou o navio!")
else:
    print(f"Água! O barco estava em ({barco_linha}, {barco_coluna})")