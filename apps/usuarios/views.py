from django.shortcuts import *

from django.contrib.auth import logout as do_logout
from apps.usuarios.models import *
def index(request):
    #if request.user.is_authenticated:
        return render(request, 'usuarios/index.html')
        # En otro caso redireccionamos al login
    #return  redirect('/login')

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def lineas_list(resquest):
    trafico = Trafico_linea.objects.all()
    contexto = {'trafico':trafico}
    return render(resquest,'usuarios/registros.html',contexto)
