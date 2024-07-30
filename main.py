from datetime import date
from models import Jugador, Arbitro, Equipo, Campeonato, Resultado, TablaPosiciones

def main():
    jugador1 = Jugador("Perez", "12345678", date(2000, 1, 1), "Ecuador", "Juan", True, "A", 10)
    jugador2 = Jugador("Gomez", "87654321", date(1999, 2, 2), "Ecuador", "Carlos", True, "A", 9)

    equipo = Equipo("Centro", "Rojo", True, "Los Rojos", "Pedro Perez")
    equipo.agregar_jugador(jugador1)
    equipo.agregar_jugador(jugador2)

    campeonato1 = Campeonato("Liga 2024", 90, date(2024, 1, 1), date(2024, 12, 31), "M", 4, 2, 2)
    campeonato2 = Campeonato("Copa 2024", 90, date(2024, 1, 1), date(2024, 12, 31), "M", 4, 2, 2)

    campeonato1.agregar_equipo(equipo)

    jugador3 = Jugador("Lopez", "23456789", date(2001, 3, 3), "Ecuador", "Luis", True, "B", 11)
    jugador4 = Jugador("Ramirez", "98765432", date(2002, 4, 4), "Ecuador", "Miguel", True, "B", 12)
    equipo2 = Equipo("Centro", "Rojo", True, "Los Rojos", "Pedro Perez")
    equipo2.agregar_jugador(jugador3)
    equipo2.agregar_jugador(jugador4)

    campeonato2.agregar_equipo(equipo2)

    resultado1 = Resultado(equipo, equipo2, 2, 2)
    campeonato1.registrar_resultado(resultado1)

    tabla_posiciones = TablaPosiciones(campeonato1)
    tabla_posiciones.actualizar()
    print("Tabla de posiciones Campeonato 1:")
    for posicion in tabla_posiciones.mostrar():
        print(posicion)

if __name__ == "__main__":
    main()