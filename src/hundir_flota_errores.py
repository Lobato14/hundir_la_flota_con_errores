import random

def crear_tablero():
    return [['O' for _ in range(5)] for _ in range(5)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()

def colocar_barcos(tablero):
    for _ in range(3):
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        tablero[fila][columna] = 'X'

def realizar_disparo(tablero, fila, columna):
    if tablero[fila][columna] == 'X':
        print("¡Tocado!")
        tablero[fila][columna] = '!'
    else:
        print("Agua")

def jugar_hundir_la_flota():
    tablero = crear_tablero()
    colocar_barcos(tablero)

    while True:
        imprimir_tablero(tablero)

        try:
            fila = int(input("Ingrese fila: "))
            columna = int(input("Ingrese columna: "))
        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

        if fila < 0 or fila >= 5 or columna < 0 or columna >= 5:
            print("Por favor, ingrese coordenadas válidas.")
            continue

        realizar_disparo(tablero, fila, columna)

        if all('X' not in fila for fila in tablero):
            print("¡Felicidades! ¡Has hundido toda la flota!")
            break

if __name__ == "__main__":
    jugar_hundir_la_flota()