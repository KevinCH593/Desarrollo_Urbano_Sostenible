# Importar las funciones render, redirect y get_object_or_404 del módulo django.shortcuts
from django.shortcuts import render, redirect, get_object_or_404

# Importar el modelo del archivo models en el mismo directorio
from .models import Contratista, ProyectoUrbano, ZonaVerde, ConstruccionSostenible

# Importar datetime para manejar fechas
from datetime import date
import os

# Importar la librería messages del módulo django.contrib para mostrar mensajes de confirmación
from django.contrib import messages

# ----------------------------------------------------------------
# HOME
# ----------------------------------------------------------------

# Página de inicio
# Definimos la función Home, que toma un objeto request como argumento
def Home(request):
    # Utilizamos la función render para devolver una respuesta HTML utilizando la plantilla 'Home.html' ubicada en el directorio 'Gestion_Proyectos_Urbanos'
    return render(request, 'Home.html',{'active_page': 'home'})

# ----------------------------------------------------------------
# CONTRATISTAS
# ----------------------------------------------------------------

# Página de inicio
# Definimos la función Home, que toma un objeto request como argumento
def VerContratistas(request):
    contratistas = Contratista.objects.all()
    # Utilizamos la función render para devolver una respuesta HTML utilizando la plantilla 'Home.html' ubicada en el directorio 'Gestion_Proyectos_Urbanos'
    return render(request, 'Contratistas/inicio_contratistas.html',{'contratistas':contratistas, 'active_page': 'contratistas'})

# Agregar Contratista
def agregar_contratista(request):
    # Si el método HTTP es POST, quiere decir que se enviaron datos al formulario
    if request.method == 'POST':
        # Obtenemos los datos enviados en el formulario
        nombre = request.POST['nombre']
        cedula = request.POST['cedula']
        empresa = request.POST['empresa']
        telefono = request.POST['telefono']
        email = request.POST['email']
        especialidad = request.POST['especialidad']
        
        # Creamos un nuevo objeto Contratista con los datos recibidos
        contratista = Contratista(nombre=nombre, cedula=cedula,empresa=empresa, telefono=telefono, email=email, especialidad=especialidad)
        
        # Guardamos el contratista en la base de datos
        contratista.save()
        
        # Mostramos un mensaje de confirmación
        messages.success(request, 'Contratista agregado correctamente.')
        
        # Redireccionamos a la página de inicio de contratistas
        return redirect('VerContratistas')
    
# Editar Contratista
def editar_contratista(request, id):
    # Obtenemos el contratista a editar
    contratista = get_object_or_404(Contratista, pk=id)
    # Si el método HTTP es POST, quiere decir que se enviaron datos al formulario
    if request.method == 'POST':
        contratista.nombre = request.POST['nombre']
        contratista.empresa = request.POST['empresa']
        contratista.telefono = request.POST['telefono']
        contratista.email = request.POST['email']
        contratista.especialidad = request.POST['especialidad']
        
        # Guardamos los cambios en la base de datos
        contratista.save()
        
        # Agregamos un mensaje de éxito para el usuario indicando que los cambios fueron guardados correctamente
        messages.success(request, 'Contratista editado correctamente.')
        
        # Redireccionamos a la página de inicio de contratistas
        return redirect('VerContratistas')
    
    return render(request, 'Contratistas/editar_contratista.html', {'contratista': contratista})

# Eliminar Contratista
def eliminar_contratista(request, id):
    # Obtiene un objeto Contratista a partir del ID proporcionado o retorna un error 404 si no se encuentra
    contratista = get_object_or_404(Contratista, pk=id)
    # Elimina el objeto contratista de la base de datos
    contratista.delete()
    # Agrega un mensaje de éxito para el usuario indicando que el contratista fue eliminado exitosamente
    messages.success(request,'Contratista eliminado exitosamente')
    # Redirige al usuario a la vista 'index_contratistas'
    return redirect('VerContratistas')

# ----------------------------------------------------------------
# PROYECTOS
# ----------------------------------------------------------------

