from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect 
from .forms import *

# Create your views here.
def obrazek_view(request): 
  
    if request.method == 'POST': 
        form = ObrazekForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ObrazekForm() 
    return render(request, 'obrazek_view.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded')
