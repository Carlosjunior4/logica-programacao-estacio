# Tema 4: Movimento da Torre
pos_linha = int(input("Linha da Torre (0-7): "))
pos_coluna = int(input("Coluna da Torre (0-7): "))

print(f"A Torre em ({pos_linha}, {pos_coluna}) ataca:")
for i in range(8):
    if i != pos_linha: print(f"Casa ({i}, {pos_coluna})")
    if i != pos_coluna: print(f"Casa ({pos_linha}, {i})")