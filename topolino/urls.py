"""topolino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tareas import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$',views.home),
    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(),
    url(r'^admin/', admin.site.urls),
    url(r'^tareas/(?P<id>[0-9]+)/$', views.comentario),
    url(r'^tareas/', views.lista_tareas),
    url(r'^registration/registro.html',views.register),
    url(r'^editar_tareas/', views.editar_tareas),
    url('^',include('django.contrib.auth.urls')),
]
