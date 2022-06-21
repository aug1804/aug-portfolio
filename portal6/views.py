from django.shortcuts import render, redirect

# Create your views here.
from .models import Autor, Editora, Formato, Livro, Country, State, City
from .forms import AutorForm, EditoraForm, FormatoForm, LivroForm, CountryForm, StateForm, CityForm

def home(request):
    return render(request, 'home.html')

# autor

def autor(request):
    #autores = Autor.objects.all().order_by('-nome') #--> augustão sort / #class Meta: ordering = ['-nome'] FUNCIONOU em models.py
    autores = Autor.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'autor.html', context)

def autor_add(request):
    form = AutorForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
    context = {
        'form': form
    }
    return render(request, 'autor_add.html', context)

def autor_edit(request, autor_pk):

    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(request.POST or None, instance=autor)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
    context = {
        'form': form
    }
    return render(request, 'autor_edit.html', context)

def autor_delete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()
    return redirect('autor')

# editora

def editora(request):
    editoras = Editora.objects.all().order_by('nome')  # --> augustão sort
    context = {
        'editoras': editoras
    }
    return render(request, 'editora.html', context)

def editora_add(request):
    form = EditoraForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')
    context = {
        'form': form
    }
    return render(request, 'editora_add.html', context)

def editora_edit(request, editora_pk):

    editora = Editora.objects.get(pk=editora_pk)

    form = EditoraForm(request.POST or None, instance=editora)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')
    context = {
        'form': form
    }
    return render(request, 'editora_edit.html', context)

def editora_delete(request, editora_pk):
    editora = Editora.objects.get(pk=editora_pk)
    editora.delete()
    return redirect('editora')

# formato

def formato(request):
    formatos = Formato.objects.all().order_by('nome')  # --> augustão sort
    context = {
        'formatos': formatos
    }
    return render(request, 'formato.html', context)

def formato_add(request):
    form = FormatoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('formato')
    context = {
        'form': form
    }
    return render(request, 'formato_add.html', context)

def formato_edit(request, formato_pk):

    formato = Formato.objects.get(pk=formato_pk)

    form = FormatoForm(request.POST or None, instance=formato)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('formato')
    context = {
        'form': form
    }
    return render(request, 'formato_edit.html', context)

def formato_delete(request, formato_pk):
    formato = Formato.objects.get(pk=formato_pk)
    formato.delete()
    return redirect('formato')

# livro

def livro(request):
    livros = Livro.objects.all().order_by('titulo')  # --> augustão sort
    context = {
        'livros': livros
    }
    return render(request, 'livro.html', context)

def livro_add(request):
    form = LivroForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livro')
    context = {
        'form': form
    }
    return render(request, 'livro_add.html', context)

def livro_edit(request, livro_pk):

    #--> foreign key combo box ???
    livro = Livro.objects.get(pk=livro_pk)
    form = LivroForm(request.POST or None, instance=livro)
    #--> foreign key combo box ???

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('livro')
    context = {
        'form': form
    }
    return render(request, 'livro_edit.html', context)

def livro_delete(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    livro.delete()
    return redirect('livro')

# country

def country(request):
    #countries = Country.objects.all().order_by('-nome') #--> augustão sort / #class Meta: ordering = ['-nome'] FUNCIONOU em models.py
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render(request, 'country.html', context)

def country_add(request):
    form = CountryForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('country')
    context = {
        'form': form
    }
    return render(request, 'country_add.html', context)

def country_edit(request, country_pk):

    country = Country.objects.get(pk=country_pk)

    form = CountryForm(request.POST or None, instance=country)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('country')
    context = {
        'form': form
    }
    return render(request, 'country_edit.html', context)

def country_delete(request, country_pk):
    country = Country.objects.get(pk=country_pk)
    country.delete()
    return redirect('country')

# state

def state(request):
    states = State.objects.all().order_by('state_name')  # --> augustão sort
    context = {
        'states': states
    }
    return render(request, 'state.html', context)

def state_add(request):
    form = StateForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('state')
    context = {
        'form': form
    }
    return render(request, 'state_add.html', context)

def state_edit(request, state_pk):

    state = State.objects.get(pk=state_pk)

    form = StateForm(request.POST or None, instance=state)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('state')
    context = {
        'form': form
    }
    return render(request, 'state_edit.html', context)

def state_delete(request, state_pk):
    state = State.objects.get(pk=state_pk)
    state.delete()
    return redirect('state')

# city

def city(request):
    #cities = City.objects.all().order_by('-nome') #--> augustão sort / #class Meta: ordering = ['-nome'] FUNCIONOU em models.py
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request, 'city.html', context)

def city_add(request):
    form = CityForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('city')
    context = {
        'form': form
    }
    return render(request, 'city_add.html', context)

def city_edit(request, city_pk):

    city = City.objects.get(pk=city_pk)

    form = CityForm(request.POST or None, instance=city)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('city')
    context = {
        'form': form
    }
    return render(request, 'city_edit.html', context)

def city_delete(request, city_pk):
    city = City.objects.get(pk=city_pk)
    city.delete()
    return redirect('city')

# aula


def aula(request):
    return render(request, 'aula.html')


def aula004(request):
    return render(request, 'aula004.html')


def aula006theboot(request):
    return render(request, 'aula006theboot.html')


def aula006holberton(request):
    return render(request, 'aula006holberton.html')


def aula006tweets(request):
    return render(request, 'aula006tweets.html')


def aula007(request):
    return render(request, 'aula007.html')


def aula008(request):
    return render(request, 'aula008.html')


def aula061exemplo(request):
    return render(request, 'aula061exemplo.html')
