from django.shortcuts import render
import random
from .forms import DatosAudioForm, DivisionAudioForm
from .models import Integrante, Audio
from django.urls import reverse
# Create your views here.

def obtener_formato_tiempo(tiempo_segundos):
    horas = tiempo_segundos // 3600
    minutos = (tiempo_segundos % 3600) // 60
    segundos = tiempo_segundos % 60
    return f'{horas:02d}:{minutos:02d}:{segundos:02d}'

def obtener_duracion_segundos(duracion_input):
    horas, minutos, segundos = map(int, duracion_input.split(':'))
    return horas * 3600 + minutos * 60 + segundos

def generar_planificacion(request):
    try:
        limite_maximo_segundos = 5 * 60  
        if request.method == 'POST':
            form = DatosAudioForm(request.POST)
            if form.is_valid():
                titulo1 = form.cleaned_data['titulo1']
                duracion_input1 = form.cleaned_data['duracion1']
                duracion_total_segundos1 = obtener_duracion_segundos(duracion_input1)
            
                titulo2 = form.cleaned_data['titulo2']
                duracion_input2 = form.cleaned_data['duracion2']
                duracion_total_segundos2 = obtener_duracion_segundos(duracion_input2)
            
                num_integrantes = form.cleaned_data['num_integrantes']
                duracion_total_segundos = (duracion_total_segundos1 + duracion_total_segundos2) // num_integrantes
            
                # Generar una lista de integrantes
                integrantes = [f'Integrante {i}' for i in range(1, num_integrantes + 1)]
                random.shuffle(integrantes)
            
                fracciones_audio1 = []
                fracciones_audio2 = []
                inicio1 = 0
                inicio2 = 0

                for integrante in integrantes:
                    fin1 = inicio1 + duracion_total_segundos
                    if fin1 > duracion_total_segundos1:
                        fin1 = duracion_total_segundos1
                    duracion_fraccion1 = fin1 - inicio1

                    fin2 = inicio2 + duracion_total_segundos - duracion_fraccion1
                    if fin2 > duracion_total_segundos2:
                        fin2 = duracion_total_segundos2
                    duracion_fraccion2 = fin2 - inicio2

                    fraccion_audio1 = f'{integrante}: Fracción {titulo1} desde {obtener_formato_tiempo(inicio1)} hasta {obtener_formato_tiempo(fin1)} ({obtener_formato_tiempo(duracion_fraccion1)})'
                    fraccion_audio2 = f'{integrante}: Fracción {titulo2} desde {obtener_formato_tiempo(inicio2)} hasta {obtener_formato_tiempo(fin2)} ({obtener_formato_tiempo(duracion_fraccion2)})'

                    if integrante == integrantes[-1]:  # Último integrante
                        tiempo_restante1 = duracion_total_segundos1 - inicio1
                        tiempo_inicio2 = inicio2
                        if tiempo_restante1 > limite_maximo_segundos:
                            tiempo_restante1 = limite_maximo_segundos
                            tiempo_inicio2 += duracion_fraccion2 - limite_maximo_segundos
                        duracion_fraccion1 += tiempo_restante1
                        duracion_fraccion2 += tiempo_restante1

                        fraccion_audio1 += f' + {titulo2} inicio {obtener_formato_tiempo(tiempo_inicio2)} hasta {obtener_formato_tiempo(fin2)} ({obtener_formato_tiempo(duracion_fraccion2)})'

                    if duracion_fraccion1 > 0:
                        fracciones_audio1.append(fraccion_audio1)
                    if duracion_fraccion2 > 0:
                        fracciones_audio2.append(fraccion_audio2)

                    inicio1 = fin1
                    inicio2 = fin2

                return render(request, 'resultados.html', {'fracciones_audio1': fracciones_audio1, 'fracciones_audio2': fracciones_audio2})
            else:
                # Si el formulario no es válido, mostrar un mensaje de error
                raise ValueError("Por favor, completa el formulario correctamente.")
        else:
            form = DatosAudioForm()

        return render(request, 'index.html', {'form': form})
    except Exception as e:
        error_message = str(e)
        return render(request, 'index.html', {'form': form, 'error_message': error_message})

def resultados(request):
    fracciones_audio1_str = request.GET.get('fracciones_audio1')
    fracciones_audio2_str = request.GET.get('fracciones_audio2')

    fracciones_audio1 = fracciones_audio1_str.split('|')
    fracciones_audio2 = fracciones_audio2_str.split('|')

    return render(request, 'resultados.html', {'fracciones_audio1': fracciones_audio1, 'fracciones_audio2': fracciones_audio2})

#Dividir un solo audio
def dividir_audio(request):
    try:
        limite_maximo_segundos = 5 * 60  
        if request.method == 'POST':
            form = DivisionAudioForm(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data['titulo']
                duracion_input = form.cleaned_data['duracion']
                duracion_total_segundos = obtener_duracion_segundos(duracion_input)
            
                num_integrantes = form.cleaned_data['num_integrantes']
                integrantes = [f'Integrante {i}' for i in range(1, num_integrantes + 1)]
                random.shuffle(integrantes)  # Mezclar los nombres de los integrantes
                
                duracion_total_audio = duracion_total_segundos // num_integrantes
            
                fracciones_audio = []
                inicio = 0

                for integrante in integrantes:
                    fin = inicio + duracion_total_audio
                    if fin > duracion_total_segundos:
                        fin = duracion_total_segundos
                    duracion_fraccion = fin - inicio

                    fraccion_audio = f'{integrante}: Fracción {titulo} desde {obtener_formato_tiempo(inicio)} hasta {obtener_formato_tiempo(fin)} ({obtener_formato_tiempo(duracion_fraccion)})'

                    if duracion_fraccion > 0:
                        fracciones_audio.append(fraccion_audio)

                    inicio = fin

                return render(request, 'resultados_division.html', {'fracciones_audio': fracciones_audio})
            else:
                # Si el formulario no es válido, mostrar un mensaje de error
                raise ValueError("Por favor, completa el formulario correctamente.")
        else:
            form = DivisionAudioForm()

        return render(request, 'dividir_audio.html', {'form': form})
    except Exception as e:
        error_message = str(e)
        return render(request, 'dividir_audio.html', {'form': form, 'error_message': error_message})

def resultados_division(request):
    fracciones_audio_str = request.GET.get('fracciones_audio')

    fracciones_audio = fracciones_audio_str.split('|')

    return render(request, 'resultados_division.html', {'fracciones_audio': fracciones_audio})
