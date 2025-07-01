from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ..models import Avatar, Estudiante, Profesor, Curso, Entregable
from ..forms import CursoFormulario, ProfesorFormulario

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante_detail.html', {'estudiante': estudiante})


def inicio(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    return render(request, "AppCoder/index.html", {"avatar": avatar if avatar else None})

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")


# def cursoFormulario(request):
#       return render(request, "AppCoder/formulario/cursoFormulario.html")




# def cursoFormulario(request):
#       if request.method == 'POST':
#             curso =  Curso(nombre=request.POST['nombre'],camada=(request.POST['camada']))
#             curso.save()
#             return render(request, "AppCoder/index.html")
#       return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario2(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        camada = request.GET['camada']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)
