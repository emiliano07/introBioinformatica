#RETO VII

proteina_diminuta = 'ATGGAAGTTGGAATCCAAGTTGGA'
rana_terrestre = 'ATGGAAGTTAATGGAAGTTGGAGGAGA'

if len(proteina_diminuta) > len(rana_terrestre):
    print("El gen de la proteina diminuta es mas grande!")
elif len(proteina_diminuta) < len(rana_terrestre):
    print("El gen de una proteína similar de rana terrestre es mas grande!")
else:
    print("Los dos genes son iguales!")


#RETO IX

cant_clones = 0

for i in range(0,20):
    cant_clones += 1
    print("¡Somos " + str(cant_clones * 2) + " clones!")
