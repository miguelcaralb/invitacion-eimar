from django.shortcuts import render


def invitacion(request):
    return render(request, 'cumple/invitacion.html')