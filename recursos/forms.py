from django.forms import ModelForm
from django import forms
from .models import Categoria, Reserva, Recurso


class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']


class FormReserva(ModelForm):
    # dataReserva = forms.DateField(widget=forms.SelectDateWidget) #
    class Meta:
        model = Reserva
        fields = ['dataReserva', 'horaReserva', 'dataEmprestimo', 'horaEmprestimo', 'dataDevolucao', 'horaDevolucao', 'recursos']
        filter_horizontal = ('recursos', )