from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()

    class Meta:
        ordering = ['nome'] #--> augustão FUNCIONOU

    # --> augustão ModelChoiceField comando mágico para aparecer o 'nome' (ForeignKey de Autor) ao invés de 'Autor object (1)'
    def __str__(self):
        return self.nome + ' - ' + self.email

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)

    #--> augustão Tabela de Estados - #modelchoicefield
    ACRE = 'AC'
    ALAGOAS = 'AL'
    AMAPA = 'AP'
    AMAZONAS = 'AM'
    BAHIA = 'BA'
    CEARA = 'CE'
    DISTRITOFEDERAL = 'DF'
    ESPIRITOSANTO = 'ES'
    GOIAS = 'GO'
    MARANHAO = 'MA'
    MATOGROSSO = 'MT'
    MATOGROSSODOSUL = 'MS'
    MINASGERAIS = 'MG'
    PARA = 'PA'
    PARAIBA = 'PB'
    PARANA = 'PR'
    PERNAMBUCO = 'PE'
    PIAUI = 'PI'
    RIODEJANEIRO = 'RJ'
    RIOGRANDEDONORTE = 'RN'
    RIOGRANDEDOSUL = 'RS'
    RONDONIA = 'RO'
    RORAIMA = 'RR'
    SANTACATARINA = 'SC'
    SAOPAULO = 'SP'
    SERGIPE = 'SE'
    TOCANTINS = 'TO'
    ESTADO_CHOICES = [
        (ACRE, 'Acre'),
        (ALAGOAS, 'Alagoas'),
        (AMAPA, 'Amapá'),
        (AMAZONAS, 'Amazonas'),
        (BAHIA, 'Bahia'),
        (CEARA, 'Ceará'),
        (DISTRITOFEDERAL, 'Distrito Federal'),
        (ESPIRITOSANTO, 'Espírito Santo'),
        (GOIAS, 'Goiás'),
        (MARANHAO, 'Maranhão'),
        (MATOGROSSO, 'Mato Grosso'),
        (MATOGROSSODOSUL, 'Mato Grosso do Sul'),
        (MINASGERAIS, 'Minas Gerais'),
        (PARA, 'Pará'),
        (PARAIBA, 'Paraíba'),
        (PARANA, 'Paraná'),
        (PERNAMBUCO, 'Pernambuco'),
        (PIAUI, 'Piauí'),
        (RIODEJANEIRO, 'Rio de Janeiro'),
        (RIOGRANDEDONORTE, 'Rio Grande do Norte'),
        (RIOGRANDEDOSUL, 'Rio Grande do Sul'),
        (RONDONIA, 'Rondônia'),
        (RORAIMA, 'Roraima'),
        (SANTACATARINA, 'Santa Catarina'),
        (SAOPAULO, 'São Paulo'),
        (SERGIPE, 'Sergipe'),
        (TOCANTINS, 'Tocantins'),
    ]
    estado = models.CharField( max_length=2, choices=ESTADO_CHOICES, default=SAOPAULO, )
    #estado = models.CharField(max_length=2)

    class Meta:
        ordering = ['nome']  # --> augustão FUNCIONOU

    def __str__(self):
        return self.nome

class Formato(models.Model):
    nome = models.CharField('Nome do Formato', max_length=255)

    class Meta:
        ordering = ['nome']  # --> augustão FUNCIONOU

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=255)

    subtitulo = models.CharField('Subtítulo', max_length=255, blank=True, null=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Quem Escreveu') #--> augustão nome do campo

    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    formato = models.ForeignKey(Formato, on_delete=models.SET_NULL, null=True)

    data_lancamento = models.DateField('Data de Lançamento')

    isbn = models.CharField('ISBN', max_length=255)
    
    numero_paginas = models.PositiveIntegerField('Número de Páginas')

class Country(models.Model):
    country_name = models.CharField(max_length=255, verbose_name='País')
    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=255, verbose_name='Estado ou DF')
    state_country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='País')
    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=255, verbose_name='Cidade')
    city_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado ou DF')
    def __str__(self):
        return self.city_name
