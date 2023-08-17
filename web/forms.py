from django import forms

class DatosAudioForm(forms.Form):
    titulo1 = forms.CharField(label='Título del primer audio', max_length=200)
    duracion1 = forms.CharField(label='Duración del primer audio (hh:mm:ss)')
    titulo2 = forms.CharField(label='Título del segundo audio', max_length=200)
    duracion2 = forms.CharField(label='Duración del segundo audio (hh:mm:ss)')
    num_integrantes = forms.IntegerField(label='Número de integrantes')

class DivisionAudioForm(forms.Form):
    titulo = forms.CharField(label = 'Titulo del audio', max_length=100)
    duracion = forms.CharField(label ='Duracion del audio (hh:mm:ss)', max_length=8) 
    num_integrantes = forms.IntegerField(label='Número de integrantes')