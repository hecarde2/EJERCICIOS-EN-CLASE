print("========JUNIOR=========")
partido_jugado = int(input(f"INGRESE LA CANTIDAD DE PARTIDOS JUGADOS"))
partido_ganado = 0
partido_empatado = 0
partido_perdido = 0 
goles_a_favor = 0
goles_en_contra = 0
puntos = 0
pierde_punto = 0
total_goles_a_favor = 0
total_goles_en_contra = 0
total_partidos_ganados = 0
total_partidos_perdidos = 0
total_partidos_empatados = 0
total_diferencia_goles = 0

for i in range(partido_jugado):
    print("PARTIDO DEL JUNIOR")

    goles_a_favor = int()(input(f"INGRESE GOLES A FAVOR:    "))
    goles_en_contra = int(input(f"INGRESE LOS GOLES EN CONTRA:   "))
    total_goles_a_favor += goles_a_favor
    total_goles_en_contra += goles_en_contra


    if goles_a_favor > goles_en_contra:
        partido_ganado += 1
        puntos += 3
        total_partidos_ganados += 1

    elif goles_a_favor == goles_en_contra:
         partido_empatado += 1
         puntos += 1
         total_partidos_empatados +=1

    else:
        goles_a_favor < goles_en_contra
        partido_perdido += 1
        total_partidos_perdidos += 1

    diferencia_goles = (goles_a_favor - goles_en_contra)




    print("RESULTADOS DE JUNIOR")
    print("total de partidos jugados", partido_jugado)
    print("partidos ganados", total_partidos_ganados)
    print("partidos perdidos", total_partidos_perdidos)
    print("goles a favor", total_goles_a_favor)
    print("goles en contra", total_goles_en_contra)
    print("diferencia de goles", diferencia_goles)
    print("puntos del junior", puntos)




