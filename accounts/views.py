from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)