from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

# Create your views here.


class CustomLoginView(LoginView):
    form_class  = LoginForm

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

@login_required
def home(request):
    return render (request, 'accounts/home.html')