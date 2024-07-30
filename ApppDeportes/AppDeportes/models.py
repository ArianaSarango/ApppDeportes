from django.db import models

class Persona(models.Model):
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    sexo = models.BooleanField()

class Jugador(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)
    numero_camisa = models.IntegerField()

class Arbitro(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    anios_experiencia = models.IntegerField()

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    nombre_representante = models.CharField(max_length=100)
    color_uniforme = models.CharField(max_length=50)
    genero = models.BooleanField()

class Disciplina(models.Model):
    nombre_disciplina = models.CharField(max_length=50)

class Puntuacion(models.Model):
    puntos_derrota_sin_jugar = models.IntegerField()
    puntos_por_empate = models.IntegerField()
    puntos_por_perdida = models.IntegerField()
    puntos_por_victoria = models.IntegerField()

class TablaPosiciones(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey('Campeonato', on_delete=models.CASCADE)
    posicion = models.IntegerField()
    partidos_jugados = models.IntegerField()
    puntos = models.IntegerField()

class Jornada(models.Model):
    nombre = models.CharField(max_length=100)

class ProgramacionJuego(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_inicio_inscripcion = models.DateField()
    fecha_fin_inscripcion = models.DateField()
    genero = models.BooleanField()
    numero_clasificados_por_grupo = models.IntegerField()
    numero_equipos_por_grupo = models.IntegerField()
    numero_grupo = models.IntegerField()

class InscripcionEquipo(models.Model):
    fecha_inscripcion = models.DateField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

class InscripcionJugador(models.Model):
    fecha_inscripcion = models.DateField()
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

class Escenario(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Encuentro(models.Model):
    fecha_encuentro = models.DateField()
    tipo_evento = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    escenario = models.ForeignKey(Escenario, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    equipo1 = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo1')
    equipo2 = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo2')
    marcador_equipo1 = models.IntegerField(default=0)
    marcador_equipo2 = models.IntegerField(default=0)

class NominaEncuentro(models.Model):
    encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)
    titularidad = models.BooleanField()

class Resultado(models.Model):
    marcador = models.CharField(max_length=50)
    nombre_goleador = models.CharField(max_length=100)
    encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)

class Amonestacion(models.Model):
    color_tarjeta = models.CharField(max_length=50)
    nomina_encuentro = models.ForeignKey(NominaEncuentro, on_delete=models.CASCADE)
