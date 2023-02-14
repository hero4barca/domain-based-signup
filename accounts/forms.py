
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import WhitelistEmails, WhitelistDomains
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field 
from crispy_bootstrap5.bootstrap5 import FloatingField

class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    
    class Meta:
            model = get_user_model()
            fields = ('email', 'username', 'first_name', 'last_name','password1', 'password2')
    
    def __init__(self, *args, **kwargs):        
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)


    def clean_email(self):
        email = self.cleaned_data['email']
        email_id, email_domain = email.split("@")

        if self.check_email(email) == False and self.check_email_domain(email_domain) == False:
            raise forms.ValidationError("Unknown email domain. Please contact your domain admin")
        return email

    
    def check_email(self, email):
        """
        Checks if email is whitelisted, returns Boolean
        """
        confirm_email = WhitelistEmails.objects.filter(email = email).first()

        if not confirm_email:
            return False
        else:
            if confirm_email.is_active: 
                return True
            else:
                return False

    
    def check_email_domain(self, email_domain):
        """
        checks if email domain is whitelisted, returns Boolean
        """
        confirm_email_domain = WhitelistDomains.objects.filter(domain = email_domain).first()

        if not confirm_email_domain:
            return False
        else:
            if confirm_email_domain.is_active:
                return True
            else:
                return False

    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("Inactive account!!. Please ensure that your account is activated via email"),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            
             Div(                
                Div(FloatingField("username") ),
                css_class='mt-1, mb-1',
            ),
            Div(                
                Div(FloatingField("password") ),
                css_class='mt-1, mb-1',
            ),
        )
