# DivideTusAudios

## Descripción
DivideTusAudios es una aplicación web que te permite dividir archivos de audio en fracciones más pequeñas, ya sea dividiendo dos audios diferentes o un solo audio en varias partes. Puedes especificar la duración total y el número de integrantes, y la aplicación generará automáticamente las fracciones de audio para cada integrante.

## Características
- División de dos audios: Divide dos archivos de audio en fracciones para cada integrante.
- División de un solo audio: Divide un archivo de audio en fracciones para cada integrante.
- Asignación aleatoria de integrantes.
- Control de errores y mensajes de validación.
- Diseño responsive y amigable para el usuario.

## Requisitos
- Python 3.x
- Django 4.x
- Otros requisitos específicos del proyecto (bibliotecas, paquetes, etc.)

## Instalación
1. Clona este repositorio: `git clone https://github.com/tu-usuario/DivideTusAudios.git`
2. Ve al directorio del proyecto: `cd DivideTusAudios`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Configura la base de datos en `settings.py`.
5. Realiza las migraciones: `python manage.py makemigrations` y `python manage.py migrate`
6. Inicia el servidor local: `python manage.py runserver`
7. Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/`

## Uso
1. Abre tu navegador y accede a la URL de la aplicación.
2. Selecciona una de las opciones de división de audio: "Dividir dos audios" o "Dividir un solo audio".
3. Completa el formulario con la información requerida (título, duración, número de integrantes, etc.).
4. Presiona el botón "Divide" para generar las fracciones de audio.
5. Visualiza los resultados de la división en la página de resultados.

