from django.contrib import admin

from django.contrib import admin
from .models import (
    Persona,
    Jugador,
    Arbitro,
    Equipo,
    Disciplina,
    Puntuacion,
    TablaPosiciones,
    Jornada,
    ProgramacionJuego,
    Campeonato,
    InscripcionEquipo,
    InscripcionJugador,
    Escenario,
    Encuentro,
    NominaEncuentro,
    Resultado,
    Amonestacion
)

admin.site.register(Persona)
admin.site.register(Jugador)
admin.site.register(Arbitro)
admin.site.register(Equipo)
admin.site.register(Disciplina)
admin.site.register(Puntuacion)
admin.site.register(TablaPosiciones)
admin.site.register(Jornada)
admin.site.register(ProgramacionJuego)
admin.site.register(Campeonato)
admin.site.register(InscripcionEquipo)
admin.site.register(InscripcionJugador)
admin.site.register(Escenario)
admin.site.register(Encuentro)
admin.site.register(NominaEncuentro)
admin.site.register(Resultado)
admin.site.register(Amonestacion)
