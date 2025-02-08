# Importamos la función path de django.urls y las vistas de nuestro módulo actual
from django.urls import path
from . import views

# Definimos las URLs que manejará nuestra aplicación
urlpatterns = [ 
    # Cuando se accede a la raíz del sitio (''), se llama a la vista 'index' del módulo 'views'
    # El nombre de esta URL es 'index'
    path('', views.Home, name='HomePage'),
    # Ruta para acceder a la vista 'Contratistas' del módulo 'views'
    # El nombre de esta URL es 'Contratistas'
    path('Contratistas/', views.VerContratistas, name='VerContratistas'),
    path('AgregarContratista/', views.agregar_contratista, name='AgregarContratista'),
    path('EditarContratista/<int:id>', views.editar_contratista, name='EditarContratista'),
    path('EliminarContratista/<int:id>', views.eliminar_contratista, name='EliminarContratista'),
    # El nombre de esta URL es  Proyectos'
    path('Proyectos/', views.VerProyectos, name='VerProyectos'),
    path('AgregarProyecto/', views.agregar_proyecto, name='AgregarProyecto'),
    path('EditarProyecto/<int:id>', views.editar_proyecto, name='EditarProyecto'),
    path('EliminarProyecto/<int:id>', views.eliminar_proyecto, name='EliminarProyecto'),
    # El nombre de esta URL es 'Zonas Verdes'
    path('Zonas/', views.VerZonas, name='VerZonas'),
    path('AgregarZona/', views.agregar_zona, name='AgregarZona'),
    path('EditarZona/<int:id>', views.editar_zona, name='EditarZona'),
    path('EliminarZona/<int:id>', views.eliminar_zona, name='EliminarZona'),
    # El nombre de esta URL es 'Construcciones'
    path('Construcciones/', views.VerConstrucciones, name='VerConstrucciones'),
    path('AgregarConstruccion/', views.agregar_construccion, name='AgregarConstruccion'),
    path('EditarConstruccion/<int:id>', views.editar_construccion, name='EditarConstruccion'),
    path('EliminarConstruccion/<int:id>', views.eliminar_construccion, name='EliminarConstruccion'),
    
]
