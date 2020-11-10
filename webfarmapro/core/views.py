from django.shortcuts import render,HttpResponse

# Create your views here.

def home (request):
    return render(request, "index.html",{'titulo':'FarmaPro'})
def paciente (request):
    return render(request, "paciente.html")