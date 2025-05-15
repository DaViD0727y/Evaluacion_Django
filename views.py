from django.shortcuts import render,HttpResponse  



def Home(request):
    return render,(request,'core/Home.html')
def soporte(request):
    return render,(request,'core/Soporte.html')
def productos(request):
    return render,(request,'core/Productos.html')




# Create your views here.
