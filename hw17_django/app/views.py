from django.shortcuts import render, redirect
from .forms import IceCreamForm
from django.views.generic import ListView
from .models import IceCream

class IceCreamList(ListView):
    model = IceCream
    template_name = 'list.html'
    context_object_name = 'ice_creams'

def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IceCreamForm()
    return render(request, 'create.html', {'form': form})