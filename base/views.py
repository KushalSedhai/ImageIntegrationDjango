from django.shortcuts import render
from .models import receipe

def home(request):
    ress = receipe.objects.all()
    return render (request, 'index.html', context={'ress':ress})



# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        receipe.objects.create(name=name, pic=image)
    return render(request, 'create.html')