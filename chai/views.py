from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store  # Store model ko import karna zaroori hai
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    Chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': Chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    # Fix 1: Dictionary ki key aur value ke beech colon ':' ki jagah arrow ya colon sahi format mein hona chahiye (jaise {'chai': chai})
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            # Fix 2: Query ko ek hi line mein likhein ya parentheses ke andar properly wrap karein taaki syntax error na aaye
            stores = Store.objects.filter(chai_varities=chai_variety)
    else:
        form = ChaiVarityForm()
       
    return render(request, 'chai/chai_store.html', {'stores': stores, 'form': form})