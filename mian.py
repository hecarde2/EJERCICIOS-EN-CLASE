#voltear texto sin range

texto = input("ingrese texto  ")
invertir = ""

for letra in texto:
    invertir = letra + invertir
    print(f"texto invertido: {invertir}" )