

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Encuentro, TablaPosiciones, Equipo

def registrar_resultado(request, encuentro_id):
    encuentro = get_object_or_404(Encuentro, pk=encuentro_id)
    marcador_equipo1 = request.POST.get('marcador_equipo1')
    marcador_equipo2 = request.POST.get('marcador_equipo2')

    if marcador_equipo1 is not None and marcador_equipo2 is not None:
        encuentro.marcador_equipo1 = marcador_equipo1
        encuentro.marcador_equipo2 = marcador_equipo2
        encuentro.save()

        actualizar_tabla_posiciones(encuentro)

        return HttpResponse("Resultado registrado correctamente")

    return HttpResponse("Datos inválidos")

def actualizar_tabla_posiciones(encuentro):
    equipo1 = encuentro.equipo1
    equipo2 = encuentro.equipo2

    try:
        tabla_equipo1 = TablaPosiciones.objects.get(equipo=equipo1, campeonato=encuentro.campeonato)
    except TablaPosiciones.DoesNotExist:
        tabla_equipo1 = TablaPosiciones(equipo=equipo1, campeonato=encuentro.campeonato, puntos=0, partidos_jugados=0)

    try:
        tabla_equipo2 = TablaPosiciones.objects.get(equipo=equipo2, campeonato=encuentro.campeonato)
    except TablaPosiciones.DoesNotExist:
        tabla_equipo2 = TablaPosiciones(equipo=equipo2, campeonato=encuentro.campeonato, puntos=0, partidos_jugados=0)

    tabla_equipo1.partidos_jugados += 1
    tabla_equipo2.partidos_jugados += 1

    if encuentro.marcador_equipo1 > encuentro.marcador_equipo2:
        tabla_equipo1.puntos += 3
    elif encuentro.marcador_equipo1 < encuentro.marcador_equipo2:
        tabla_equipo2.puntos += 3
    else:
        tabla_equipo1.puntos += 1
        tabla_equipo2.puntos += 1

    tabla_equipo1.save()
    tabla_equipo2.save()