def VerProyectos(request):
    proyectos = ProyectoUrbano.objects.all()
    contratistas = Contratista.objects.all()  # Asegúrate de obtener los contratistas
    return render(request, 'Proyectos/inicio_proyectos.html', {'proyectos': proyectos, 'contratistas': contratistas, 'active_page': 'proyectos'})

def agregar_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        ubicacion = request.POST['ubicacion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST.get('fecha_fin', None)  # Permitir valores nulos
        contratista_id = request.POST.get('contratista')  # Capturar ID del contratista

        if contratista_id:
            contratista = get_object_or_404(Contratista, pk=contratista_id)  # Obtener objeto
        else:
            contratista = None

        # Crear y guardar proyecto
        proyecto = ProyectoUrbano(
            nombre=nombre,
            descripcion=descripcion,
            ubicacion=ubicacion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin if fecha_fin else None,
            contratista=contratista
        )
        proyecto.save()

        messages.success(request, 'Proyecto agregado correctamente.')
        return redirect('VerProyectos')

    # Si no es POST, renderizar formulario
    contratistas = Contratista.objects.all()
    return render(request, 'Proyectos/agregar_proyecto.html', {'contratistas': contratistas})

def editar_proyecto(request, id):
    proyecto = get_object_or_404(ProyectoUrbano, pk=id)
    contratistas = Contratista.objects.all()

    if request.method == 'POST':
        proyecto.nombre = request.POST['nombre']
        proyecto.descripcion = request.POST['descripcion']
        proyecto.ubicacion = request.POST['ubicacion']
        proyecto.fecha_inicio = request.POST['fecha_inicio']
        proyecto.fecha_fin = request.POST['fecha_fin']
        
        # Obtener el contratista seleccionado
        contratista_id = request.POST.get('contratista')
        if contratista_id:
            proyecto.contratista = get_object_or_404(Contratista, pk=contratista_id)
        else:
            proyecto.contratista = None

        proyecto.save()

        messages.success(request, 'Proyecto editado correctamente.')
        return redirect('VerProyectos')

    return render(request, 'Proyectos/editar_proyecto.html', {
        'proyecto': proyecto,
        'contratistas': contratistas,
        'contratista_seleccionado': proyecto.contratista.id if proyecto.contratista else None
    })

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(ProyectoUrbano, pk=id)
    proyecto.delete()
    messages.success(request, 'Proyecto eliminado correctamente.')
    return redirect('VerProyectos')

# ----------------------------------------------------------------
# ZONAS VERDES
# ----------------------------------------------------------------

def VerZonas(request):
    zonas = ZonaVerde.objects.all()
    proyectos = ProyectoUrbano.objects.all()
    return render(request, 'Zonas/inicio_zonas.html', {'zonas': zonas, 'proyectos': proyectos, 'active_page': 'zonas'})

def agregar_zona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        area = request.POST.get('area')
        ubicacion = request.POST.get('ubicacion')
        proyecto_id = request.POST.get('proyecto')
        foto = request.FILES.get('foto')
        # Obtener proyecto si existe
        proyecto = get_object_or_404(ProyectoUrbano, pk=proyecto_id) if proyecto_id else None

        # Guardar la zona
        zona = ZonaVerde(
            nombre=nombre,
            area=area,
            ubicacion=ubicacion,
            proyecto=proyecto,
            foto=foto
        )
        zona.save()

        messages.success(request, 'Zona agregada correctamente.')
        return redirect('VerZonas')

    # Si no es POST, renderizar formulario
    zonas = ZonaVerde.objects.all()
    proyectos = ProyectoUrbano.objects.all()
    return render(request, 'Zonas/agregar_zona.html', {'zonas': zonas, 'proyectos': proyectos})

def editar_zona(request, id):
    zona = get_object_or_404(ZonaVerde, pk=id)
    proyectos = ProyectoUrbano.objects.all()
    # Convertir el salario a un formato adecuado
    zona_area = f"{zona.area:.2f}"
    if request.method == 'POST':
        zona.nombre = request.POST.get('nombre')
        zona.area = request.POST.get('area')
        zona.ubicacion = request.POST.get('ubicacion')
        
        # Si el usuario sube una nueva imagen, la actualiza; si no, mantiene la anterior
        if 'foto' in request.FILES:
            zona.foto = request.FILES['foto']

        # Obtener el proyecto si existe
        proyecto_id = request.POST.get('proyecto')
        if proyecto_id:
            zona.proyecto = get_object_or_404(ProyectoUrbano, pk=proyecto_id)

        zona.save()
        messages.success(request, 'Zona editada correctamente.')
        return redirect('VerZonas')

    return render(request, 'Zonas/editar_zona.html', {'zona': zona, 'proyectos': proyectos, 'zona_area': zona_area})

def eliminar_zona(request, id):


    zona = get_object_or_404(ZonaVerde, pk=id)
    
    # Verifica si existe una foto asociada y la elimina
    if zona.foto:
        try:
            # Elimina el archivo de la foto del sistema de archivos
            if os.path.isfile(zona.foto.path):
                os.remove(zona.foto.path)
        except Exception as e:
            # Maneja cualquier error que pueda ocurrir al intentar eliminar el archivo
            print(f"Error al eliminar la foto: {e}")
    
    # Elimina la zona
    zona.delete()
    
    # Mensaje de éxito
    messages.success(request, 'Zona eliminada correctamente.')
    
    # Redirige a la vista de zonas
    return redirect('VerZonas')

# ----------------------------------------------------------------
# CONSTRUCCIONES
# ----------------------------------------------------------------

def VerConstrucciones(request):
    construcciones = ConstruccionSostenible.objects.all()
    proyectos = ProyectoUrbano.objects.all()
    return render(request, 'Construccion/inicio_construcciones.html', {'construcciones': construcciones, 'proyectos': proyectos, 'active_page': 'construcciones'})

def agregar_construccion(request):
    if request.method == 'POST':
        # Capturar los datos del formulario
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        materiales_sostenibles = request.POST['materiales']
        proyecto_id = request.POST.get('proyecto')  # Capturar ID del proyecto
        
        # Obtener el valor del campo 'sostenibilidad' (True o False)
        eficiencia_energetica = request.POST.get('eficiencia') == 'si'  # Si 'si' es seleccionado, es True

        # Obtener el proyecto si existe
        if proyecto_id:
            proyecto = get_object_or_404(ProyectoUrbano, pk=proyecto_id)
        else:
            proyecto = None

        # Crear y guardar la construcción sostenible
        construccion = ConstruccionSostenible(
            nombre=nombre,
            tipo=tipo,
            materiales_sostenibles=materiales_sostenibles,
            eficiencia_energetica=eficiencia_energetica,
            proyecto=proyecto
        )
        construccion.save()

        # Mensaje de éxito y redirección
        messages.success(request, 'Construcción agregada correctamente.')
        return redirect('VerConstrucciones')

    # Si no es POST, renderizar formulario
    proyectos = ProyectoUrbano.objects.all()
    return render(request, 'Construccion/agregar_construcciones.html', {'proyectos': proyectos})

def editar_construccion(request, id):
    construccion = get_object_or_404(ConstruccionSostenible, pk=id)
    proyectos = ProyectoUrbano.objects.all()

    if request.method == 'POST':
        construccion.nombre = request.POST['nombre']
        construccion.tipo = request.POST['tipo']
        construccion.materiales_sostenibles = request.POST['materiales']
        construccion.eficiencia_energetica = request.POST['eficiencia'] == 'si'
        
        # Obtener el proyecto seleccionado
        proyecto_id = request.POST.get('proyecto')
        if proyecto_id:
            construccion.proyecto = get_object_or_404(ProyectoUrbano, pk=proyecto_id)
        else:
            construccion.proyecto = None

        construccion.save()

        messages.success(request, 'Construcción editada correctamente.')
        return redirect('VerConstrucciones')

    return render(request, 'Construccion/editar_construccion.html', {
        'construccion': construccion,
        'proyectos': proyectos,
        'proyecto_seleccionado': construccion.proyecto.id if construccion.proyecto else None
    })

def eliminar_construccion(request, id):
    construccion = get_object_or_404(ConstruccionSostenible, pk=id)
    construccion.delete()
    messages.success(request, 'Construcción eliminada correctamente.')
    return redirect('VerConstrucciones')
