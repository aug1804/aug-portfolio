from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

#from django.contrib import admin

# importa todas as views que foram criadas
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # autor
    path('autor/', views.autor, name='autor'),
    path('autor/add/', views.autor_add, name='autor_add'),
    path('autor/edit/<int:autor_pk>', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),

    # editora
    path('editora/', views.editora, name='editora'),
    path('editora/add/', views.editora_add, name='editora_add'),
    path('editora/edit/<int:editora_pk>', views.editora_edit, name='editora_edit'),
    path('editora/delete/<int:editora_pk>', views.editora_delete, name='editora_delete'),

    # formato
    path('formato/', views.formato, name='formato'),
    path('formato/add/', views.formato_add, name='formato_add'),
    path('formato/edit/<int:formato_pk>', views.formato_edit, name='formato_edit'),
    path('formato/delete/<int:formato_pk>', views.formato_delete, name='formato_delete'),

    # livro
    path('livro/', views.livro, name='livro'),
    path('livro/add/', views.livro_add, name='livro_add'),
    path('livro/edit/<int:livro_pk>', views.livro_edit, name='livro_edit'),
    path('livro/delete/<int:livro_pk>', views.livro_delete, name='livro_delete'),

    # country
    path('country/', views.country, name='country'),
    path('country/add/', views.country_add, name='country_add'),
    path('country/edit/<int:country_pk>', views.country_edit, name='country_edit'),
    path('country/delete/<int:country_pk>', views.country_delete, name='country_delete'),

    # state
    path('state/', views.state, name='state'),
    path('state/add/', views.state_add, name='state_add'),
    path('state/edit/<int:state_pk>', views.state_edit, name='state_edit'),
    path('state/delete/<int:state_pk>', views.state_delete, name='state_delete'),

    # city
    path('city/', views.city, name='city'),
    path('city/add/', views.city_add, name='city_add'),
    path('city/edit/<int:city_pk>', views.city_edit, name='city_edit'),
    path('city/delete/<int:city_pk>', views.city_delete, name='city_delete'),

    # aula
    path('aula/', views.aula, name='aula'),
    path('aula004/', views.aula004, name='aula004'),
    path('aula006theboot/', views.aula006theboot, name='aula006theboot'),
    path('aula006holberton/', views.aula006holberton, name='aula006holberton'),
    path('aula006tweets/', views.aula006tweets, name='aula006tweets'),
    path('aula007/', views.aula007, name='aula007'),
    path('aula008/', views.aula008, name='aula008'),
    path('aula061exemplo/', views.aula061exemplo, name='aula061exemplo'),

] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #--> august??o ???

#   path('portal6/', include('portal6.urls')),

#   path('admin/', admin.site.urls), --> tirei para n??o ficar duplicado ???
