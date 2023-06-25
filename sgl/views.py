from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Leccion, Pregunta, Opcion, RespuestaUsuario, Calificacion

def leccion(request, examen_id):
    examen = get_object_or_404(Leccion, id=examen_id)
    usuario = request.user

    if request.method == 'POST':
        preguntas = Pregunta.objects.filter(examen=examen)
        total_preguntas = preguntas.count()
        puntaje = 0

        for pregunta in preguntas:
            opcion_seleccionada = request.POST.get(f'opcion_{pregunta.id}')

            if opcion_seleccionada:
                opcion = get_object_or_404(Opcion, id=opcion_seleccionada)
                respuesta_usuario = RespuestaUsuario(usuario=usuario, pregunta=pregunta, opcion=opcion)
                respuesta_usuario.save()

                if opcion.es_correcta:
                    puntaje += 1

        calificacion = int((puntaje / total_preguntas) * 100)

        try:
            # Intentar obtener la calificación existente del usuario para el examen actual
            calificacion_usuario = Calificacion.objects.get(usuario=usuario, examen=examen)
            calificacion_usuario.calificacion = calificacion  # Sobrescribir la calificación existente
            calificacion_usuario.save()
        except Calificacion.DoesNotExist:
            # Si no existe una calificación existente, crear una nueva
            calificacion_usuario = Calificacion(usuario=usuario, examen=examen, calificacion=calificacion)
            calificacion_usuario.save()

        messages.success(request, 'Examen completado. Tu calificación se ha guardado.')
        return redirect('resultado')

    preguntas = Pregunta.objects.filter(examen=examen)
    opciones = Opcion.objects.filter(pregunta__in=preguntas)
    numero = Leccion.objects.get(id=examen_id)
    context = {
        'examen': examen,
        'preguntas': preguntas,
        'opciones': opciones,
        'numero': numero
    }
    return render(request, 'examen.html', context)

def resultado(request):
    usuario = request.user
    calificaciones = Calificacion.objects.filter(usuario=usuario).order_by('-fecha_creacion')[:1]

    context = {
        'calificaciones': calificaciones
    }
    return render(request, 'resultado.html', context)



# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404

# def home(request):
#         return HttpResponse("<h2>Selecciona tu perfil</h2>")

# def leccion(request):
#         return HttpResponse("<h2>Registrarse</h2>")
