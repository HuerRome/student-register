from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
#las vistas trabajan recibiendo una peticion 
def formularioContacto(request):
    return render(request, "formularioContacto.html")

'''
pagina de exito que indique que la información enviada del formulario se a enviado con exito
'''
def contactar(request):
    if request.method == 'POST':
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["anroo475@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
          







