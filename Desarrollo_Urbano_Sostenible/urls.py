"""
Configuración de URLs para el proyecto Desarrollo_Urbano_Sostenible.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, por favor visita:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones:
    1. Añadir una importación:  from my_app import views
    2. Añadir una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases:
    1. Añadir una importación:  from other_app.views import Home
    2. Añadir una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluir otra configuración de URL:
    1. Importar la función include(): from django.urls import include, path
    2. Añadir una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Definimos las URLs que manejará nuestro proyecto
urlpatterns = [
    # Ruta para acceder a la interfaz de administración de Django
    path('admin/', admin.site.urls),
    # Incluimos las URLs de la aplicación 'Gestion_Proyectos_Urbanos'
    # Cuando se accede a la raíz del sitio (''), se redirige a las URLs definidas en 'Aplicaciones.Gestion_Proyectos_Urbanos.urls'
    path('', include('Aplicaciones.Gestion_Proyectos_Urbanos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)