from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site 
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .tokens import account_activation_token
from django.utils.encoding import force_bytes 
from django.core.mail import EmailMessage  

from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomLoginView(LoginView):
    form_class  = LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            form.save()

            send_activation_email(user_email, request)
            messages.success(request, f'Your account has been created. You can log in now!') 
               
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def home(request):
    return render (request, 'accounts/home.html')


def send_activation_email(user_email, request):

    user = User.objects.filter(email=user_email).first()
    if user:
        current_site = get_current_site(request)
        subject = 'Activate your Wentors membership Account'

        message = render_to_string('accounts/email/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
    
        # send email 
        email = EmailMessage( subject, 
                    message,                 
                to= [user.email]) 

        email.send()