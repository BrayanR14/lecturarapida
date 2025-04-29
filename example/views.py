from datetime import datetime

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