import django
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import FormTipo, FormularioDatos

# Create your views here.
def registro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('Home')
        else:
            return render(request, 'registro.html')
    else:
        form_datos = FormularioDatos(request.POST)
        form_tipo = FormTipo(request.POST)

        if form_datos.is_valid() and form_tipo.is_valid():
            datos = form_datos.save()
            usuario = form_tipo.save(commit=False)
            usuario.datos = datos
            usuario.save()
            messages.success(request, "Tu cuenta ha sido creada.")
            return redirect('login')
        else:
            return render(request, 'registro.html', {"errors": form_datos.errors})

        return render(request, 'registro.html')