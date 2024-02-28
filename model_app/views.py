from django.shortcuts import render, redirect
from .forms import StudentsForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = StudentsForm()

    return render(request, 'index.html', {'form': form})
