from django.shortcuts import render

# Create your views here.
def zlecenia_lista(request):
    return render(request, 'omnomnom_app/zlecenia_lista.html', {})