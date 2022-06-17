"""meu_projeto6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal6.urls')),
]

# a cagada estava por aqui
#    path("", TemplateView.as_view(template_name="home.html")),
#    path("autor", TemplateView.as_view(template_name="autor.html")),
#    path("autor_add", TemplateView.as_view(template_name="autor_add.html")),

# não sei se isso funciona
#   path('', include('../portal.urls')), --> não está funcionando
#   path("", TemplateView.as_view(template_name="index.html")),
#   path("", TemplateView.as_view(template_name="base.html")),
