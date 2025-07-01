from django.shortcuts import render
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Profesor


def leerProfesores(request):
      profesores = Profesor.objects.all() #trae todos los profesores
      return render(request, "AppCoder/formulario/leerProfesores.html", {"profesores": profesores})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return leerProfesores(request)
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})


def eliminarProfesor(request, id_profesor):
 
    profesor = Profesor.objects.get(id=id_profesor)  # Obtengo el profesor por su ID
    profesor.delete()
 
    return leerProfesores(request)
    # vuelvo al menú
    # profesores = Profesor.objects.all()  # trae todos los profesores
    # return render(request, "AppCoder/formulario/leerProfesores.html", {"profesores": profesores})


def editarProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)  # Recibe el nombre del profesor que vamos a modificar
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            return leerProfesores(request)

    else:
        miFormulario = ProfesorFormulario(
            initial={
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'email': profesor.email,
                'profesion': profesor.profesion
                }
        )

    return render(request, "AppCoder/formulario/editarProfesor.html", {"miFormulario": miFormulario, "profesor_id": profesor.id})
