import random


lista_DNI = [1611,1688,2659,1613,1613,1628,1562,1111,1613,1658]

lista_nombres = ["lorena", "Fernando", "Mariana", "Maximo","Daniel","Ariel","Cristina","Santiago","Carlos","Iván"]

lista_apellidos = ["Perez", "Espinosa", "Naniz", "Fernandez", "Lancha", "Negro", "Vholve","Father","Enrique","Yeoman"]

lista_edad = [1,23,11,58,74,6,42,99,28,68]


def azar_pos(lista):

    pos = random.randint(0, len(lista_DNI)-1)

    return pos

posicion_azar = azar_pos(lista_DNI)


persona_azar = lista_DNI[posicion_azar], lista_nombres[posicion_azar], lista_apellidos[posicion_azar]


if lista_edad[posicion_azar] > 65:
        salida = "No apto"

elif lista_edad[posicion_azar] < 16:
        salida = "Menor"

else:
    salida = "a sorteo"



print(salida, persona_azar)


































