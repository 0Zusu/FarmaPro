from django.shortcuts import render,get_object_or_404
from .models import Receta
from .forms import formulario
#from .forms import FiltroBusqueda
# Create your views here.
#def verRecetas(request):
    #Recetas = Receta.objects.all()
    #return render(request, 'receta.html',{"Receta":Recetas})

def paciente (request):
    return render(request, "paciente.html")

#def medico (request):
    #return render (request,"medico.html")

def busqueda (request):
    if request.method=='GET':
        buscar = request.GET.get('rut')
        recetas = Receta.objects.all().filter(RutPaciente=buscar)
        print(recetas)
        return render(request, 'receta.html',{'recetas':recetas})

def medico(request):
    form = formulario()
    if request.method == "POST":
         form = formulario(data=request.POST)
         if form.is_valid():
             print("funciona")
             NombrePaciente = request.POST.get("NombrePaciente",'')
             rutpaciente = request.POST.get("RutPaciente",'')
             nombremed = request.POST.get("NombreMedicamento",'')
             dosis = request.POST.get("Dosis",'')
             motivo = request.POST.get("Motivo",'')
             firma = request.FILES['Firma']

             nueva_receta = Receta(NombrePaciente=NombrePaciente,RutPaciente=rutpaciente,NombreMedicamento=nombremed,Dosis=dosis,Motivo=motivo,Firma=firma)
             nueva_receta.save()
             form=formulario()
         else:
            print("nofunciona nah")
    recetas = Receta.objects.all()
    return render(request,"medico.html",{'form':form,'recetas':recetas})

def DetalleReceta(request,receta_id):
    recetas = get_object_or_404(Receta,id=receta_id)
    return render(request,"ver_receta.html",{'recetas':recetas})