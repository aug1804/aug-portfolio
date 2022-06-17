# from attr import fields #--> ???
from django import forms

from .models import Autor, Country, Editora, Formato, Livro, Country, State, City

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ()
        #ordering = ['-nome'] #--> augustão NÃO CLASSIFICOU NO FORMULÁRIO DE ADD / EDIT DO LIVRO
        #                                   TEM QUE COLOCAR NO models.py
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'autofocus': True}) #--> augustão autofocus

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'autofocus': True}) #--> augustão autofocus

class FormatoForm(forms.ModelForm):
    class Meta:
        model = Formato
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'autofocus': True}) #--> augustão autofocus


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'autofocus': True})  # --> augustão autofocus


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_name'].widget.attrs.update({'autofocus': True})
class StateForm(forms.ModelForm):
    class Meta:
        model = State
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state_name'].widget.attrs.update({'autofocus': True})
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        exclude = ()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_name'].widget.attrs.update({'autofocus': True})

"""
        username = forms.CharField(
            label=_('nome'),
            strip=True,
            widget=forms.TextInput(attrs={'placeholder': _(
                'nome'), 'class': 'form-control', 'autofocus': True})
        )

class FormatoForm(forms.ModelForm):
    # nome = forms.CharField(
    #     max_length=255,
    #     widget=forms.TextInput(attrs={'autofocus': True})
    # )
    class Meta:
        model = Formato
        # fields = ['nome']
        exclude = ()
"""

"""
    def __init__(self):
        self.fields['nome'].widget.attrs.update({'autofocus': True})
"""

"""
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
"""

"""
        fields = (all) ???
        ou
        fields = ('nome', 'data_nascimento', 'email')
        ou
        exclude = ()
"""

""" depois eu coloco aqui as classes do bootstrap """
