import random


Tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
JugadorActual = "X"
Ganador = None
correJuego = True

#1
def ImprimirTablero(Tablero):
    print(Tablero[0] + " | " + Tablero[1] + " | " + Tablero[2])
    print("---------")
    print(Tablero[3] + " | " + Tablero[4] + " | " + Tablero[5])
    print("---------")
    print(Tablero[6] + " | " + Tablero[7] + " | " + Tablero[8])


#2
def entradaJugador(Tablero):
    inp = int(input("Selecciona un lugar 1-9:" ))
    if Tablero[inp-1] == "-":
        Tablero[inp-1] = JugadorActual
    else:
        print("ups, el jugador ya esta en ese lugar.")


#3
def ComprobarHorizontal(Tablero):
    global Ganador
    if Tablero[0] == Tablero[1] == Tablero[2] and Tablero[0] != "-":
        Ganador = Tablero[0]
        return True
    elif Tablero[3] == Tablero[4] == Tablero[5] and Tablero[3] != "-":
        Ganador = Tablero[3]
        return True
    elif Tablero[6] == Tablero[7] == Tablero[8] and Tablero[6] != "-":
        Ganador = Tablero[6]
        return True

def ComprobarVeretical(Tablero):
    global Ganador
    if Tablero[0] == Tablero[3] == Tablero[6] and Tablero[0] != "-":
        Ganador = Tablero[0]
        return True
    elif Tablero[1] == Tablero[4] == Tablero[7] and Tablero[1] != "-":
        Ganador = Tablero[1]
        return True
    elif Tablero[2] == Tablero[5] == Tablero[8] and Tablero[2] != "-":
        Ganador = Tablero[3]
        return True


def ComprobarDiagonal(Tablero):
    global Ganador
    if Tablero[0] == Tablero[4] == Tablero[8] and Tablero[0] != "-":
        Ganador = Tablero[0]
        return True
    elif Tablero[2] == Tablero[4] == Tablero[6] and Tablero[4] != "-":
        Ganador = Tablero[2]
        return True


def ComprobarSiGana(Tablero):
    global correJuego
    if ComprobarHorizontal(Tablero):
        ImprimirTablero(Tablero)
        print(f"el ganador es {Ganador}!")
        correJuego = False

    elif ComprobarVeretical(Tablero):
        ImprimirTablero(Tablero)
        print(f"el Ganador es {Ganador}!")
        correJuego = False

    elif ComprobarDiagonal(Tablero):
        ImprimirTablero(Tablero)
        print(f"el Ganador es {Ganador}!")
        correJuego = False


def ComprobarSiEmpate(Tablero):
    global correJuego
    if "-" not in Tablero:
        ImprimirTablero(Tablero)
        print("Es un Empate!")
        correJuego = False


#4
def CambiarJugador():
    global JugadorActual
    if JugadorActual == "X":
        JugadorActual = "O"
    else:
        JugadorActual = "X"


def LaCompu(Tablero):
    while JugadorActual == "O":
        position = random.randint(0, 8)
        if Tablero[position] == "-":
            Tablero[position] = "O"
            CambiarJugador()


while correJuego:
    ImprimirTablero(Tablero)
    entradaJugador(Tablero)
    ComprobarSiGana(Tablero)
    ComprobarSiEmpate(Tablero)
    CambiarJugador()
    LaCompu(Tablero)
    ComprobarSiGana(Tablero)
    ComprobarSiEmpate(Tablero)