from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Categoria, Reserva, Recurso
from .forms import FormCategoria, FormReserva


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return render(request, 'home.html')


# CATEGORIA RECURSO #
@login_required
def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria.html', {'categorias': categorias})


@login_required
def nova_categoria(request):
    form = FormCategoria(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_categoria')
    return render(request, 'categoria_form.html', {'form': form})


@login_required
def alterar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    form = FormCategoria(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listar_categoria')

    return render(request, 'categoria_form.html', {'form': form})


@login_required
def mostrar_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    return render(request, 'categoria_mostrar.html', {'categoria': categoria})


# RESERVA #
@login_required
def listar_reserva(request):
    #reservas = Reserva.objects.get(statusReserva='Reservado').recursos.all()
    reservas = Reserva.objects.all()

    return render(request, 'reserva.html', {'reservas': reservas})


@login_required
def nova_reserva(request):
    form = FormReserva(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.usuario = request.user
        form.save()
        return redirect('listar_reserva')
    return render(request, 'reserva_form.html', {'form_reserva': form})