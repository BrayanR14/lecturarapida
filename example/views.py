from datetime import datetime
from .models import Usuario, Nivel
from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Bienvenido a Lectura Rapida!</h1>
            <p>La hora exacta ahora mismo es { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def perfil(request):
    html = '''
    <html>
        <body>
            <h1>Perfil</h1>
            <p>Esta es la pagina de perfil.</p>
        </body>
    </html>
    '''
    return HttpResponse(html) 

def create(request):
    usuar = Usuario(User="Usuario1", Puntos=0, Nivel=1, Objetivos="Objetivo1", Amistades="Amigo1")
    usuar.save()
    lvl = Nivel(Nombre_nivel="Nivel1", Descripcion="Descripcion del nivel 1", Puntos_Necesarios=100, usuario=usuar)
    lvl.save()
    html = '''
    <html>
        <body>
            <h1>Crear Usuario {%lvl.usuario.usuar%}</h1>
            <p>Esta es la pagina para crear un nuevo usuario.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)