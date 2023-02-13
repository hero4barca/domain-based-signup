
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    def __init__(self, *args, **kwargs):
        
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name','password1', 'password2')