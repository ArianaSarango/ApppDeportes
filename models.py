from datetime import date
from typing import List, Optional

class Persona:
    def __init__(self, apellido: str, cedula: str, fecha_nacimiento: date, nacionalidad: str, nombre: str, sexo: bool):
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.sexo = sexo

class Jugador(Persona):
    def __init__(self, apellido: str, cedula: str, fecha_nacimiento: date, nacionalidad: str, nombre: str, sexo: bool, categoria: str, numero_camiseta: int):
        super().__init__(apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo)
        self.categoria = categoria
        self.numero_camiseta = numero_camiseta

class Arbitro(Persona):
    def __init__(self, apellido: str, cedula: str, fecha_nacimiento: date, nacionalidad: str, nombre: str, sexo: bool, anios_experiencia: int):
        super().__init__(apellido, cedula, fecha_nacimiento, nacionalidad, nombre, sexo)
        self.anios_experiencia = anios_experiencia

class Equipo:
    def __init__(self, barrio: str, color_uniforme: str, genero: bool, nombre_equipo: str, nombre_representante: str):
        self.barrio = barrio
        self.color_uniforme = color_uniforme
        self.genero = genero
        self.nombre_equipo = nombre_equipo
        self.nombre_representante = nombre_representante
        self.jugadores: List[Jugador] = []

    def agregar_jugador(self, jugador: Jugador):
        self.jugadores.append(jugador)

class Campeonato:
    def __init__(self, nombre: str, duracion_compromiso: int, fecha_inicio: date, fecha_fin: date, genero: str, numero_clasificados_por_grupo: int, numero_equipos_por_grupo: int, numero_grupo: int):
        self.nombre = nombre
        self.duracion_compromiso = duracion_compromiso
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.genero = genero
        self.numero_clasificados_por_grupo = numero_clasificados_por_grupo
        self.numero_equipos_por_grupo = numero_equipos_por_grupo
        self.numero_grupo = numero_grupo
        self.equipos: List[Equipo] = []
        self.resultados: List[Resultado] = []

    def agregar_equipo(self, equipo: Equipo):
        self.equipos.append(equipo)

    def registrar_resultado(self, resultado: 'Resultado'):
        self.resultados.append(resultado)

class Resultado:
    def __init__(self, equipo1: Equipo, equipo2: Equipo, marcador1: int, marcador2: int):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.marcador1 = marcador1
        self.marcador2 = marcador2

    def es_empate(self):
        return self.marcador1 == self.marcador2

class TablaPosiciones:
    def __init__(self, campeonato: Campeonato):
        self.campeonato = campeonato
        self.posiciones = {equipo.nombre_equipo: {'partidos_jugados': 0, 'puntos': 0} for equipo in campeonato.equipos}

    def actualizar(self):
        for resultado in self.campeonato.resultados:
            equipo1 = resultado.equipo1.nombre_equipo
            equipo2 = resultado.equipo2.nombre_equipo
            self.posiciones[equipo1]['partidos_jugados'] += 1
            self.posiciones[equipo2]['partidos_jugados'] += 1
            if resultado.es_empate():
                self.posiciones[equipo1]['puntos'] += 1
                self.posiciones[equipo2]['puntos'] += 1
            else:
                if resultado.marcador1 > resultado.marcador2:
                    self.posiciones[equipo1]['puntos'] += 3
                else:
                    self.posiciones[equipo2]['puntos'] += 3

    def mostrar(self):
        return sorted(self.posiciones.items(), key=lambda x: x[1]['puntos'], reverse=True)