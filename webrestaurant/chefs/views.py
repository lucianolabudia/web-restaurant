from django.shortcuts import render
from . models import Chef

# Create your views here.
def chefs(request):
    chefs = Chef.objects.all()
    return render(request, 'chefs/chefs.html', {'chefs': chefs})

